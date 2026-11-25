# GUI Application Projects

A collection of desktop GUI applications built with **Python** and **PyQt6**. This repository showcases various practical desktop utilities, ranging from text formatting and currency conversion to file management.

## Projects Included

### 1. Currency Converter (`currency_converter_app.py`)
A straightforward desktop application built with PyQt6 that allows users to convert amounts between different currencies through a clean graphical interface.

### 2. Currency Converter 2.0 (`currency_converter_app_2.0.py`)
An upgraded iteration of the original currency converter featuring an improved, more advanced PyQt6 layout and enhanced user interface design.

### 3. File Destroyer GUI (`file_destroyer_gui_app.py`)
A desktop utility designed to permanently delete selected files from the system. 
* **Tech Stack:** Built with **PyQt6** for the user interface and Python's **`pathlib`** module for modern, reliable file path handling.

### 4. Sentence Builder GUI (`sentence_builder_gui_app.py`)
A lightweight text-cleaning and formatting tool powered by PyQt6. It takes raw text input from the user and automatically formats it into a proper sentence by capitalizing the first letter and adding a full stop (period) at the end.

---

## Technologies Used
* **Python 3**
* **PyQt6** – Graphical User Interface (GUI) framework
* **pathlib** – Object-oriented filesystem paths (used in *File Destroyer GUI*)

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd GUI-Application-Projects
   ```

2. **Install the required dependency:**
   ```bash
   pip install PyQt6
   ```

3. **Run any of the applications:**
   ```bash
   python currency_converter_app.py
   python currency_converter_app_2.0.py
   python file_destroyer_gui_app.py
   python sentence_builder_gui_app.py
   ```

---

## What I Learned
* Building event-driven desktop interfaces using PyQt6 widgets, layouts, and signals/slots.
* Upgrading and refactoring UI designs for better usability.
* Handling local file paths safely with `pathlib` and automating string formatting in Python.
