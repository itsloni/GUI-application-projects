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

v_layout = QVBoxLayout()
h_layout = QHBoxLayout()

v_layout.addWidget(h_layout)
output_label = QLabel("")
v_layout.addWidget(output_label)



input_currency_dropdown = QComboBox()
currency_list = ["EUR", "USD", "INR", "GBP", "SGD", "CAD", "KRW", "JPY"]
input_currency_dropdown.addItems(currency_list)
v_layout.addWidget(input_currency_dropdown)

target_currency_dropdown = QComboBox()
target_currency_dropdown.addItems(currency_list)
v_layout.addWidget(target_currency_dropdown)


text = QLineEdit()
v_layout.addWidget(text)

btn = QPushButton("convert")
v_layout.addWidget(btn)



window.setLayout(v_layout)
window.setLayout(h_layout)
window.show()
app.exec()