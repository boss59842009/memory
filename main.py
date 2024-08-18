from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *
main_window.show()
app.exec_()