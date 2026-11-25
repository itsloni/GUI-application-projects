from textwrap import indent

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtWidgets import QFileDialog
from pathlib import Path
from PyQt6.QtCore import Qt

def select_file():
    filenames, _ = QFileDialog.getOpenFileNames(window, "select files")
    output_label.setText(str(filenames))
    return filenames

#
def destroy_file():
    filenames, _ = select_file()
    for filename in filenames:
        path = Path(filename)
        with open (path, "wb") as file:
            file.write(b"")
        path.unlink()
#

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()

description_label = QLabel("Select the files you want to destroy. The files with be <font color='red'>permanently</font> deleted")
layout.addWidget(description_label)

btn1 = QPushButton("select file")
btn1.setToolTip("open")
btn1.setFixedWidth(100)
btn1.clicked.connect(select_file)
layout.addWidget(btn1, alignment = Qt.AlignmentFlag.AlignCenter)

btn2 = QPushButton("Destroy File")
btn2.setToolTip("delete")
btn2.setFixedWidth(100)
# btn1.clicked.connect(select_file)
# btn2.clicked.connect(destroy_file)
layout.addWidget(btn2, alignment = Qt.AlignmentFlag.AlignCenter)



output_label = QLabel("")
layout.addWidget(output_label)


window.setLayout(layout)
window.show()
app.exec()