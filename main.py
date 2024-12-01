import sys
import random
from PyQt6 import QtWidgets, QtGui, QtCore


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        self.pushButton = QtWidgets.QPushButton("Нажми на меня", self)
        self.pushButton.setGeometry(350, 20, 100, 40)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        radius = random.randint(10, 100)
        center_x = self.width() // 2
        center_y = self.height() // 2
        self.circles.append((center_x, center_y, radius))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for x, y, radius in self.circles:
            painter.drawEllipse(QtCore.QPoint(x, y), radius, radius)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())