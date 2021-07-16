#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import DDui

class ExampleApp(QtWidgets.QMainWindow, DDui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()
