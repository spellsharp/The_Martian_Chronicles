import sys
import Fetch
import os

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox, QApplication
from PySide6.QtGui import QPixmap, QMovie
import time
cdPath = '/home/shrisharanyan/The_Martian_Chronicles/'
path = '/home/shrisharanyan/The_Martian_Chronicles/marsImages/'
imgList = os.listdir(path)

from shareWindow import ShareWindow

class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        

        self.prev = QLabel(self)
        self.prev.resize(1000, 800)
        pixmap = QPixmap(os.path.join(cdPath,'NASALogo.png'))
        self.prev.setScaledContents(True)
        self.pixmap = pixmap.scaled(self.width(), self.height())
        self.prev.setPixmap(self.pixmap)
        self.prev.setMinimumSize(1,1)
        # self.setCentralWidget(self.prev)
        
        self.setStyleSheet("background-color: #080117;")
        self.setWindowTitle("Mars Rover Image")
        self.layout = QtWidgets.QHBoxLayout(self)

        self.help = QtWidgets.QPushButton("Help")
        self.layout.addWidget(self.help, alignment=QtCore.Qt.AlignBottom)
        self.help.clicked.connect(self.Help)

        self.home = QtWidgets.QPushButton("Home")
        self.layout.addWidget(self.home, alignment=QtCore.Qt.AlignBottom)
        self.home.clicked.connect(self.homeScreen)

        self.fetch = QtWidgets.QPushButton("Fetch - Display")
        self.layout.addWidget(self.fetch, alignment=QtCore.Qt.AlignBottom)
        self.fetch.clicked.connect(self.inputBox)

    @QtCore.Slot()
    def Help(self):
        self.demoWidget = DemoWindow()
        self.demoWidget.resize(300,200)
        self.demoWidget.show()

    @QtCore.Slot()
    def magic(self):
        # self.movie.stop()
        self.prev.close()
        self.fetch.setEnabled(True)
        

        imgList = os.listdir(path)

        for i in range(len(Fetch.Name())):
            if i == 4:
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
            self.demoWidget.close()
        except:
            pass

        try: 
            self.widget = MyWidget()
            self.widget.resize(1000,1020)
            self.widget.show()
            self.close()
        except:
            print("Home screen error")
        
        
    @QtCore.Slot()
    def inputBox(self):
        self.help.close()
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
        # self.label = QLabel(self)
        # self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        # self.label.setMinimumSize(QtCore.QSize(250, 250))
        # self.label.setMaximumSize(QtCore.QSize(250, 250))

        # self.movie = QMovie("Loading.gif")
        # self.label.setMovie(self.movie)
        # self.movie.start()

        sol = self.sol.text()
        earthdate = self.earthdate.text()
        rover = self.rover.currentText().lower()
        camera = self.camera.currentText().lower()

        

        #default or example parameters
        if sol == 'sol' or '':
            print()
            print("Using default sol parameter: 1000")
            sol = '1000'
        if earthdate == '<yyyy-m-d>' or '':
            print()
            print("Using default earthDate parameter: 2015-6-3")
            earthdate =  '2015-6-3'
        if rover == 'choose rover':
            print()
            print("Using default roverName parameter: curiosity")
            rover = 'curiosity'
        if camera == 'choose camera':
            print()
            print("Using default cameraName parameter: fhaz")
            camera = 'fhaz'

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

class DemoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo")
        self.setStyleSheet("background-color: #080117;")
        self.demo = QLabel(self)
        self.demLayout = QtWidgets.QHBoxLayout(self)
        self.demo.setText("""Click the 'Fetch-Display' button.

If you wish for built-in parameters to be taken 
then click 'Enter' directly without altering the values.

You may choose to enter your own parameters 
and then click 'Enter' button, in which case, 
your entered parameters will be considered.

After the images are displayed, click 'Share'
to send these images as attachments to whoever you want.
You can edit the subject and body of the mail if you wish.

Click 'Home' if you want to restart the app.""")
        self.demo.adjustSize()
        self.demLayout.addWidget(self.demo)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(1000,1020)
    widget.show()

    sys.exit(app.exec())