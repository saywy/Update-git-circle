import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRect


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        radius = random.randint(10, 1000)
        x = (self.centralWidget().width() - radius) // 2
        y = (self.centralWidget().height() - radius) // 2
        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, radius) in self.circles:
            painter.drawEllipse(QRect(x, y, radius, radius))

    def resizeEvent(self, event):
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())

