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

# def show_currency

app = QApplication([])
window = QWidget()
window.setWindowTitle("Advanced GUI Currency Converter")

v_layout = QVBoxLayout()
h_layout = QHBoxLayout()

input_currency_dropdown = QComboBox()
input_curr_list = ["EUR", "USD", "INR", "GBP", "SGD", "CAD", "KRW", "JPY"]
input_currency_dropdown.addItems(input_curr_list)
v_layout.addWidget(input_currency_dropdown)

text = QLineEdit()
v_layout.addWidget(text)

btn = QPushButton("convert")
v_layout.addWidget(btn)

output_label = QLabel("")
v_layout.addWidget(output_label)

window.setLayout(v_layout)
window.setLayout(h_layout)
window.show()
app.exec()