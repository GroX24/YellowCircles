import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        self.do_paint = False
        self.circles = []
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(0, 0, 0))
            qp.setBrush(QColor(255, 255, 0))
            size = randint(2, 400)
            self.circles.append((randint(-size, self.width()), randint(-size, self.height()), size, size))
            for i in self.circles:
                qp.drawEllipse(*i)
            qp.end()
            self.do_paint = False

    def drawycircles(self, qp):

        qp.drawEllipse(randint(0, self.width()), randint(0, self.height()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())