import sys
import Fetch
import os
import ezgmail

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit
from PySide6.QtGui import QPixmap

cdPath = '/home/shrisharanyan/The_Martian_Chronicles/'
path = '/home/shrisharanyan/The_Martian_Chronicles/marsImages/'
imgList = os.listdir(path)

class ShareWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.setWindowTitle("Share")

        self.emailLabel = QLabel(self)
        self.subjectLabel = QLabel(self)
        self.bodyLabel = QLabel(self)

        self.emailLabel.setText("Email Ids: ")
        self.emailLabel.move(15,70)
        self.email = QLineEdit(self)
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.email, alignment=QtCore.Qt.AlignBottom)
        
        self.subjectLabel.setText("Subject: ")
        self.subjectLabel.move(15,180)
        self.subject = QLineEdit(self)
        self.subject.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.subject, alignment=QtCore.Qt.AlignBottom)

        self.bodyLabel.setText("Body: ")
        self.bodyLabel.move(15,300)
        self.body = QLineEdit(self)
        self.body.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.body, alignment=QtCore.Qt.AlignBottom)     
        
        self.enter = QtWidgets.QPushButton("Enter")
        self.layout.addWidget(self.enter, alignment=QtCore.Qt.AlignBottom)
        self.enter.clicked.connect(self.close_input)

    @QtCore.Slot()    
    def close_input(self):
        email = self.email.text()
        subject = self.subject.text()
        body = self.body.text()

        print("Email: ", email)
        print("Subject: ", subject)
        print("Body: ", body)

        # try:
        ezgmail.send('boomchingshaka@gmail.com', f'{subject}', f'{body}', Fetch.Name(), bcc=email)
        # except AttributeError:
        #     self.alert = PopUp.alert(self)
        #     self.alert.show()
        #     # I WANT TO ADD AN ALERT TELLING THE USER TO FETCH THE IMAGES FIRST.

        # self.toast = PopUp.toast(self)
        # self.toast.show()
        print("Shared through mail!")
        
        self.close()       