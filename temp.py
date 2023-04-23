#         step 1
import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
#           step 2
app=QApplication([])
window=QWidget()
window.setWindowTitle("PYQT App")
window.setGeometry(100, 100, 200, 80)
helloMsg=QLabel("<h1Hello, World! </h1>",parent=window)
helloMsg.move(60, 15)
