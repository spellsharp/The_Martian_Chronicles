import sys
import Fetch
import os
import ezgmail
import re
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit
from PySide6.QtGui import QPixmap

cdPath = '/home/shrisharanyan/NasaDesktopApp/'
path = '/home/shrisharanyan/NasaDesktopApp/marsImages/'
imgList = os.listdir(path)
print(imgList)



class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: #080117;")
        self.setWindowTitle("Mars Rover Image")
        self.layout = QtWidgets.QHBoxLayout(self)

        self.fetch = QtWidgets.QPushButton("Fetch - Display")
        self.layout.addWidget(self.fetch, alignment=QtCore.Qt.AlignBottom)
        self.fetch.clicked.connect(self.inputBox)

        self.send = QtWidgets.QPushButton("Share")
        self.layout.addWidget(self.send, alignment=QtCore.Qt.AlignBottom)
        self.send.clicked.connect(self.send_mail)


        self.prev = QLabel(self)
        self.prev.resize(1000, 800)
        pixmap = QPixmap(os.path.join(cdPath,'NASAbg.jpg'))
        self.pixmap = pixmap.scaled(self.width(), self.height())
        self.prev.setAlignment(QtCore.Qt.AlignCenter)
        self.prev.setPixmap(self.pixmap)
        self.prev.setMinimumSize(1,1)
        

    @QtCore.Slot()
    def magic(self):
        self.fetch.setEnabled(True)
        MyWidget.magic.name = Fetch.Name()

        imgList = os.listdir(path)
        self.label = QLabel(self)
        self.label.move(40,50)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.resize(900,900)

        if len(imgList) > 0:
            try:
                pixmap = QPixmap(os.path.join(path,Fetch.Name()))
                self.label.setPixmap(pixmap)
                self.label.show()
                print("Image embedded in Window..")
            except:
                print("Try Again Later...")

        
        
    @QtCore.Slot()

    def inputBox(self):

        self.width = QLineEdit(self)
        self.width.setStyleSheet("QLineEdit {background-color: #4F4D53}")
        self.layout.addWidget(self.width, alignment=QtCore.Qt.AlignBottom)
        self.height = QLineEdit(self)
        self.height.setStyleSheet("QLineEdit {background-color: #4F4D53}")
        self.layout.addWidget(self.height, alignment=QtCore.Qt.AlignBottom)

        self.enter = QtWidgets.QPushButton("Enter")
        self.layout.addWidget(self.enter, alignment=QtCore.Qt.AlignBottom)
        self.enter.clicked.connect(self.parameter)

        self.closeText = QtWidgets.QPushButton("Close")
        self.layout.addWidget(self.closeText, alignment=QtCore.Qt.AlignBottom)
        self.closeText.clicked.connect(self.closeFunc)

        self.fetch.setEnabled(False)


    @QtCore.Slot()
    def parameter(self):
        
        global imgwidth
        global imgheight
        print("Recieved Parameters")
        imgwidth = int(self.width.text())
        imgheight = int(self.height.text())
        self.width.close()
        self.height.close()
        self.enter.close()
        self.closeText.close()
        Fetch.Image(imgwidth,imgheight)
        self.magic()

    @QtCore.Slot()
    def closeFunc(self):
        self.width.close()
        self.height.close()
        self.enter.close()
        self.closeText.close()
        self.fetch.setEnabled(True)
        

    @QtCore.Slot()
    def send_mail(self):
        self.widget = ShareWindow()
        self.widget.resize(500, 500)
        self.widget.show()

        
    

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
        ezgmail.send('boomchingshaka@gmail.com', f'{subject}', f'{body}',[os.path.join(path,f'{MyWidget.magic.name}')],cc=email)
        # except AttributeError:
        #     self.alert = PopUp.alert(self)
        #     self.alert.show()
        #     # I WANT TO ADD AN ALERT TELLING THE USER TO FETCH THE IMAGES FIRST.

        # self.toast = PopUp.toast(self)
        # self.toast.show()
        print("Shared through mail!")
        
        self.close()       

class PopUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toast!")
        self.layout = QtWidgets.QVBoxLayout(self)
    def toast(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QLabel(self)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("The emails were sent! Cheers!! :) ")
    def alert(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText("Download the image using the fetch button first!!")


stylesheet = """
    MyWidget {
        background-image: url(home/shrisharanyan/NasaDesktopApp/NASAbg.jpg); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    widget = MyWidget()
    widget.resize(1000,1020)
    widget.show()

    sys.exit(app.exec())