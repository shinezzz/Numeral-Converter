from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys
from MainWindow import Ui_MainWindow

# Calculator state.


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.title = 'PyQt5 textbox'
        self.left = 200
        self.top = 200
        self.width = 320
        self.height = 300
        # self.setupUi(self)
        # self.retranslateUi(MainWindow)
        self.setGeometry(self.left, self.top, self.width, self.height)


        # creat a button
        button = QPushButton("10to2", self)
        button.setToolTip("10进制转化为2进制")
        button.move(100, 70)
        button.clicked.connect(self.on_click)

        button = QPushButton("10to8", self)
        button.setToolTip("10进制转化为8进制")
        button.move(100, 120)
        button.clicked.connect(self.on_click)

        button = QPushButton("10to16", self)
        button.setToolTip("10进制转化为16进制")
        button.move(100, 170)
        button.clicked.connect(self.on_click)

        #creat a input box
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)



        self.show()
    #TODO
    def on_click(self):
        print("PyQt5 button click")
        # textboxValue = self.textbox.text()
        self.textbox.setText('')


if __name__ == '__main__':

    app = QApplication([])
    app.setApplicationName("NumeralConverter")
    # app.height(200)
    # app.width(200)

    window = MainWindow()

    app.exec_()