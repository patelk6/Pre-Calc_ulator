import os
from PyQt5.QtWidgets import *


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Calculate ')

comboBox = QComboBox()

numerator_text = QLineEdit()
num = QLabel("Numerator")

layout.addWidget(num)

denom_text = QLineEdit()
den = QLabel("Denomnator")

layout.addWidget(num)
layout.addWidget(numerator_text)

layout.addWidget(den)
layout.addWidget(denom_text)


answer_label = QLabel("Your answer is:")

output_label = QLabel("2.5x^3+.25x^2+4.875x+1.0625" + " Remainder: " + "7.9375")

layout.addWidget(answer_label)
layout.addWidget(output_label)

layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()


