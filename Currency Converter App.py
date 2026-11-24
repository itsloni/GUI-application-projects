import requests
from bs4 import BeautifulSoup

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QLabel, QPushButton, QComboBox #Note: "QComboBox" is the class of 'PyQt6' that allows the dynamic dropdown list design.

def get_currency(input_currency, output_currency):
    url = f"https://x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt title-36 text-content-base tabular-nums sm:title-48").get_text()
    cleaned_rate = float(rate[:-4])
    return cleaned_rate


# rate = get_currency("USD", "EUR")

def show_currency():
    input_label = float(text.text())
    input_currency = input_label_combo.currentText()
    target_currency = target_label_combo.currentText()
    rate = get_currency(input_currency, target_currency)
    result = str(round(input_label * rate, 2))
    message = f"{input_label} {input_currency} is {result} {target_currency}"
    output_label.setText(message)



app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter App")


layout = QVBoxLayout()
layout.setContentsMargins(100, 100, 100, 100)


input_label_combo = QComboBox()
list_of_Currency = ["EUR", "USD", "INR", "GBP", "SGD", "CAD", "KRW", "JPY"]
input_label_combo.addItems(list_of_Currency)
layout.addWidget(input_label_combo)

target_label_combo = QComboBox()
target_label_combo.addItems(list_of_Currency)
layout.addWidget(target_label_combo)

text = QLineEdit()
layout.addWidget(text)

# text = QLineEdit()
# layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)
btn.clicked.connect(show_currency)


output_label = QLabel("")
layout.addWidget(output_label)
window.setLayout(layout)


window.show()
app.exec()