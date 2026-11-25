from bs4 import BeautifulSoup
import requests
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox

def get_currency(input_currency, output_currency):
    url = f"https://x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt title-36 text-content-base tabular-nums sm:title-48").get_text()
    cleaned_rate = float(rate[:-4])
    return cleaned_rate

def show_currency():
    input_text = float(text.text())
    input_currency = input_currency_dropdown.currentText()
    target_currency = target_currency_dropdown.currentText()
    rate = get_currency(input_currency, target_currency)
    result = str(round(input_text * rate, 2))
    message = f"{input_text} {input_currency} is {result} {target_currency}"
    output_label.setText(message)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Advanced GUI Currency Converter")

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel("")
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

input_currency_dropdown = QComboBox()
currency_list = ["EUR", "USD", "INR", "GBP", "SGD", "CAD", "KRW", "JPY"]
input_currency_dropdown.addItems(currency_list)
layout2.addWidget(input_currency_dropdown)

target_currency_dropdown = QComboBox()
target_currency_dropdown.addItems(currency_list)
layout2.addWidget(target_currency_dropdown)

text = QLineEdit()
layout3.addWidget(text)

btn = QPushButton("convert")
btn.clicked.connect(show_currency)
layout3.addWidget(btn)

window.setLayout(layout)
window.setLayout(layout1)
window.show()
app.exec()