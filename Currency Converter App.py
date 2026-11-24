import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QLabel, QPushButton

def currency_converter():
    input_label = text.text()



app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter App")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)
# text = QLineEdit()
# layout.addWidget(text)


btn = QPushButton("Convert")
layout.addWidget(btn)
btn.clicked.connect(currency_converter)


output_label = QLabel("")
layout.addWidget(output_label)
window.setLayout(layout)


window.show()
app.exec()