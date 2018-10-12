


# this file needs to contain a method for the following:
# way to create branches
# an over arching directory for branches
# a way to name each branch
# a way to delete each branch (password protected?)
# take names in from profile for creating comments in branch or to say who made each branch
# a way to go from branch to branch
# a way to save contents of branch
# a way to report comments
#
# Tutorial for PyQt here:
# https://pythonspot.com/category/pyqt5/
#
#
# widgets = interation to things
# layouts control the position of the widgets
# you add widgets to layout and change the layouts as you go
#
# a signal activates a slot (its a button that activates a method)
# Slots and Signals should be on the same class for simplicity
#
#

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )