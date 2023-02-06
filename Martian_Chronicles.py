import sys
import Fetch
import os

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
        self.widget = FetchWindow()
        self.widget.resize(550,550)
        self.widget.show()
        
        self.parameter()
        self.fetch.setEnabled(False)


    @QtCore.Slot()
    def parameter(self):
       
        print("Recieved Parameters")

        MyWidget.parameter.imgwidth = 350
        MyWidget.parameter.imgheight = 350
        rover = FetchWindow.input.rover
        sol = FetchWindow.input.sol
        camera = FetchWindow.input.camera
        date = FetchWindow.input.earthdate
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


class FetchWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(370, 437)
        self.setStyleSheet("background-color: rgb(13, 2, 30);")
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        self.enterButton = QtWidgets.QPushButton(self)
        self.enterButton.setGeometry(QtCore.QRect(10, 360, 141, 25))
        self.enterButton.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.enterButton.setObjectName("enterButton")
        self.enterButton.clicked.connect(self.input)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 10, 271, 52))
        self.widget.setObjectName("widget")
        self.RoverVert = QtWidgets.QVBoxLayout(self.widget)
        self.RoverVert.setContentsMargins(0, 0, 0, 0)
        self.RoverVert.setObjectName("RoverVert")
        self.roverVert = QtWidgets.QVBoxLayout()
        self.roverVert.setObjectName("roverVert")
        self.rover = QtWidgets.QLabel(self.widget)
        self.rover.setStyleSheet("background-color: rgb(13, 2, 30);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.rover.setScaledContents(True)
        self.rover.setWordWrap(False)
        self.rover.setObjectName("rover")
        self.roverVert.addWidget(self.rover)
        self.RoverVert.addLayout(self.roverVert)
        self.roverCombo = QtWidgets.QComboBox(self.widget)
        self.roverCombo.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.roverCombo.setObjectName("roverCombo")
        self.roverCombo.addItem("")
        self.roverCombo.addItem("")
        self.roverCombo.addItem("")
        self.roverCombo.addItem("")
        self.RoverVert.addWidget(self.roverCombo)
        self.widget1 = QtWidgets.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(10, 280, 271, 54))
        self.widget1.setObjectName("widget1")
        self.EarthVert = QtWidgets.QVBoxLayout(self.widget1)
        self.EarthVert.setContentsMargins(0, 0, 0, 0)
        self.EarthVert.setObjectName("EarthVert")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.earthVert = QtWidgets.QVBoxLayout()
        self.earthVert.setObjectName("earthVert")
        self.earthdate = QtWidgets.QLabel(self.widget1)
        self.earthdate.setStyleSheet("background-color: rgb(13, 2, 30);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.earthdate.setScaledContents(True)
        self.earthdate.setWordWrap(False)
        self.earthdate.setObjectName("earthdate")
        self.earthVert.addWidget(self.earthdate)
        self.verticalLayout.addLayout(self.earthVert)
        self.EarthVert.addLayout(self.verticalLayout)
        self.earthdateLine = QtWidgets.QLineEdit(self.widget1)
        self.earthdateLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.earthdateLine.setObjectName("earthdateLine")
        self.EarthVert.addWidget(self.earthdateLine)
        self.widget2 = QtWidgets.QWidget(self)
        self.widget2.setGeometry(QtCore.QRect(10, 180, 271, 61))
        self.widget2.setObjectName("widget2")
        self.SolVert = QtWidgets.QVBoxLayout(self.widget2)
        self.SolVert.setContentsMargins(0, 0, 0, 0)
        self.SolVert.setObjectName("SolVert")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sol = QtWidgets.QLabel(self.widget2)
        self.sol.setStyleSheet("background-color: rgb(13, 2, 30);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.sol.setScaledContents(True)
        self.sol.setWordWrap(False)
        self.sol.setObjectName("sol")
        self.verticalLayout_3.addWidget(self.sol)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.SolVert.addLayout(self.verticalLayout_6)
        self.solLine = QtWidgets.QLineEdit(self.widget2)
        self.solLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.solLine.setObjectName("solLine")
        self.SolVert.addWidget(self.solLine)
        self.widget3 = QtWidgets.QWidget(self)
        self.widget3.setGeometry(QtCore.QRect(10, 90, 271, 58))
        self.widget3.setObjectName("widget3")
        self.CameraVert = QtWidgets.QVBoxLayout(self.widget3)
        self.CameraVert.setContentsMargins(0, 0, 0, 0)
        self.CameraVert.setObjectName("CameraVert")
        self.cameraVert = QtWidgets.QVBoxLayout()
        self.cameraVert.setObjectName("cameraVert")
        self.CameraVert.addLayout(self.cameraVert)
        self.camera = QtWidgets.QLabel(self.widget3)
        self.camera.setStyleSheet("background-color: rgb(13, 2, 30);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.camera.setScaledContents(True)
        self.camera.setWordWrap(False)
        self.camera.setObjectName("camera")
        self.CameraVert.addWidget(self.camera)
        self.cameraCombo = QtWidgets.QComboBox(self.widget3)
        self.cameraCombo.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.cameraCombo.setObjectName("cameraCombo")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.cameraCombo.addItem("")
        self.CameraVert.addWidget(self.cameraCombo)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    @QtCore.Slot()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        self.rover.setText(_translate("MainWindow", "Rover Name"))
        self.roverCombo.setItemText(0, _translate("MainWindow", "Choose Rover"))
        self.roverCombo.setItemText(1, _translate("MainWindow", "Curiosity"))
        self.roverCombo.setItemText(2, _translate("MainWindow", "Opportunity"))
        self.roverCombo.setItemText(3, _translate("MainWindow", "Spirit"))
        self.earthdate.setText(_translate("MainWindow", "Earth Date (yyyy-mm-dd)"))
        self.sol.setText(_translate("MainWindow", "Sol"))
        self.camera.setText(_translate("MainWindow", "Camera Name"))
        self.cameraCombo.setItemText(0, _translate("MainWindow", "Choose Camera"))
        self.cameraCombo.setItemText(1, _translate("MainWindow", "FHAZ"))
        self.cameraCombo.setItemText(2, _translate("MainWindow", "RHAZ"))
        self.cameraCombo.setItemText(3, _translate("MainWindow", "MAST"))
        self.cameraCombo.setItemText(4, _translate("MainWindow", "CHEMCAM"))
        self.cameraCombo.setItemText(5, _translate("MainWindow", "MAHLI"))
        self.cameraCombo.setItemText(6, _translate("MainWindow", "MARDI"))
        self.cameraCombo.setItemText(7, _translate("MainWindow", "NAVCAM"))
        self.cameraCombo.setItemText(8, _translate("MainWindow", "PANCAM"))
        self.cameraCombo.setItemText(9, _translate("MainWindow", "MINITES"))

    @QtCore.Slot()
    def input(self):
        FetchWindow.input.rover = self.roverCombo.currentText().lower()
        FetchWindow.input.camera = self.cameraCombo.currentText().lower()
        FetchWindow.input.sol = self.solLine.text()
        FetchWindow.input.earthdate = self.earthdateLine.text()
        print(FetchWindow.input.rover)
        print(FetchWindow.input.camera)
        print(FetchWindow.input.sol)
        print(FetchWindow.input.earthdate)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(1000,1020)
    widget.show()

    sys.exit(app.exec())