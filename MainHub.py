#Python 3.6
#Install PyQt5==5.9.2
#https://build-system.fman.io/pyqt5-tutorial
# git clone git://github.com/sympy/sympy.git
import os
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Select Script')

comboBox = QComboBox()





def on_button_clicked():
	alert = QMessageBox()
	alert.setText('Test Click')
	alert.exec_()


def sortThroughScripts(comboBox):
	directory = 'C:\\Users\\Kishan\\Desktop\\git_repos\\Pre-Calc_ulator'
	for filename in os.listdir(directory):
		if filename.endswith('.py'):
			comboBox.addItem(filename[0:len(filename)-3])
			continue
		else:
			continue

sortThroughScripts(comboBox)

layout.addWidget(comboBox)
layout.addWidget(button)

window.setLayout(layout)
window.show()

button.clicked.connect(on_button_clicked)
app.exec_()




