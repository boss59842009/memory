from PyQt5.QtWidgets import QApplication

app = QApplication([]) # створення додатку

from main_window import *
from menu_window import *

main_window.show()

def to_menu():
    main_window.hide()
    menu_window.show()

def to_main():
    menu_window.hide()
    main_window.show()

btn_menu.clicked.connect(to_menu)
btn_back.clicked.connect(to_main)

app.exec_()