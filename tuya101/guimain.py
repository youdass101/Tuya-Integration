# from PyQt6 import QtWidgets
from tuya_auth import *

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

def window():

    plug = tuya_auth()
    def on():
        plug.turnon()

    def off():
        plug.turnoff()


    # connecting and getting system information 
    app = QApplication(sys.argv)
    # creating the windows
    win = QMainWindow()
    # setting and sizing the window
    win.setGeometry(200, 200, 300, 300)
    # set a name for the window
    win.setWindowTitle("The new Home!")

    # creating a lable 
    # label = QLabel(win)
    # set label text 
    # label.setText("first label")
    # setting the lable positiojn in the window 
    # label.move(40, 50)

    offplug = QPushButton(win)
    offplug.setText("Plug On")
    offplug.move(80, 80)
    offplug.setCheckable(True)
    offplug.clicked.connect(on)

    onplug = QPushButton(win)
    onplug.setText("PLug Off")
    onplug.move(80, 50)
    onplug.setCheckable(True)
    onplug.clicked.connect(off)



    win.show()



    sys.exit(app.exec())
    # app.exec()

window()

