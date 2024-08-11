from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton, QSpinBox, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup

main_window = QWidget()
main_window.resize(600, 500)
main_window.setWindowTitle("Memory card")
main_window.move(300, 300)

btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")

box_minutes = QSpinBox()
box_minutes.setValue(30)
box_minutes_lbl = QLabel("хвилин")

question_lbl = QLabel('Question')

answer_group_box = QGroupBox("Варіанти відповідей")
radio_buttons_group = QButtonGroup()
r_btn1 = QRadioButton('1')
r_btn2 = QRadioButton('2')
r_btn3 = QRadioButton('3')
r_btn4 = QRadioButton('4')

radio_buttons_group.addButton(r_btn1)
radio_buttons_group.addButton(r_btn2)
radio_buttons_group.addButton(r_btn3)
radio_buttons_group.addButton(r_btn4)

v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line = QHBoxLayout()

v_line1.addWidget(r_btn1)
v_line1.addWidget(r_btn2)

v_line2.addWidget(r_btn3)
v_line2.addWidget(r_btn4)

h_line.addLayout(v_line1)
h_line.addLayout(v_line2)
answer_group_box.setLayout(h_line)

result_group_box = QGroupBox("Результат теста")
lbl_correct = QLabel('')
lbl_right = QLabel('')

result_line = QVBoxLayout()
result_line.addWidget(lbl_correct, alignment=(Qt.AlignCenter|Qt.AlignTop))
result_line.addWidget(lbl_right, alignment=Qt.AlignCenter, stretch=3)
result_group_box.setLayout(result_line)
result_group_box.hide()