from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random
app = QApplication([])
ex = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(ex)

def generate():
    letters = "qwertyuiopasdfghjklzxcvbnm" 
    nambers = "1234567890"
    password_length = 16
    password_list = []
    for i in range(password_length):
        if ui.use_letters.isChecked():
            random_letter = random.choice(letters)
            password_list.append(random_letter)
        if ui.use_numders.isChecked():
            random_naber = random.choice(nambers)
            password_list.append(random_naber)

    password_str = "".join(password_list)
    ui.resuit.setText(password_str)

ui.generate_btn.clicked.connect(generate)
ex.show()
app.exec()