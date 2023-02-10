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

#Passing the address of Fetch.Name() to Name. Accessing the same list.
Name = Fetch.Name()

class MyWidget(QtWidgets.QWidget):
    global imgNum
    imgNum = 0

    def __init__(self):
        super().__init__()
        

        self.prev = QLabel(self)
        self.prev.resize(1000, 800)
        pixmap = QPixmap(os.path.join(cdPath,'NASALogo.png'))
        # self.prev.setScaledContents(True)
        self.prev.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = pixmap.scaled(self.width(), self.height())
        self.prev.setPixmap(self.pixmap)
        self.prev.setMinimumSize(1,1)
        
        self.setStyleSheet("background-color: #080117;")
        self.setWindowTitle("NASA - Mars Rover Images")
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
    

        MyWidget.magic.name = Name

        self.label = QLabel(self)
        
        Width = MyWidget.parameter.imgwidth
        Height = MyWidget.parameter.imgheight
        try:
            pixmap = QPixmap(os.path.join(path, Name[0]))
            self.label.setPixmap(pixmap)
            self.label.move(25,25)
            self.label.resize(850,850)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.show()
            self.num.setText(f"{imgNum+1}/{len(Name)}")
            self.setWindowTitle("Image(s)")
        except IndexError:
            #print("No Images found for given parameters.")
            self.prev.show()
            self.homeScreen()
                
                
    
    @QtCore.Slot()
    def homeScreen(self):
        try:
            self.demoWidget.close()
        except:
            pass

        try:
            Name.clear()
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
        global imgNum
        imgNum = 0
        try:
            Name.clear()
        except:
            pass

        try:
            self.next.close()
            self.pre.close()
            self.num.close()
            self.send.close()
        except:
            pass

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

        self.pre = QtWidgets.QPushButton("Previous")
        self.layout.addWidget(self.pre, alignment=QtCore.Qt.AlignBottom)
        self.pre.clicked.connect(self.prevImg)

        self.num = QLabel(self)
        self.layout.addWidget(self.num, alignment=QtCore.Qt.AlignBottom)
        # self.num.resize(10,25)
        self.next = QtWidgets.QPushButton("Next")
        self.layout.addWidget(self.next, alignment=QtCore.Qt.AlignBottom)
        self.next.clicked.connect(self.nextImg)
        
        sol = self.sol.text()
        earthdate = self.earthdate.text()
        rover = self.rover.currentText().lower()
        camera = self.camera.currentText().lower()

        defaultRover = ''
        defaultSol = ''
        defaultCamera = ''
        defaultEarth = ''

        #default or example parameters
        if sol == 'sol' or '':
            defaultSol = ' (default)'
            sol = '1000'
        if earthdate == '<yyyy-m-d>' or '':
            defaultEarth = ' (default)'
            earthdate =  '2015-6-3'
        if rover == 'choose rover':
            defaultRover = ' (default)'
            rover = 'curiosity'
        if camera == 'choose camera':
            defaultCamera = ' (default)'
            camera = 'fhaz'

        

        print()
        print("---------------------------------------")
        print("RECEIVED PARAMETERS")
        print("---------------------------------------")
        print("Rover Name" + ": ".rjust(3), rover.rjust(12) + defaultRover)
        print("Sol" + ": ".rjust(10), sol.rjust(12) + defaultSol)
        print("Camera Name: ", camera.rjust(12) + defaultCamera)
        print("Earth date"+": ".rjust(3), earthdate.rjust(12) + defaultEarth)
        print("---------------------------------------")

        self.sol.close()
        self.earthdate.close()
        self.rover.close()
        self.camera.close()
        self.enter.close()

        print()

        MyWidget.parameter.imgwidth = 500
        MyWidget.parameter.imgheight = 500

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

    def nextImg(self):
        self.pre.setEnabled(True)
        global imgNum

        if imgNum < len(Name) - 1:
            imgNum += 1
            if imgNum == len(Name) - 1:
                self.next.setEnabled(False)

        self.num.setText(f"{imgNum+1}/{len(Name)}")
        
        
        pixmap = QPixmap(os.path.join(path, Name[imgNum]))

        self.setWindowTitle("Image(s)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(pixmap)
        self.label.resize(850,850)
        self.label.show()

    def prevImg(self):
        global imgNum
        self.next.setEnabled(True)
        

        if imgNum > 0:
            imgNum -= 1
            if imgNum == 0:
                self.pre.setEnabled(False)

        self.num.setText(f"{imgNum+1}/{len(Name)}")
       
        self.setWindowTitle("Image(s)") 
        pixmap = QPixmap(os.path.join(path, Name[imgNum]))
        self.label.setPixmap(pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.resize(850,850)
        self.label.show()



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
