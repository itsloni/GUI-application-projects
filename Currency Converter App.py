import requests
from bs4 import BeautifulSoup

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QLabel, QPushButton

def get_currency():



def show_currency():
    input_label = text.text()
    input_label *
    output_label.setText(input_label)



app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter App")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)
text = QLineEdit()
layout.addWidget(text)


btn = QPushButton("Convert")
layout.addWidget(btn)
btn.clicked.connect(show_currency)


output_label = QLabel("")
layout.addWidget(output_label)
window.setLayout(layout)


window.show()
app.exec()