from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
app = QApplication([])
window = QWidget()
window.setWindowTitle("Простий калькулятор")
window.move(50,30)
window.resize(500,500)
window.setStyleSheet('font-size: 18pt; font-family: Courier; background-color: yellow')
def fclear():
    textbox.setText("")

def fsuma():
    global f1
    global dia
    f1 = int(textbox.text())
    textbox.setText("")
    dia = 1

def fminus():
    global f1
    global dia
    f1 = int(textbox.text())
    textbox.setText("")
    dia = 2

def fdil():
    global f1
    global dia
    f1 = int(textbox.text())
    textbox.setText("")
    dia = 3

def fdob():
    global f1
    global dia
    f1 = int(textbox.text())
    textbox.setText("")
    dia = 4

def fone():
    textbox.setText(textbox.text()+"1")
def ftwo():
    textbox.setText(textbox.text()+"2")
def fzero():
    textbox.setText(textbox.text()+"0")
def ffree():
    textbox.setText(textbox.text()+"3")
def ffour():
    textbox.setText(textbox.text()+"4")
def ffive():
    textbox.setText(textbox.text()+"5")
def fsix():
    textbox.setText(textbox.text()+"6")
def fseven():
    textbox.setText(textbox.text()+"7")
def feight():
    textbox.setText(textbox.text()+"8")
def fnine():
    textbox.setText(textbox.text()+"9")

def fdoriv():
    f2 = int(textbox.text())
    if dia == 1:
        textbox.setText(str(f1+f2))
    if dia == 2:
        textbox.setText(str(f1-f2))
    if dia == 3:
        textbox.setText(str(f1*f2))
    if dia == 4:
        textbox.setText(str (f1/f2))

textbox = QLineEdit()

textbox = QLineEdit()
#textbox.move(320, 320)
one = QPushButton("1")
two = QPushButton("2")
free = QPushButton("3")
four = QPushButton("4")
five = QPushButton("5")
six = QPushButton("6")
seven = QPushButton("7")
eight = QPushButton("8")
nine = QPushButton("9")
zero = QPushButton("0")

suma = QPushButton("+")
minus = QPushButton("-")
doriv = QPushButton("=")
dob = QPushButton("*")
dil = QPushButton("/")
clear = QPushButton("CE")

one.setStyleSheet('background-color: lightblue')
two.setStyleSheet('background-color: lightblue')
free.setStyleSheet('background-color: lightblue')
four.setStyleSheet('background-color: lightblue')
five.setStyleSheet('background-color: lightblue')
six.setStyleSheet('background-color: lightblue')
seven.setStyleSheet('background-color: lightblue')
eight.setStyleSheet('background-color: lightblue')
nine.setStyleSheet('background-color: lightblue')
zero.setStyleSheet('background-color: lightblue')

dil.setStyleSheet('background-color: pink')
minus.setStyleSheet('background-color: pink')
dob.setStyleSheet('background-color: pink')
suma.setStyleSheet('background-color: pink')
doriv.setStyleSheet('background-color: pink')
clear.setStyleSheet('background-color: pink')

lineV= QVBoxLayout()
line= QHBoxLayout()
lineH= QHBoxLayout()
lineH1= QHBoxLayout()
lineH2= QHBoxLayout()
lineH3= QHBoxLayout()
lineH4= QHBoxLayout()
line.addWidget (textbox, alignment = Qt.AlignCenter)
lineH1.addWidget (one, alignment = Qt.AlignCenter)
lineH1.addWidget (two, alignment = Qt.AlignCenter)
lineH1.addWidget (free, alignment = Qt.AlignCenter)
lineH2.addWidget(four, alignment = Qt.AlignCenter)
lineH2.addWidget (five, alignment = Qt.AlignCenter)
lineH2.addWidget (six, alignment = Qt.AlignCenter)
lineH3.addWidget (seven, alignment = Qt.AlignCenter)
lineH3.addWidget (eight, alignment = Qt.AlignCenter)
lineH3.addWidget (nine, alignment = Qt.AlignCenter)
lineH4.addWidget (zero, alignment = Qt.AlignCenter)

lineH.addWidget (suma, alignment = Qt.AlignCenter)
lineH.addWidget (dil, alignment = Qt.AlignCenter)
lineH.addWidget (dob, alignment = Qt.AlignCenter)
lineH.addWidget (minus, alignment = Qt.AlignCenter)
lineH.addWidget (doriv, alignment = Qt.AlignCenter)
lineH.addWidget(clear, alignment = Qt.AlignCenter)

lineV.addLayout(line)
lineV.addLayout (lineH)
lineV.addLayout(lineH1)
lineV.addLayout(lineH2)
lineV.addLayout (lineH3)
lineV.addLayout (lineH4)
window.setLayout(lineV)

one.clicked.connect(fone)
two.clicked.connect(ftwo)
free.clicked.connect(ffree)
four.clicked.connect(ffour)
five.clicked.connect(ffive)
six.clicked.connect(fsix)
seven.clicked.connect(fseven)
eight.clicked.connect(feight)
nine.clicked.connect(fnine)
zero.clicked.connect(fzero)

suma.clicked.connect(fsuma)
doriv.clicked.connect(fdoriv)
minus.clicked.connect(fminus)
dil.clicked.connect(fdil)
dob.clicked.connect(fdob)
clear.clicked.connect(fclear)

textbox.setStyleSheet('background-color: green; color: rgb(255, 255, 255);')

textbox.setFixedWidth(500)
textbox.setFixedHeight(100)
window.show()
app.exec_()