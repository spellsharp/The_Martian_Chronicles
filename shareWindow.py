from PySide6 import QtCore, QtGui, QtWidgets
from PySide6 import QtCore, QtWidgets, QtGui

from PySide6.QtWidgets import QLabel, QLineEdit, QApplication
from PySide6.QtGui import QPixmap

import Fetch
import os
import ezgmail

cdPath = '/home/shrisharanyan/The_Martian_Chronicles/'
path = '/home/shrisharanyan/The_Martian_Chronicles/marsImages/'
imgList = os.listdir(path)

class ShareWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(430, 488)
        self.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #09011B;")

        self.centralwidget = QtWidgets.QWidget(self)
                
        self.enter = QtWidgets.QPushButton(self)
        self.enter.setText("Enter")
        
        self.enter.setGeometry(QtCore.QRect(160, 425, 89, 25))

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 361, 50))
        
        self.emailVert = QtWidgets.QVBoxLayout(self.widget)
        self.emailVert.setContentsMargins(0, 0, 0, 0)
        
        self.emailLabel = QtWidgets.QLabel(self.widget)
        self.emailLabel.setText("Email Id(s)")
        self.emailVert.addWidget(self.emailLabel)
        self.emailLine = QtWidgets.QLineEdit(self.widget)
        self.emailLine.setStyleSheet("background-color: #080117;")
        
        self.emailVert.addWidget(self.emailLine)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 100, 361, 50))
        
        self.subjectVert = QtWidgets.QVBoxLayout(self.widget1)
        self.subjectVert.setContentsMargins(0, 0, 0, 0)
        
        self.subjectL = QtWidgets.QLabel(self.widget1)
        self.subjectL.setText("Subject")
        
        self.subjectVert.addWidget(self.subjectL)
        self.subjectLine = QtWidgets.QLineEdit(self.widget1)
        self.subjectLine.setStyleSheet("background-color: #080117;")
        
        self.subjectVert.addWidget(self.subjectLine)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 180, 371, 217))
        
        self.bodyVert = QtWidgets.QVBoxLayout(self.widget2)
        self.bodyVert.setContentsMargins(0, 0, 0, 0)
        
        self.bodyLabel = QtWidgets.QLabel(self.widget2)
        self.bodyLabel.setText("Body")
        
        self.bodyVert.addWidget(self.bodyLabel)
        self.bodyText = QtWidgets.QTextEdit(self.widget2)
        self.bodyText.setStyleSheet("background-color: #080117;")
        
        self.bodyVert.addWidget(self.bodyText)
        
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 22))
        
        
        
        
        
        

        self.enter.clicked.connect(self.close_input)
        
        

    @QtCore.Slot()    
    def close_input(self):
        email = self.emailLine.text()
        subject = self.subjectLine.text()
        body = self.bodyText.toPlainText()

        print("Email: ", email)
        print("Subject: ", subject)
        print("Body:\n", body)

        try:
            ezgmail.send('boomchingshaka@gmail.com', f'{subject}', f'{body}', Fetch.Name(), bcc=email)
            self.close()
            ShareWindow.close_input.success = 1
            self.widget = PopUp()
            self.widget.resize(400,150)
            self.widget.show()
            print("Shared through mail!")

        except:
            print("Fail")
            ShareWindow.close_input.success = 0

class PopUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        print("Message: The email was sent!")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet("background-color: #080117;")
        self.setWindowTitle("Congratulations!")
        self.toastLabel = QLabel(self)
        if ShareWindow.close_input.success == 1:
            self.toastLabel.setText("The email was sent!")
        self.toastLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.toastLabel) 