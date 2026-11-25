from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel
from pathlib import Path

def select_file():

def destroy_file():



app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()

btn1 = QPushButton("select file")
btn1.clicked.connect(select_file)
layout.addWidget(btn1)

btn2 = QPushButton("Destroy File")
btn2.clicked.connect(destroy_file)
layout.addWidget(btn2)

instruction_label = QLabel("Select the files you want to destroy. The files with be permanently deleted")
layout.addWidget(instruction_label)

output_label = QLabel("")
layout.addWidget(output_label)


window.setLayout(layout)
window.show()
app.exec()