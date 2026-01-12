import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QFont, QMouseEvent
from PySide6.QtCore import Qt, QPoint, QRect, Signal

class FanCurveWidget(QWidget):
    curveChanged = Signal(QPoint, QPoint) 

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMinimumSize(281, 181)
        self.setMouseTracking(True)

        self.p1 = QPoint(30, 20)
        self.p2 = QPoint(70, 80)
        
        self.active_point = None
        self.margin = 30
        self.point_radius = 5

    def to_screen(self, temp, speed):
        w_area = self.width() - 2 * self.margin
        h_area = self.height() - 2 * self.margin
        x = self.margin + (temp / 100) * w_area
        y = self.height() - self.margin - (speed / 100) * h_area
        return QPoint(x, y)

    def from_screen(self, x, y):
        w_area = self.width() - 2 * self.margin
        h_area = self.height() - 2 * self.margin
        temp = (x - self.margin) / w_area * 100
        speed = (self.height() - self.margin - y) / h_area * 100
        return max(0, min(100, int(temp))), max(0, min(100, int(speed)))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor(255, 255, 255, 0))

        axis_pen = QPen(QColor("#333333"), 2)
        grid_pen = QPen(QColor("#F0F0F0"), 1)
        painter.setFont(QFont("Segoe UI", 8))

        origin = QPoint(self.margin, self.height() - self.margin)
        x_end = QPoint(self.width() - self.margin, self.height() - self.margin)
        y_end = QPoint(self.margin, self.margin)

        for i in range(0, 101, 20):
            px = self.to_screen(i, 0)
            py = self.to_screen(0, i)
            painter.setPen(grid_pen)
            painter.drawLine(px.x(), self.margin, px.x(), origin.y())
            painter.drawLine(origin.x(), py.y(), self.width() - self.margin, py.y())
            
            painter.setPen(axis_pen)
            painter.drawText(QRect(px.x() - 20, origin.y() + 8, 40, 20), Qt.AlignCenter, f"{i}")
            painter.drawText(QRect(origin.x() - 40, py.y() - 10, 35, 20), Qt.AlignRight | Qt.AlignVCenter, f"{i}%")

        painter.setPen(axis_pen)
        painter.drawLine(origin, x_end)
        painter.drawLine(origin, y_end)
        painter.drawText(self.width() - self.margin + 5, origin.y() + 5, "°C")

        status_text = f"Fan Speed Curve Set: "
        painter.drawText(self.margin, self.margin - 15, status_text)

        painter.setPen(QPen(QColor("#3498DB"), 3))
        sp1 = self.to_screen(self.p1.x(), self.p1.y())
        sp2 = self.to_screen(self.p2.x(), self.p2.y())
        painter.drawLine(self.to_screen(0, self.p1.y()), sp1)
        painter.drawLine(sp1, sp2)
        painter.drawLine(sp2, self.to_screen(100, self.p2.y()))

        for name, pt in [("p1", self.p1), ("p2", self.p2)]:
            screen_pt = self.to_screen(pt.x(), pt.y())
            
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, 50))
            painter.drawEllipse(screen_pt + QPoint(1, 1), self.point_radius, self.point_radius)
            
            color = QColor("#E74C3C") if self.active_point == name else QColor("#2C3E50")
            painter.setBrush(color)
            painter.setPen(QPen(Qt.white, 2))
            painter.drawEllipse(screen_pt, self.point_radius, self.point_radius)

            label = f"{pt.x()}°C, {pt.y()}%"
            
            off_x, off_y = 12, -10
            
            if screen_pt.x() > self.width() - 80:
                off_x = -75
            
            if screen_pt.y() < 40:
                off_y = 25
                
            painter.setPen(QColor("#333"))
            painter.drawText(screen_pt.x() + off_x, screen_pt.y() + off_y, label)
            
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            m_pos = event.position().toPoint()
            for name, pt in [("p1", self.p1), ("p2", self.p2)]:
                if (self.to_screen(pt.x(), pt.y()) - m_pos).manhattanLength() < 25:
                    self.active_point = name
                    break
            self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.active_point:
            m_pos = event.position().toPoint()
            temp, speed = self.from_screen(m_pos.x(), m_pos.y())
            if self.active_point == "p1":
                self.p1.setX(min(temp, self.p2.x() - 5))
                self.p1.setY(min(speed, self.p2.y() - 5))
            else:
                self.p2.setX(max(temp, self.p1.x() + 5))
                self.p2.setY(max(speed, self.p1.y() + 5))
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.active_point:
            self.curveChanged.emit(self.p1, self.p2)
            self.active_point = None
            self.update()
            
class FanNoCurveWidget(QWidget):
    curveChanged = Signal(QPoint) 

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMinimumSize(281, 181)
        self.setMouseTracking(True)

        self.p1 = QPoint(50, 50)
        
        self.active_point = None
        self.margin = 30
        self.point_radius = 5

    def to_screen(self, temp, speed):
        w_area = self.width() - 2 * self.margin
        h_area = self.height() - 2 * self.margin
        x = self.margin + (temp / 100) * w_area
        y = self.height() - self.margin - (speed / 100) * h_area
        return QPoint(x, y)

    def from_screen(self, x, y):
        h_area = self.height() - 2 * self.margin
        speed = (self.height() - self.margin - y) / h_area * 100
        return 50, max(0, min(100, int(speed)))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor(255, 255, 255, 0))

        axis_pen = QPen(QColor("#333333"), 2)
        grid_pen = QPen(QColor("#F0F0F0"), 1)
        painter.setFont(QFont("Segoe UI", 8))

        origin = QPoint(self.margin, self.height() - self.margin)
        x_end = QPoint(self.width() - self.margin, self.height() - self.margin)
        y_end = QPoint(self.margin, self.margin)

        for i in range(0, 101, 20):
            px = self.to_screen(i, 0)
            py = self.to_screen(0, i)
            painter.setPen(grid_pen)
            painter.drawLine(px.x(), self.margin, px.x(), origin.y())
            painter.drawLine(origin.x(), py.y(), self.width() - self.margin, py.y())
            
            painter.setPen(axis_pen)
            painter.drawText(QRect(px.x() - 20, origin.y() + 8, 40, 20), Qt.AlignCenter, f"{i}")
            painter.drawText(QRect(origin.x() - 40, py.y() - 10, 35, 20), Qt.AlignRight | Qt.AlignVCenter, f"{i}%")

        painter.setPen(axis_pen)
        painter.drawLine(origin, x_end)
        painter.drawLine(origin, y_end)
        painter.drawText(self.width() - self.margin + 5, origin.y() + 5, "°C")

        status_text = f"Fixed Fan Speed: "
        painter.drawText(self.margin, self.margin - 10, status_text)

        line_pen = QPen(QColor("#3498DB"), 3)
        painter.setPen(line_pen)
        screen_y = self.to_screen(0, self.p1.y()).y()
        painter.drawLine(self.margin, screen_y, self.width() - self.margin, screen_y)

        screen_pt = self.to_screen(50, self.p1.y())
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 50))
        painter.drawEllipse(screen_pt + QPoint(1, 1), self.point_radius, self.point_radius)
        
        color = QColor("#E74C3C") if self.active_point else QColor("#2C3E50")
        painter.setBrush(color)
        painter.setPen(QPen(Qt.white, 2))
        painter.drawEllipse(screen_pt, self.point_radius, self.point_radius)

        label = f"{self.p1.y()}%"
        painter.setPen(QColor("#333"))
        painter.drawText(QRect(screen_pt.x() - 20, screen_pt.y() - 22, 40, 15), Qt.AlignCenter, label)
            
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            m_pos = event.position().toPoint()
            center_pt = self.to_screen(50, self.p1.y())
            if (center_pt - m_pos).manhattanLength() < 25:
                self.active_point = "p1"
                self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.active_point == "p1":
            m_pos = event.position().toPoint()
            _, speed = self.from_screen(m_pos.x(), m_pos.y())
            
            self.p1.setY(speed)
            self.p1.setX(50) 
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.active_point:
            self.curveChanged.emit(self.p1)
            self.active_point = None
            self.update()