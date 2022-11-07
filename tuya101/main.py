# from PyQt6 import QtWidgets
# from tuya_auth import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

def window():


    def pp():
        print("fuck")
    # connecting and getting system information 
    app = QApplication(sys.argv)
    # creating the windows
    win = QMainWindow()
    # setting and sizing the window
    win.setGeometry(200, 200, 300, 300)
    # set a name for the window
    win.setWindowTitle("The new Home!")

    # creating a lable 
    label = QLabel(win)
    # set label text 
    label.setText("first label")
    # setting the lable positiojn in the window 
    label.move(40, 50)

    button = QPushButton(win)
    button.setText("first but")
    button.move(80, 80)
    button.setCheckable(True)
    button.clicked.connect(pp)



    win.show()



    sys.exit(app.exec())
    # app.exec()

window()

