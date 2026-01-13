import sys, random
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QPoint
from PySide6.QtGui import QFontMetrics, QGuiApplication

active_notifications = []
MAX_NOTIFICATIONS = 5

FIXED_HEIGHT = 80
MIN_WIDTH = 250

LABEL_PADDING_Y = 10
LABEL_PADDING_X = 32
LAYOUT_MARGIN = 10

class NotificationBar(QWidget):
    margin = 10

    def __init__(self, message: str, duration=3000):
        super().__init__()
        self.duration = duration

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedHeight(FIXED_HEIGHT)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(LAYOUT_MARGIN, LAYOUT_MARGIN,
                                  LAYOUT_MARGIN, LAYOUT_MARGIN)

        self.label = QLabel(message)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.label.setStyleSheet(f"""
            QLabel {{
                color: #333;
                background-color: rgba(255, 255, 255, 220);
                border-radius: 4px;
                padding: {LABEL_PADDING_Y}px {LABEL_PADDING_X}px;
                font-size: 14px;
            }}
        """)
        layout.addWidget(self.label)

        fm = QFontMetrics(self.label.font())
        text_width = fm.horizontalAdvance(message)

        final_width = max(
            MIN_WIDTH,
            text_width
            + LABEL_PADDING_X * 2
            + LAYOUT_MARGIN * 2
        )
        self.setFixedWidth(final_width)

        if len(active_notifications) >= MAX_NOTIFICATIONS:
            oldest = active_notifications.pop(0)
            oldest.fade_out()
        active_notifications.append(self)

        self.update_position(animated=False)

        self.setWindowOpacity(0.0)
        self.show()

        self.fade_in_anim = QPropertyAnimation(self, b"windowOpacity", self)
        self.fade_in_anim.setDuration(300)
        self.fade_in_anim.setStartValue(0.0)
        self.fade_in_anim.setEndValue(1.0)
        self.fade_in_anim.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_in_anim.start()

        QTimer.singleShot(duration, self.fade_out)

    def update_position(self, animated=True):
        screen = QGuiApplication.primaryScreen()
        rect = screen.availableGeometry()

        x = rect.right() - self.width() - 10
        index = active_notifications.index(self)

        y = rect.bottom() - FIXED_HEIGHT - 10
        for i in range(index):
            y -= FIXED_HEIGHT + NotificationBar.margin

        target_pos = QPoint(x, y)

        if animated:
            if hasattr(self, "move_anim") and self.move_anim.state() == QPropertyAnimation.Running:
                self.move_anim.stop()
            self.move_anim = QPropertyAnimation(self, b"pos", self)
            self.move_anim.setDuration(300)
            self.move_anim.setEndValue(target_pos)
            self.move_anim.setEasingCurve(QEasingCurve.OutCubic)
            self.move_anim.start()
        else:
            self.move(target_pos)

    def fade_out(self):
        self.fade_out_anim = QPropertyAnimation(self, b"windowOpacity", self)
        self.fade_out_anim.setDuration(300)
        self.fade_out_anim.setStartValue(1.0)
        self.fade_out_anim.setEndValue(0.0)
        self.fade_out_anim.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_out_anim.finished.connect(self.close_notification)
        self.fade_out_anim.start()

    def close_notification(self):
        if self in active_notifications:
            index = active_notifications.index(self)
            active_notifications.pop(index)
            self.close()
            for n in active_notifications[index:]:
                n.update_position(animated=True)
                
    def show_notification(message: str):
        NotificationBar(f"{message} ", duration=2500)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     messages = [
#         "The program has minimzed to the system tray ",
#         "A new Ultra 2 Controller has been connected! ",
#         "A new Ultra 2 Controller has been removed! ",
#         "New firmware version is available for download ",
#         "New update for control center is available for download ",
#     ]

#     def show_random_notification():
#         NotificationBar(random.choice(messages), duration=4000)

#     timer = QTimer()
#     timer.timeout.connect(show_random_notification)
#     timer.start(random.randint(1000, 3000))

#     sys.exit(app.exec())
