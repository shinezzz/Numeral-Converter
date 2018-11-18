import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):

    def __init__(self):
       super().__init__()
       self.titie = "Numeral Converter"
       self.initUI()

    def initUI(self):
        """设置窗体的标题"""
        self.setWindowTitle(self.titie)
        """通过调用show()函数来显示窗口"""
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
