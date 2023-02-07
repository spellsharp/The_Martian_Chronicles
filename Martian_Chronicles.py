import sys
import Fetch
import os

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox, QApplication
from PySide6.QtGui import QPixmap

cdPath = '/home/shrisharanyan/The_Martian_Chronicles/'
path = '/home/shrisharanyan/The_Martian_Chronicles/marsImages/'
imgList = os.listdir(path)

from shareWindow import ShareWindow

class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        

        self.setStyleSheet("background-color: #080117;")
        self.setWindowTitle("Mars Rover Image")
        self.layout = QtWidgets.QHBoxLayout(self)

        self.home = QtWidgets.QPushButton("Home")
        self.layout.addWidget(self.home, alignment=QtCore.Qt.AlignBottom)
        self.home.clicked.connect(self.homeScreen)

        self.fetch = QtWidgets.QPushButton("Fetch - Display")
        self.layout.addWidget(self.fetch, alignment=QtCore.Qt.AlignBottom)
        self.fetch.clicked.connect(self.inputBox)

        self.prev = QLabel(self)
        self.prev.resize(1000, 800)
        pixmap = QPixmap(os.path.join(cdPath,'NASALogo.png'))
        self.prev.setScaledContents(True)
        
        self.pixmap = pixmap.scaled(self.width(), self.height())
        
        self.prev.setPixmap(self.pixmap)
        self.prev.setMinimumSize(1,1)
        

    @QtCore.Slot()
    def magic(self):
        self.prev.close()
        self.fetch.setEnabled(True)
        

        imgList = os.listdir(path)

        for i in range(len(Fetch.Name())):
            if i >= 4:
                break
            MyWidget.magic.name = Fetch.Name()

            self.label = QLabel(self)
            
            Width = MyWidget.parameter.imgwidth
            Height = MyWidget.parameter.imgheight
            if i%2==0:
                self.label.move(60,60+int(Height*i*0.75))
            if i%2 != 0:
                self.label.move(500,60+int((Height)*(i-1)))

            

            self.label.resize(Width,Height)

            if len(imgList) > 0:
                pixmap = QPixmap(os.path.join(path, Fetch.Name()[i]))
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(True)
                self.label.show()
                print("Image embedded in Window..")
                
                
    
    @QtCore.Slot()
    def homeScreen(self):
        try: 
            self.widget = MyWidget()
            self.widget.resize(1000,1020)
            self.widget.show()
            self.close()
        except:
            print("Home screen error")
        
        
    @QtCore.Slot()
    def inputBox(self):
        global rover
        global sol
        global camera
        global earthdate
        
        self.sol = QLineEdit(self)
        self.earthdate = QLineEdit(self)
        self.sol.setText("sol")
        self.earthdate.setText("<yyyy-m-d>")
        self.layout.addWidget(self.sol, alignment=QtCore.Qt.AlignBottom)
        self.sol.setStyleSheet("background-color: #060111")
        self.earthdate.setStyleSheet("background-color: #060111")
        self.layout.addWidget(self.earthdate, alignment=QtCore.Qt.AlignBottom)

        self.rover = QComboBox(self)
        self.layout.addWidget(self.rover, alignment=QtCore.Qt.AlignBottom)
        self.rover.addItem("Choose Rover")
        self.rover.addItem("Curiosity")
        self.rover.addItem("Opportunity")
        self.rover.addItem("Spirit")

        self.camera = QComboBox(self)
        self.layout.addWidget(self.camera, alignment=QtCore.Qt.AlignBottom)
        self.camera.addItem("Choose Camera")
        self.camera.addItem("FHAZ")
        self.camera.addItem("RHAZ")
        self.camera.addItem("MAST")
        self.camera.addItem("CHEMCAM")
        self.camera.addItem("MAHLI")
        self.camera.addItem("MARDI")
        self.camera.addItem("NAVCAM")
        self.camera.addItem("PANCAM")
        self.camera.addItem("MINITES")
    

        self.enter = QtWidgets.QPushButton("Enter")
        self.layout.addWidget(self.enter, alignment=QtCore.Qt.AlignBottom)
        self.enter.clicked.connect(self.parameter)


        self.fetch.setEnabled(False)


    @QtCore.Slot()
    def parameter(self):
        sol = self.sol.text()
        earthdate = self.earthdate.text()
        rover = self.rover.currentText().lower()
        camera = self.camera.currentText().lower()
        
        print()
        print("Recieved Parameters")
        print(rover)
        print(sol)
        print(camera)
        print(earthdate)

        self.sol.close()
        self.earthdate.close()
        self.rover.close()
        self.camera.close()
        self.enter.close()

        print()

        MyWidget.parameter.imgwidth = 350
        MyWidget.parameter.imgheight = 350

        Fetch.Image(rover, sol, camera, earthdate)

        self.send = QtWidgets.QPushButton("Share")
        self.layout.addWidget(self.send, alignment=QtCore.Qt.AlignBottom)
        self.send.clicked.connect(self.send_mail)

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
        self.send.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(1000,1020)
    widget.show()

    sys.exit(app.exec())