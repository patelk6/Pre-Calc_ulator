#Python 3.6
#Install PyQt5==5.9.2
#https://build-system.fman.io/pyqt5-tutorial
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel('Hello World!')

label.show()

app.exec_()