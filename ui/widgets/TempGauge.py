from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt, QRectF

class TemperatureGauge(QWidget):
    def __init__(self, parent=None, value=0, min_temp=0, max_temp=100):
        super().__init__(parent)
        self.setMinimumSize(141, 141)
        
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.value = value
        
        self.line_width = 15
        self.total_angle = 300 
        self.padding = 25
        self.start_angle_conv = 90 + (self.total_angle / 2)

    def set_value(self, val):
        self.value = max(self.min_temp, min(val, self.max_temp))
        self.update()

    def paintEvent(self, event):
        width, height = self.width(), self.height()
        side = min(width, height)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(width / 2, height / 2)
        
        side = min(self.width(), self.height())
        rect = QRectF(-side/2 + self.padding, -side/2 + self.padding, 
                    side - self.padding*2, side - self.padding*2)

        bg_pen = QPen(QColor(230, 230, 230), self.line_width)
        bg_pen.setCapStyle(Qt.RoundCap)
        painter.setPen(bg_pen)
        painter.drawArc(rect, self.start_angle_conv * 16, -self.total_angle * 16)

        ratio = (self.value - self.min_temp) / (self.max_temp - self.min_temp)
        span_angle = -ratio * self.total_angle
        
        color = QColor(255, 85, 0) if self.value >= 50 else QColor(0, 150, 255)
        prog_pen = QPen(color, self.line_width)
        prog_pen.setCapStyle(Qt.RoundCap)
        painter.setPen(prog_pen)
        painter.drawArc(rect, self.start_angle_conv * 16, span_angle * 16)

        painter.setPen(QColor(50, 50, 50))
        painter.setFont(QFont("Arial", 14, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, f"{int(self.value)}°C")