import sys
import Fetch
import os
import ezgmail

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox
from PySide6.QtGui import QPixmap

cdPath = '/home/shrisharanyan/The_Martian_Chronicles/'
path = '/home/shrisharanyan/The_Martian_Chronicles/marsImages/'
imgList = os.listdir(path)
print(imgList)

from shareWindow import ShareWindow
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
        self.prev.close()
        self.fetch.setEnabled(True)
        

        imgList = os.listdir(path)

        for i in range(len(Fetch.Name())):
            MyWidget.magic.name = Fetch.Name()

            self.label = QLabel(self)
            Width = MyWidget.parameter.imgwidth
            Height = MyWidget.parameter.imgheight
            if i%2==0:
                self.label.move(60,60+int(Height*i))
            if i%2 != 0:
                self.label.move(500,60+int((Height)*(i-1)))
            
            

            self.label.resize(Width,Height)

            if len(imgList) > 0:
                pixmap = QPixmap(os.path.join(path, Fetch.Name()[i]))
                self.label.setPixmap(pixmap)
                self.label.show()
                print("Image embedded in Window..")

                # print("Try Again Later...")

        
        
    @QtCore.Slot()

    def inputBox(self):
        # self.widget = FetchWindow()
        # self.widget.resize(550,550)
        # self.widget.show()
        
        self.parameter()
        self.fetch.setEnabled(False)


    @QtCore.Slot()
    def parameter(self):
       
        print("Recieved Parameters")

        MyWidget.parameter.imgwidth = 350
        MyWidget.parameter.imgheight = 350

        # sol = FetchWindow.useParam.sol
        # roverName = FetchWindow.useParam.roverName
        # earthDate = FetchWindow.useParam.earthDate
        # cameraName = FetchWindow.useParam.cameraName

        Fetch.Image()
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


# class FetchWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.setWindowTitle("Fetch")
        
#         self.getParam()

#     @QtCore.Slot()
#     def getParam(self):

#         self.sol = QLineEdit(self)
#         self.layout.addWidget(self.sol)

#         self.roverName = QLineEdit(self)
#         self.layout.addWidget(self.roverName)

#         self.earthDate = QLineEdit(self)
#         self.layout.addWidget(self.earthDate)

#         self.cameraName = QLineEdit(self)
#         self.layout.addWidget(self.cameraName)

#         self.enter = QtWidgets.QPushButton("Enter")
#         self.layout.addWidget(self.enter, alignment=QtCore.Qt.AlignBottom)
#         self.enter.clicked.connect(self.useParam)
    
#     @QtCore.Slot()
#     def useParam(self):
#         if self.sol.text() != '':
#             FetchWindow.useParam.sol = self.sol.text()
#         if self.roverName.text() != '':
#             FetchWindow.useParam.roverName = self.roverName.text()
#         if self.earthDate.text() != '':
#             FetchWindow.useParam.earthDate = self.earthDate.text()
#         if self.cameraName.text() != '':
#             FetchWindow.useParam.cameraName = self.cameraName.text()


# class PopUp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Toast!")
#         self.layout = QtWidgets.QVBoxLayout(self)
#     def toast(self):
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.label = QLabel(self)
#         # self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setText("The emails were sent! Cheers!! :) ")
#     def alert(self):
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.label = QLabel(self)
#         self.label.setText("Download the image using the fetch button first!!")


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