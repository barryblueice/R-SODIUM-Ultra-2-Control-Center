import sys
import ui.main_windows
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    app.setQuitOnLastWindowClosed(False)
    window = ui.main_windows.MainDialog()

    window.showNormal()
    window.activateWindow()
    app.exec()