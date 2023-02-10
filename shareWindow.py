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
"background-color: #0D0D0D;")

        self.centralwidget = QtWidgets.QWidget(self)

        self.enter = QtWidgets.QPushButton(self)
        self.enter.setText("Enter")
        self.enter.setStyleSheet("background-color: #191919; border : 2px solid #DD4E00; border-radius : 4px;")
        self.enter.setGeometry(QtCore.QRect(200, 425, 89, 25))

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 361, 50))
        
        self.emailVert = QtWidgets.QVBoxLayout(self.widget)
        self.emailVert.setContentsMargins(0, 0, 0, 0)
        
        self.emailLabel = QtWidgets.QLabel(self.widget)
        self.emailLabel.setText("Email Id(s)")
        self.emailVert.addWidget(self.emailLabel)
        self.emailLine = QtWidgets.QLineEdit(self.widget)
        self.emailLine.setStyleSheet("background-color: #191919; border : 2px solid #DD4E00; border-radius : 4px;")

        self.emailVert.addWidget(self.emailLine)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 100, 361, 50))

        
        self.subjectVert = QtWidgets.QVBoxLayout(self.widget1)
        self.subjectVert.setContentsMargins(0, 0, 0, 0)
        
        
        self.subjectL = QtWidgets.QLabel(self.widget1)
        self.subjectL.setText("Subject")
        
        self.subjectVert.addWidget(self.subjectL)
        self.subjectLine = QtWidgets.QLineEdit(self.widget1)
        self.subjectLine.setStyleSheet("background-color: #191919; border : 2px solid #DD4E00; border-radius : 4px;")
        
        self.subjectVert.addWidget(self.subjectLine)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 180, 371, 217))
        
        self.bodyVert = QtWidgets.QVBoxLayout(self.widget2)
        self.bodyVert.setContentsMargins(0, 0, 0, 0)
        
        self.bodyLabel = QtWidgets.QLabel(self.widget2)
        self.bodyLabel.setText("Body")
        
        self.bodyVert.addWidget(self.bodyLabel)
        self.bodyText = QtWidgets.QTextEdit(self.widget2)
        self.bodyText.setStyleSheet("background-color: #191919; border : 2px solid #DD4E00; border-radius : 4px;")
        
        self.bodyVert.addWidget(self.bodyText)
        
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 22))
        # rover = Fetch.roverName()
        sol = Fetch.Sol()
        # date = Fetch.Date()
        num = Fetch.numbPhotos()
        
        self.subjectLine.setText("Latest Photos - NASA Mars Rover")
        self.bodyText.setText(f"""Latest photos taken by NASA Mars rover, in the Solar Year {sol}, have been sent to you as attachments.

Number of attachments: {num}

Please enjoy!

Regards,
Sharan""")
        
        
        

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
            print("Shared through mail!")
        except:
            ShareWindow.close_input.success = 0

        toastLabel = QtWidgets.QMessageBox(self)
        toastLabel.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if ShareWindow.close_input.success == 1:
            toastLabel.setWindowTitle("Congratulations!")
            toastLabel.setText("The email was sent!")
            toastLabel.setIcon(QtWidgets.QMessageBox.Information)
            toastLabel.exec_()
            
        else:
            toastLabel.setWindowTitle("Error!")
            toastLabel.setText("""Email could not be sent.
Enter correct parameters or Try again later""")
            toastLabel.setIcon(QtWidgets.QMessageBox.Warning)
            toastLabel.exec_()
        