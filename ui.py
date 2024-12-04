from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 324)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        Form.setFont(font)
        Form.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/vovas/Desktop/загружено.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 60, 221, 141))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 19, 151, 165))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 3, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 240, 51, 41))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 60, 211, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 20, 131, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout_3.addWidget(self.radioButton_7, 2, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 1, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_3.addWidget(self.radioButton_6, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 250, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 250, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generate_password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Programm"))
        self.groupBox.setTitle(_translate("Form", "Складність паролів"))
        self.radioButton_2.setText(_translate("Form", "Легкий"))
        self.radioButton.setText(_translate("Form", "Середній"))
        self.radioButton_3.setText(_translate("Form", "Дуже складний"))
        self.radioButton_4.setText(_translate("Form", "Складний"))
        self.label.setText(_translate("Form", "Пароль:"))
        self.groupBox_2.setTitle(_translate("Form", "Довжина пароля"))
        self.radioButton_7.setText(_translate("Form", "Середня"))
        self.radioButton_5.setText(_translate("Form", "Мала"))
        self.radioButton_6.setText(_translate("Form", "Велика"))
        self.pushButton.setText(_translate("Form", "Згенерувати пароль"))

    def generate_password(self):
        # Визначення складності
        if self.radioButton_2.isChecked():
            chars = string.ascii_lowercase
        elif self.radioButton.isChecked():
            chars = string.ascii_letters
        elif self.radioButton_4.isChecked():
            chars = string.ascii_letters + string.digits
        elif self.radioButton_3.isChecked():
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            self.lineEdit.setText("Оберіть складність")
            return

        # Визначення довжини
        if self.radioButton_5.isChecked():
            length = 8
        elif self.radioButton_7.isChecked():
            length = 12
        elif self.radioButton_6.isChecked():
            length = 16
        else:
            self.lineEdit.setText("Оберіть довжину")
            return

        # Генерація пароля
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
