#Python 3.6
#Install PyQt5==5.9.2
#https://build-system.fman.io/pyqt5-tutorial
# git clone git://github.com/sympy/sympy.git
from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Top')
layout.addWidget(button)
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()



def on_button_clicked():
	alert = QMessageBox()
	alert.setText('Test Click')
	alert.exec_()

button.clicked.connect(on_button_clicked)
app.exec_()




