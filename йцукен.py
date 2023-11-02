from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import QApplication,QFileDialog ,QLabel, QWidget, QPushButton,  QVBoxLayout, QHBoxLayout, QListWidget
app= QApplication([])

window = QWidget()
window.setWindowTitle("Easy editor")
window.resize(1000,700)
window.move(200,200)

def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   folder1()
   filenames = filter(os.listdir(workdir), extensions)
   listimg.clear()
   for filename in filenames:
       listimg.addItem(filename)
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
def folder1():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

folder = QPushButton()
folder.setText("Папка")

listimg = QListWidget()
winimg = QLabel()
winimg.setText("тут могла бути ваша реклама")


lineH = QHBoxLayout()  #головна лінія
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH1 = QHBoxLayout()

but_left = QHBoxLayout()
but_right = QHBoxLayout()
but_mirror = QHBoxLayout()
but_r = QHBoxLayout()
but_bw = QHBoxLayout()

lineH1.addWidget(but_left)
lineH1.addWidget(but_right)
lineH1.addWidget(but_mirror)
lineH1.addWidget(but_r)
lineH1.addWidget(but_bw)


lineV1.addWidget(folder)
lineV1.addWidget(listimg)
lineV2.addWidget(winimg)

lineH.addLayout(lineV1)

folder.clicked.connect(folder1)
window.setLayout(lineH)
window.show()
app.exec_()