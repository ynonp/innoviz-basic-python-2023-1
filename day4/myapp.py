from PySide6.QtWidgets import *
from myapp_ui import Ui_MainWindow

def handle_button_click():
    file, _ = QFileDialog.getOpenFileName()
    with open(file, 'r') as f:
        content = f.read()
        ui.textEdit.setText(content)

app = QApplication()
w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)

# Code starts here
ui.myButton.clicked.connect(handle_button_click)
# ui.horizontalSlider.valueChanged.connect(...)

w.show()
app.exec()
