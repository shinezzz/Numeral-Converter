from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)


        # # Setup the QTextEdit editor configuration
        # fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        # fixedfont.setPointSize(24)
        # self.editor.setFont(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        # self.path = None

        layout.addWidget(self.editor)

        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)
        #
        # self.status = QStatusBar()
        # self.setStatusBar(self.status)


        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("NumeralConverter")

    window = MainWindow()
    app.exec_()