from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

app = QApplication([])                              # This is the application instance
window =QWidget()                                 # This is where all the windows, labels and like the text buttons will be
window.setWindowTittle("Sentence Builder")      # To set a title for the window. Typically the name of the Application
window.show()                                 # To show what the window looks like atm
app.exec()                                  #To execute the app as it contains the window