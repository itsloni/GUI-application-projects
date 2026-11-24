from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QHBoxLayout


def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + ".")


app = QApplication([])                              # This is the application instance
window =QWidget()                                 # This is where all the windows, labels and like the text buttons will be
window.setWindowTitle("Sentence Builder")      # To set a title for the window. Typically the name of the Application

layout = QVBoxLayout() # This is for layout like the 'V' in QVBox... means vertical layout for the boxes(Like thy boxes will be stacked ontop of eachother). like you call this so that a box shows
# and there is obviously the QHBoxLayout where 'H' stands for Horizontal and the boxes are put side by side.

text = QLineEdit()  # This is for adding lines inside teh box created by the 'QVBoxLayout', but to actually put that lineedit inside yot add the line below this comment
layout.addWidget(text) # So this line now puts that LineEdit INSIDE THE LAYOUT 'QVBoxLayout'

btn =  QPushButton("Build Sentence")
layout.addWidget(btn)
btn.clicked.connect(make_sentence) # The 'clicked' is a widgets signal like the button has been clicked etc and the 'make_sentence' houses the functions(slots) that holds what will happen when the
# signal has been triggered like the button has been clicked. you call th signal and alot after youu create a button

output_label = QLabel("")
layout.addWidget(output_label)
window.setLayout(layout) # To then make the layout show in the window you must call it by using this line







window.show()                                 # To show what the window looks like atm
app.exec()                                  #To execute the app as it contains the window