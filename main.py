# Modified by Augmented Startups & Geeky Bee
# October 2020
# Facial Recognition Attendence GUI
# Full Course - https://augmentedstartups.info/yolov4release
# *-
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QFileDialog, QMessageBox, QLabel
from PyQt5.uic.properties import QtCore
import PyQt5
#import resource
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QWidget
from PyQt5 import QtCore
import pyrebase
import hashlib
from fpdf import FPDF
# from model import Model
#from out_window import Ui_OutputDialog
from PyQt5.QtWidgets import QMessageBox
from out_window import Ui_OutputDialog



class SplashScreen(QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()
        loadUi("splash_screen.ui", self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.center()
        self.btnGetStarted.clicked.connect(self.gotoRole)

        self.dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def gotoRole(self):
        role = Ui_Dialog()
        widget.addWidget(role)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ui.hide()
        self.center()
        widget.resize(1100, 750)
        widget.show()


#End of Splash Screen



class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("chooseRole.ui", self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.btnEmployee.clicked.connect(self.gotoEmployee)
        self.btnAdmin.clicked.connect(self.gotoAdmin)

        self.dragPos = QtCore.QPoint()



    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def gotoAdmin(self):
        adminz = adminScreen()
        widget.addWidget(adminz)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ui.hide()
        self.center()
        widget.resize(1100, 750)
        widget.show()
    def gotoEmployee(self):
        employeetz = employeeScreen()
        widget.addWidget(employeetz)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ui.hide()
        self.center()
        widget.resize(1100, 750)
        widget.show()

class employeeScreen(QDialog):
    def __init__(self):
        super(employeeScreen, self).__init__()
        print("Start")
        loadUi("loginfinal.ui", self)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        self.btnLogin.clicked.connect(self.runSlot)

        self.dragPos = QtCore.QPoint()

        # stylesheet of error popup messages

    styleLineEditOk = ("QLineEdit {\n"
                        "    border: 2px solid rgb(45, 45, 45);\n"
                        "    border-radius: 5px;\n"
                        "    padding: 15px;\n"
                        "    background-color: rgb(255, 255, 255);    \n"
                        "    color: rgb(0, 0, 0);\n"
                        "}\n"
                        "QLineEdit:hover {\n"
                        "    border: 2px solid rgb(55, 55, 55);\n"
                        "}\n"
                        "QLineEdit:focus {\n"
                        "    border: 2px solid rgb(255, 207, 0);    \n"
                        "    color: rgba(27, 29, 35, 200);\n"
                        "}")
    styleLineEditError = ("QLineEdit {\n"
                        "    border: 2px solid rgb(255, 85, 127);\n"
                        "    border-radius: 5px;\n"
                        "    padding: 15px;\n"
                        "    background-color: rgb(255, 255, 255);    \n"
                        "    color: rgb(0, 0, 0);\n"
                        "}\n"
                        "QLineEdit:hover {\n"
                        "    border: 2px solid rgb(55, 55, 55);\n"
                        "}\n"
                        "QLineEdit:focus {\n"
                        "    border: 2px solid rgb(255, 207, 0);    \n"
                        "    color: rgba(27, 29, 35, 200);\n"
                        "}")
    stylePopupError = ("background-color: rgb(255, 85, 127); border-radius: 5px;")
    stylePopupOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")
        # ends of stylesheet error

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        self.Videocapture_ = "0"

    @pyqtSlot()
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abe89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"

        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()
        storage = firebase.storage()

        section = "Accounts"
        folder = "ImagesAttendance"

        inpId = self.lineEditID.text()

        username = database.child(section).child(inpId).child("Username").get()
        password = database.child(section).child(inpId).child("Password").get()
        role = database.child(section).child(inpId).child("Role").get()

        inpName = self.lineEditUsername.text()
        inpPass = self.lineEditPassword.text()

        # Hashing
        inpHashPassword = inpPass.encode("utf8")
        inpHashPassword1 = hashlib.md5(inpHashPassword)
        hexaInpPassword = inpHashPassword1.hexdigest()

        if inpName == username.val() and hexaInpPassword == password.val() and role.val() == "Employee":
            # Download Pic
            fname = database.child(section).child(inpId).child("FirstName").get()
            lname = database.child(section).child(inpId).child("LastName").get()
            path_on_cloud = "Images/" + str(inpId) + "/" + str(fname.val()) + " " + str(lname.val()) + ".jpg"

            storage.child(path_on_cloud).download(folder + "/" + str(fname.val()).upper() + " " + str(lname.val()).upper() + ".jpg")

            #Employee Screen
            self.refreshAll()
            widget.hide()  # hide the main window
            self.outputWindow_()  # Create and open new output window

        else:
            if not self.lineEditID.text():
                inpId = " ID is Empty!"
                self.lineEditID.setStyleSheet(self.styleLineEditError)
            else:
                inpId = ""
                self.lineEditID.setStyleSheet(self.styleLineEditOk)
                # End of ID

                # Check username
            if not self.lineEditUsername.text():
                inpName = " Username is Empty!"
                self.lineEditUsername.setStyleSheet(self.styleLineEditError)
            else:
                inpName = ""
                self.lineEditUsername.setStyleSheet(self.styleLineEditOk)
                # End of username

                # Check Password
            if not self.lineEditPassword.text():
                inpPass = " Password is Empty! "
                self.lineEditPassword.setStyleSheet(self.styleLineEditError)
            else:
                inpPass = ""
                self.lineEditPassword.setStyleSheet(self.styleLineEditOk)
            # end of check password
            invalid = " Invalid Credentials!"
            text = inpId + inpName + inpPass + invalid
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText(text)
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def outputWindow_(self):
        """
        Created new window for vidual output of the video in GUI
        """
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        print("Video Played")

class adminScreen(QDialog):
    def __init__(self):
        super(adminScreen, self).__init__()
        loadUi("loginfinalTest.ui", self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.center()
        self.btnLogin.clicked.connect(self.gotoChoose)

        # BT CLOSE POPUP
        self.pushButton_close_pupup.clicked.connect(lambda: self.frame_error.hide())

        # HIDE ERROR
        self.frame_error.hide()

        # BT LOGIN
        self.dragPos = QtCore.QPoint()


        #stylesheet of error popup messages

    styleLineEditOk = ("QLineEdit {\n"
                       "    border: 2px solid rgb(45, 45, 45);\n"
                       "    border-radius: 5px;\n"
                       "    padding: 15px;\n"
                       "    background-color: rgb(255, 255, 255);    \n"
                       "    color: rgb(0, 0, 0);\n"
                       "}\n"
                       "QLineEdit:hover {\n"
                       "    border: 2px solid rgb(55, 55, 55);\n"
                       "}\n"
                       "QLineEdit:focus {\n"
                       "    border: 2px solid rgb(255, 207, 0);    \n"
                       "    color: rgba(27, 29, 35, 200);\n"
                       "}")
    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    padding: 15px;\n"
                          "    background-color: rgb(255, 255, 255);    \n"
                          "    color: rgb(0, 0, 0);\n"
                          "}\n"
                          "QLineEdit:hover {\n"
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgba(27, 29, 35, 200);\n"
                          "}")
    stylePopupError = ("background-color: rgb(255, 85, 127); border-radius: 5px;")
    stylePopupOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")
        #ends of stylesheet error

    #FUNCTIONS IN THE FIELD
    def gotoChoose(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"

        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        section = "Accounts"

        inpId = self.lineEditID.text()

        username = database.child(section).child(inpId).child("Username").get()
        password = database.child(section).child(inpId).child("Password").get()
        role = database.child(section).child(inpId).child("Role").get()

        inpName = self.lineEditUsername.text()
        inpPass = self.lineEditPassword.text()

        # Hashing
        inpHashPassword = inpPass.encode("utf8")
        inpHashPassword1 = hashlib.md5(inpHashPassword)
        hexaInpPassword = inpHashPassword1.hexdigest()

        if inpName == username.val() and hexaInpPassword == password.val() and role.val() == "Admin":
            choose = chooseAction()
            widget.addWidget(choose)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.center()
            ui.hide()

            self.resize(1800, 800)
            widget.show()

        else:
            if not self.lineEditID.text():
                inpId = " ID is Empty!"
                self.lineEditID.setStyleSheet(self.styleLineEditError)
            else:
                inpId = ""
                self.lineEditID.setStyleSheet(self.styleLineEditOk)
                # End of ID

                # Check username
            if not self.lineEditUsername.text():
                inpName = " Username is Empty!"
                self.lineEditUsername.setStyleSheet(self.styleLineEditError)
            else:
                inpName = ""
                self.lineEditUsername.setStyleSheet(self.styleLineEditOk)
                # End of username

                # Check Password
            if not self.lineEditPassword.text():
                inpPass = " Password is Empty! "
                self.lineEditPassword.setStyleSheet(self.styleLineEditError)
            else:
                inpPass = ""
                self.lineEditPassword.setStyleSheet(self.styleLineEditOk)
            # end of check password
            invalid = " Invalid Credentials!"
            text = inpId + inpName + inpPass + invalid
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText(text)
            msg.setIcon(QMessageBox.Information)
            msg.exec_()


        #END OF CHECK FIELDS
    #END OF FUNCTION IN THE FIELD

    #
    #

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


#CHOOSE ACTION
class chooseAction(QDialog):
    def __init__(self):
        super(chooseAction, self).__init__()
        loadUi("testingChoose.ui", self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        widget.move(550, 200)
        #elf.centerN()

        #self.initUI()
        self.dragPos = QtCore.QPoint()
        #widget.resize(1200, 720)
        self.btnExit.clicked.connect(lambda: widget.close())
        self.btnCrud.clicked.connect(self.gotoHome)
        self.btnViewSeemore.clicked.connect(self.gotoViewGenerate)
    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    #def initUI(self):
        #self.center()
        #self.show()

    #def center(self):
        #qr = self.frameGeometry()
        #cp = QDesktopWidget().availableGeometry().center()
        #qr.moveCenter(cp)
        #self.move(qr.topLeft())

    def gotoHome(self):
        home = createHome()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.move(320, 150)

    def gotoViewGenerate(self):
        report = createReport()
        widget.addWidget(report)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.move(320, 150)
#END OF CHOOSE ACTION

#GENERATE STARTS HERE
class createReport(QMainWindow):
    def __init__(self):
        super(createReport, self).__init__()
        loadUi("testingReport.ui", self)
        widget.resize(1200, 800)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.FramelessWindowHint)
        self.btnMin.clicked.connect(lambda: widget.showMinimized())
        self.btnClose.clicked.connect(lambda: widget.close())
        self.setWindowFlags(flags)
        self.center()
        self.btnBack.clicked.connect(self.goBackChoose)
        self.btnGeneratePDF.clicked.connect(self.goGeneratePDF)
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 125)
        self.btnDisplayData.clicked.connect(self.goDisplayData)

    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    background-color: rgb(30, 30, 30);    \n"
                          "    color: rgb(100, 100, 100);\n"
                          "}\n"
                          "QLineEdit:hover {\n"
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgb(200, 200, 200);\n"
                          "}")

    def goDisplayData(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        attendance = "Attendance"
        date = self.lbl_HomeDate.text()

        if date != "":
            ret1 = database.child(attendance).get()
            checker = 0
            for rets1 in ret1.each():
                if str(rets1.key()) == date:
                    checker = 1
            if checker != 0:
                ret = database.child(attendance).child(date).get()
                row = 0
                item = 0
                for rets in ret.each():
                    people = [rets.val()]
                    item = item + 1
                    self.tableWidget.setRowCount(item)
                    for person in people:
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['Name']))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Time In']))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Time Out']))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Working Hours']))
                        row = row + 1
            else:
                self.lbl_HomeDate.setStyleSheet(self.styleLineEditError)
                msg = QMessageBox()
                msg.setWindowTitle("WARNING!")
                msg.setText("DATE DOES NOT EXIST!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

        else:
            self.lbl_HomeDate.setStyleSheet(self.styleLineEditError)
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText("PLEASE ENTER DATE!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def goGeneratePDF(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        attendance = "Attendance"

        date = self.lbl_HomeDate.text()

        ret = database.child(attendance).child(date).get()
        if date != "":
            ret1 = database.child(attendance).get()
            checker = 0
            for rets1 in ret1.each():
                if str(rets1.key()) == date:
                    checker = 1
            if checker != 0:
                pdf = FPDF('P', 'mm', 'Letter')
                pdf.add_page()
                pdf.set_font("Times", size=12)

                pdf.cell(160, 10, "RAFIE Attendance System")
                pdf.cell(40, 10, "Date: " + date, ln=True)
                pdf.cell(120, 5,
                         "--------------------------------------------------------------------------------------------------------------------------------------",
                         ln=True)
                pdf.cell(5, 8, "|")
                pdf.cell(65, 10, "Name")
                pdf.cell(10, 8, "|")
                pdf.cell(28, 10, "Time In")
                pdf.cell(12, 8, "|")
                pdf.cell(28, 10, "Time Out")
                pdf.cell(5, 8, "|")
                pdf.cell(35, 10, "Working Hours")
                pdf.cell(5, 8, "|", ln=True)
                pdf.cell(120, 5,
                         "--------------------------------------------------------------------------------------------------------------------------------------",
                         ln=True)
                for rets in ret.each():
                    pdf.cell(5, 8, "|")
                    pdf.cell(65, 8, str(rets.val()['Name']))
                    pdf.cell(10, 8, "|")
                    pdf.cell(28, 8, str(rets.val()['Time In']))
                    pdf.cell(12, 8, "|")
                    pdf.cell(28, 8, str(rets.val()['Time Out']))
                    pdf.cell(5, 8, "|")
                    pdf.cell(35, 10, str(rets.val()['Working Hours']))
                    pdf.cell(5, 8, "|", ln=True)
                pdf.cell(120, 5,
                         "--------------------------------------------------------------------------------------------------------------------------------------",
                         ln=True)

                filename = "Reports/" + "Attendance_Report_" + date.replace('|', '-') + ".pdf"
                pdf.output(filename)

                msg = QMessageBox()
                msg.setWindowTitle("MESSAGE!")
                msg.setText("PDF HAS BEEN GENERATED!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

            else:
                self.lbl_HomeDate.setStyleSheet(self.styleLineEditError)
                msg = QMessageBox()
                msg.setWindowTitle("WARNING!")
                msg.setText("DATE DOES NOT EXIST!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
        else:
            self.lbl_HomeDate.setStyleSheet(self.styleLineEditError)
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText("PLEASE ENTER DATE!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    # def popup_btn(self, i):
    # print(i.text())

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def goBackChoose(self):
        backChoose = chooseAction()
        widget.addWidget(backChoose)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#GENERATE ENDS HERE

class createHome(QMainWindow):
    def __init__(self):
        super(createHome, self).__init__()
        loadUi("MainHome.ui", self)
        widget.resize(1200, 800)

        self.btnCreate.clicked.connect(self.gotoCreate)
        self.btnUpdate.clicked.connect(self.gotoUpdate)
        self.btnView.clicked.connect(self.gotoView)
        self.btnDelete.clicked.connect(self.gotoDelete)
        self.btnLogout.clicked.connect(self.logout)
        self.btnBack.clicked.connect(self.goChoose)

        self.btnMin.clicked.connect(lambda: widget.showMinimized())
        self.btnClose.clicked.connect(lambda: widget.close())


    # Function Starts Here Update
    def logout(self):
        awtz = Ui_Dialog()
        widget.addWidget(awtz)
        widget.move(480, 280)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def goChoose(self):
        chuuz = chooseAction()
        widget.addWidget(chuuz)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoCreate(self):
        create = createScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoUpdate(self):
        update = createUpdate()
        widget.addWidget(update)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoView(self):
        view = createView()
        widget.addWidget(view)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoDelete(self):
        delete = createDelete()
        widget.addWidget(delete)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    # Function Ends Here Update

#create USER STARTS HERE
class createScreen(QMainWindow):
    def __init__(self):
        super(createScreen, self).__init__()
        loadUi("testingCreate.ui", self)
        self.btnMin.clicked.connect(lambda: widget.showMinimized())
        self.btnClose.clicked.connect(lambda: widget.close())
        self.btnBack.clicked.connect(self.goBack)
        self.btnCreate.clicked.connect(self.goCreate)
        self.btnUpload.clicked.connect(self.goUpload)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)
        self.loaddata()


    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    background-color: rgb(30, 30, 30);    \n"
                          "    color: rgb(100, 100, 100);\n"
                          "}\n"
                          "QLineEdit:hover {\n"
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgb(200, 200, 200);\n"
                          "}")

    # ends of stylesheet error

    def loaddata(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        ret = database.child(accounts).get()
        row = 0
        item = 0
        for rets in ret.each():
            people = [rets.val()]
            item = item + 1
            self.tableWidget.setRowCount(item)
            for person in people:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                row = row + 1


    def goUpload(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'D:\codefirst.io', 'Images (*.png, *.xmp, *.jpg)')
        self.lblUploadPhoto.setText(fname[0])

    def goCreate(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }
        # Database
        firebase = pyrebase.initialize_app(config)
        database = firebase.database()
        storage = firebase.storage()

        accounts = "Accounts"

        inpId = self.lbl_ID.text()
        inpUsername = self.lbl_Username.text()
        inpPassword = self.lbl_Password.text()
        inpRole = self.comboBox_Role.currentText()
        inpFname = self.lbl_FirstName.text()
        inpLname = self.lbl_LastName.text()
        inpAge = self.lbl_Age.text()
        inpGender = self.comboBox_Gender.currentText()
        inpBirthdate = self.lbl_Birthdate.text()
        inpContact = self.lbl_Contact.text()
        inpCity = self.lbl_City.text()

        ret = database.child("Accounts").get()

        if inpId != "" and inpUsername != "" and inpPassword != "":
            checker = 0
            for rets in ret.each():
                if inpId == rets.val()['ID']:
                    checker = 1
            if checker == 0:
                inpHashPassword = inpPassword.encode("utf8")
                inpHashPassword1 = hashlib.md5(inpHashPassword)
                hexaInpPassword = inpHashPassword1.hexdigest()

                data = {"ID": inpId, "Username": inpUsername, "Password": hexaInpPassword, "Role": inpRole,
                        "FirstName": inpFname, "LastName": inpLname, "Age": inpAge, "Gender": inpGender,
                        "Birthdate": inpBirthdate, "Contact": inpContact, "City": inpCity}
                database.child(accounts).child(inpId).set(data)

                name = inpFname + " " + inpLname
                eId = inpId
                imgPath = self.lblUploadPhoto.text()

                # Browsing
                path_on_cloud = "Images/" + eId + "/" + name + ".jpg"
                path_local = str(imgPath)

                # Uploading
                storage.child(path_on_cloud).put(path_local)

                msg = QMessageBox()
                msg.setWindowTitle("NOTIFICATION!")
                msg.setText("RECORD CREATED")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.loaddata()

                self.lbl_ID.setText("")
                self.lbl_Username.setText("")
                self.lbl_Password.setText("")
                self.lbl_FirstName.setText("")
                self.lbl_LastName.setText("")
                self.lbl_Age.setText("")
                self.lbl_Birthdate.setText("")
                self.lbl_Contact.setText("")
                self.lbl_City.setText("")
            else:
                msg = QMessageBox()
                msg.setWindowTitle("WARNING!")
                msg.setText("EMPLOYEE ID IS ALREADY EXISTED")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
        else:
            self.lbl_ID.setStyleSheet(self.styleLineEditError)
            self.lbl_Username.setStyleSheet(self.styleLineEditError)
            self.lbl_Password.setStyleSheet(self.styleLineEditError)

#GO BACK BUTTON
    def goBack(self):
        back = createHome()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
#GO BACK ENDS HERE
#create USER ENDS HERE

#UPDATE STARTS HERE
class createUpdate(QMainWindow):
    def __init__(self):
        super(createUpdate, self).__init__()
        loadUi("testingUpdate.ui", self)
        self.btnMin.clicked.connect(lambda: widget.showMinimized())
        self.btnClose.clicked.connect(lambda: widget.close())
        self.btnBack.clicked.connect(self.goBackUpdate)
        self.btnUpdate.clicked.connect(self.goUpdate)
        self.btnSearch_ID.clicked.connect(self.goSearch)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)
        self.loaddata()

    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    background-color: rgb(30, 30, 30);    \n"
                          "    color: rgb(100, 100, 100);\n"
                          "}\n"
                          "QLineEdit:hover {\n"
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgb(200, 200, 200);\n"
                          "}")

    def loaddata(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        ret = database.child(accounts).get()
        row = 0
        item = 0
        for rets in ret.each():
            people = [rets.val()]
            item = item + 1
            self.tableWidget.setRowCount(item)
            for person in people:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                row = row + 1

    def goSearch(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        inpId = self.lbl_UpdateID_2.text()

        if inpId != "":
            ret1 = database.child(accounts).get()
            checker = 0
            for rets1 in ret1.each():
                if str(rets1.val()['ID']) == inpId:
                    checker = 1
            if checker != 0:
                fname = database.child("Accounts").child(inpId).child("FirstName").get()
                lname = database.child("Accounts").child(inpId).child("LastName").get()
                age = database.child("Accounts").child(inpId).child("Age").get()
                birthdate = database.child("Accounts").child(inpId).child("Birthdate").get()
                contact = database.child("Accounts").child(inpId).child("Contact").get()
                city = database.child("Accounts").child(inpId).child("City").get()

                self.lbl_UpdateFName.setText(str(fname.val()))
                self.lbl_UpdateLName.setText(str(lname.val()))
                self.lbl_UpdateAge.setText(str(age.val()))
                self.lbl_UpdateBday.setText(str(birthdate.val()))
                self.lbl_UpdateContactNum.setText(str(contact.val()))
                self.lbl_UpdateCity.setText(str(city.val()))

                ret = database.child(accounts).child(inpId).get()
                row = 0
                item = 0
                people = [ret.val()]
                item = item + 1
                self.tableWidget.setRowCount(item)
                for person in people:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                    self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                    self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                    self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                    self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                    row = row + 1
                self.lbl_UpdateID_2.setText("")
            else:
                self.lbl_UpdateID_2.setStyleSheet(self.styleLineEditError)
                msg = QMessageBox()
                msg.setWindowTitle("WARNING!")
                msg.setText("ID DOES NOT EXIST")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

        else:
            self.lbl_UpdateID_2.setStyleSheet(self.styleLineEditError)
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText("PLEASE ENTER ID")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        self.lbl_UpdateID_2.setText("")

    def goUpdate(self):

        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        inpId = self.lbl_UpdateID_2.text()
        inpFname = self.lbl_UpdateFName.text()
        inpLname = self.lbl_UpdateLName.text()
        inpAge = self.lbl_UpdateAge.text()
        inpGender = self.cb_Age.currentText()
        inpBirthdate = self.lbl_UpdateBday.text()
        inpContact = self.lbl_UpdateContactNum.text()
        inpCity = self.lbl_UpdateCity.text()

        if inpId != "":

            ret1 = database.child(accounts).get()
            checker = 0
            for rets1 in ret1.each():
                if str(rets1.val()['ID']) == inpId:
                    checker = 1
            if checker != 0:
                database.child(accounts).child(inpId).update(
                    {"FirstName": inpFname, "LastName": inpLname, "Age": inpAge,
                     "Gender": inpGender, "Birthdate": inpBirthdate, "Contact": inpContact, "City": inpCity})
                msg = QMessageBox()
                msg.setWindowTitle("NOTIFICATION")
                msg.setText("RECORD UPDATED")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.loaddata()
            else:
                self.lbl_UpdateID_2.setStyleSheet(self.styleLineEditError)
                msg = QMessageBox()
                msg.setWindowTitle("WARNING!")
                msg.setText("ID DOES NOT EXIST!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
        else:
            self.lbl_UpdateID_2.setStyleSheet(self.styleLineEditError)
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText("PLEASE ENTER ID")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def goBackUpdate(self):
        backUpdate = createHome()
        widget.addWidget(backUpdate)
        widget.setCurrentIndex(widget.currentIndex() + 1)
#UPDATE ENDS HERE

#VIEW STARTS HERE
class createView(QMainWindow):
    def __init__(self):
        super(createView, self).__init__()
        loadUi("testingView.ui", self)
        self.btnMin.clicked.connect(lambda: widget.showMinimized())
        self.btnClose.clicked.connect(lambda: widget.close())
        self.btnBack.clicked.connect(self.gotoBackView)
        self.btnViewView.clicked.connect(self.goView)
        self.btnViewSearch.clicked.connect(self.goSearch)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)
        self.loaddata()

    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    background-color: rgb(30, 30, 30);    \n"
                          "    color: rgb(100, 100, 100);\n"
                          "}\n"
                          "QLineEdit:hover {\n" 
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgb(200, 200, 200);\n"
                          "}")

    def loaddata(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        ret = database.child(accounts).get()
        row = 0
        item = 0
        for rets in ret.each():
            people = [rets.val()]
            item = item + 1
            self.tableWidget.setRowCount(item)
            for person in people:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                row = row + 1

    def goSearch(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        inpId = self.lbl_ViewID.text()

        if inpId != "":
            ret1 = database.child(accounts).get()
            checker = 0
            for rets1 in ret1.each():
                if str(rets1.val()['ID']) == inpId:
                    checker = 1
            if checker != 0:
                ret = database.child(accounts).child(inpId).get()
                row = 0
                item = 0
                people = [ret.val()]
                item = item + 1
                self.tableWidget.setRowCount(item)
                for person in people:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                    self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                    self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                    self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                    self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                    row = row + 1

                    self.lbl_ViewID.setText("")
            else:
                self.lbl_ViewID.setStyleSheet(self.styleLineEditError)
                msg = QMessageBox()
                msg.setWindowTitle("WARNING!")
                msg.setText("ID DOES NOT EXIST!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
        else:
            self.lbl_ViewID.setStyleSheet(self.styleLineEditError)
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText("PLEASE ENTER ID")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        self.lbl_ViewID.setText("")

    def goView(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        ret = database.child(accounts).get()
        row = 0
        item = 0
        for rets in ret.each():
            people = [rets.val()]
            item = item + 1
            self.tableWidget.setRowCount(item)
            for person in people:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                row = row + 1

    def gotoBackView(self):
        backView = createHome()
        widget.addWidget(backView)
        widget.setCurrentIndex(widget.currentIndex() + 1)
#VIEW ENDS HERE

#DELETE STARTS HERE
class createDelete(QMainWindow):
    def __init__(self):
        super(createDelete, self).__init__()
        loadUi("testingDelete.ui", self)
        self.btnMin.clicked.connect(lambda: widget.showMinimized())
        self.btnClose.clicked.connect(lambda: widget.close())
        self.btnDelBack.clicked.connect(self.gotoBackDelete)
        self.btnDelete.clicked.connect(self.goDelete)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)
        self.loaddata()

    styleLineEditError = ("QLineEdit {\n"
                          "    border: 2px solid rgb(255, 85, 127);\n"
                          "    border-radius: 5px;\n"
                          "    background-color: rgb(30, 30, 30);    \n"
                          "    color: rgb(100, 100, 100);\n"
                          "}\n"
                          "QLineEdit:hover {\n"
                          "    border: 2px solid rgb(55, 55, 55);\n"
                          "}\n"
                          "QLineEdit:focus {\n"
                          "    border: 2px solid rgb(255, 207, 0);    \n"
                          "    color: rgb(200, 200, 200);\n"
                          "}")

    def loaddata(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        ret = database.child(accounts).get()
        row = 0
        item = 0
        for rets in ret.each():
            people = [rets.val()]
            item = item + 1
            self.tableWidget.setRowCount(item)
            for person in people:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['ID']))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Username']))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Password']))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Role']))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['FirstName']))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(person['LastName']))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(person['Age']))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(person['Gender']))
                self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(person['Birthdate']))
                self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(person['Contact']))
                self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(person['City']))
                row = row + 1

    def goDelete(self):
        config = {
            "apiKey": "AIzaSyBd5d6jyhT9OAUp791BYehrSSsWge2DDTQ",
            "authDomain": "employee-916e4.firebaseapp.com",
            "projectId": "employee-916e4",
            "databaseURL": "https://employee-916e4-default-rtdb.firebaseio.com/",
            "storageBucket": "employee-916e4.appspot.com",
            "messagingSenderId": "109236505740",
            "appId": "1:109236505740:web:96abde89677300c5783fa9",
            "measurementId": "G-4LHV2QY5XJ"
        }

        firebase = pyrebase.initialize_app(config)
        database = firebase.database()

        accounts = "Accounts"

        inpId = self.lbl_DelID.text()

        if inpId != "":
            database.child(accounts).child(inpId).remove()
            msg = QMessageBox()
            msg.setWindowTitle("NOTIFICATION")
            msg.setText("RECORD DELETED")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.loaddata()
        else:
            self.lbl_DelID.setStyleSheet(self.styleLineEditError)
            msg = QMessageBox()
            msg.setWindowTitle("WARNING!")
            msg.setText("ENTER THE ID")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def gotoBackDelete(self):
        backDelete = createHome()
        widget.addWidget(backDelete)
        widget.setCurrentIndex(widget.currentIndex()+1)
#DELETE ENDS HERE


app = QApplication(sys.argv)
mainUI = adminScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainUI)
ui = SplashScreen()
ui.show()
try:
    sys.exit(app.exec_())
except:
    print("Closing...")