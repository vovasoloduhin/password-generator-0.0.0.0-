from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 350)
        Form.setWindowTitle("Generator")
        icon = QtGui.QIcon("image.png")
        Form.setWindowIcon(icon)
        Form.setStyleSheet("""
            QWidget {
                background-color: #f7f7f7;
                font-family: 'Segoe UI';
                font-size: 12pt;
                color: #2c3e50;
            }
            QGroupBox {
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                margin-top: 15px;
                background-color: #ecf0f1;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 5px;
                font-size: 14pt;
                font-weight: bold;
                color: #34495e;
            }
            QLabel {
                font-weight: bold;
                font-size: 12pt;
                color: #34495e;
            }
            QRadioButton {
                spacing: 10px;
                color: #34495e;
                background: transparent;
            }
            QRadioButton::indicator {
                border: 2px solid #95a5a6;
                width: 15px;
                height: 15px;
                border-radius: 7px;
                background: #ecf0f1;
            }
            QRadioButton::indicator:checked {
                background-color: #2ecc71;
                border: 2px solid #27ae60;
            }
            QLineEdit {
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                padding: 5px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QPushButton {
                background-color: #3498db;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                color: white;
                font-weight: bold;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 250, 150))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Складність паролів")

        self.radioButton_easy = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_easy.setGeometry(QtCore.QRect(20, 30, 200, 20))
        self.radioButton_easy.setObjectName("radioButton_easy")
        self.radioButton_easy.setText("Легкий")

        self.radioButton_medium = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_medium.setGeometry(QtCore.QRect(20, 60, 200, 20))
        self.radioButton_medium.setObjectName("radioButton_medium")
        self.radioButton_medium.setText("Середній")

        self.radioButton_hard = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_hard.setGeometry(QtCore.QRect(20, 90, 200, 20))
        self.radioButton_hard.setObjectName("radioButton_hard")
        self.radioButton_hard.setText("Складний")

        self.radioButton_very_hard = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_very_hard.setGeometry(QtCore.QRect(20, 120, 200, 20))
        self.radioButton_very_hard.setObjectName("radioButton_very_hard")
        self.radioButton_very_hard.setText("Дуже складний")

        # Группа 2: Длина пароля
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 50, 250, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("Довжина пароля")

        self.radioButton_short = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_short.setGeometry(QtCore.QRect(20, 30, 200, 20))
        self.radioButton_short.setObjectName("radioButton_short")
        self.radioButton_short.setText("Мала")

        self.radioButton_medium_length = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_medium_length.setGeometry(QtCore.QRect(20, 60, 200, 20))
        self.radioButton_medium_length.setObjectName("radioButton_medium_length")
        self.radioButton_medium_length.setText("Середня")

        self.radioButton_long = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_long.setGeometry(QtCore.QRect(20, 90, 200, 20))
        self.radioButton_long.setObjectName("radioButton_long")
        self.radioButton_long.setText("Велика")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 220, 120, 30))
        self.label.setObjectName("label")
        self.label.setText("Пароль:")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 220, 200, 30))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 270, 200, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Згенерувати пароль")
        self.pushButton.clicked.connect(self.generate_password)  # Связь кнопки с функцией

    def generate_password(self):

        if self.radioButton_easy.isChecked():
            chars = string.ascii_lowercase
        elif self.radioButton_medium.isChecked():
            chars = string.ascii_letters
        elif self.radioButton_hard.isChecked():
            chars = string.ascii_letters + string.digits
        elif self.radioButton_very_hard.isChecked():
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_lowercase


        if self.radioButton_short.isChecked():
            length = 6
        elif self.radioButton_medium_length.isChecked():
            length = 10
        elif self.radioButton_long.isChecked():
            length = 16
        else:
            length = 8

        password = ''.join(random.choice(chars) for _ in range(length))
        self.lineEdit.setText(password)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
