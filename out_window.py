# Modified by Augmented Startups & Geeky Bee
# October 2020
# Facial Recognition Attendence GUI
# Full Course - https://augmentedstartups.info/yolov4release
# *-
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, QTime ,Qt
from PyQt5.QtWidgets import QDialog,QMessageBox
import cv2
#import face_recognition
import numpy as np
import datetime
import os
#import dlib
import csv
import pyrebase
from math import hypot

class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        loadUi("./outputwindow.ui", self)
        #self.btnMin.clicked.connect(lambda: self.showMinimized())
        #self.btnClose.clicked.connect(lambda: self.close())
        #Update time
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%hh:%M %p")
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        self.Date_Label.setText(current_date)

        self.image = None

    def displayTime(self):
        currentTime = QTime.currentTime()

        displayText = currentTime.toString('hh:mm:ss A')
        self.Time_Label.setText(displayText)

    @pyqtSlot()
    def startVideo(self, camera_name):
        """
        :param camera_name: link of camera or usb camera
        :return:
        """

        if len(camera_name) == 1:
        	self.capture = cv2.VideoCapture(int(camera_name))
        else:
        	self.capture = cv2.VideoCapture(camera_name)
        self.timer = QTimer(self)  # Create Timer
        path = 'ImagesAttendance'
        if not os.path.exists(path):
            os.mkdir(path)

        # known face encoding and known face name list
        images = []
        self.class_names = []
        self.encode_list = []
        self.TimeList1 = []
        self.TimeList2 = []
        attendance_list = os.listdir(path)

        # print(attendance_list)
        for cl in attendance_list:
            cur_img = cv2.imread(f'{path}/{cl}')
            images.append(cur_img)
            self.class_names.append(os.path.splitext(cl)[0])
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            # encode = face_recognition.face_encodings(img)[0]
            self.encode_list.append(encodes_cur_frame)
        self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
        self.timer.start(10)  # emit the timeout() signal at x=40ms

    def face_rec_(self, frame, encode_list_known, class_names):
        """
        :param frame: frame from camera
        :param encode_list_known: known face encoding
        :param class_names: known face names
        :return:
        """
        # csv
        def mark_attendance(name):
            """
            :param name: detected face known or unknown one
            :return:
            """
            if self.ClockInButton.isChecked():
                self.ClockInButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                    if (name != 'unknown'):
                        buttonReply = QMessageBox.question(self, 'Welcome ' + name, 'Are you going to Time In?',
                                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if buttonReply == QMessageBox.Yes:
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

                            date_time_string = datetime.datetime.now().strftime("%y|%m|%d %I:%M:%p")
                            f.writelines(f'\n{name},{date_time_string},Clock In')
                            self.ClockInButton.setChecked(False)

                            date_now = datetime.datetime.now().strftime("%m|%d|%Y")
                            time_now = datetime.datetime.now().strftime("%I:%M:%p")

                            data = {"Name": name, "Time In": time_now, "Time Out": "00:00", "Working Hours": "0 hrs and 0 mins"}
                            database.child("Attendance").child(date_now).child(name).set(data)


                            self.NameLabel.setText(name)
                            self.StatusLabel.setText('Timed In')
                            self.TimeMeasure_2.setText('Measuring')

                            # self.CalculateElapse(name)
                            # print('Yes clicked and detected')
                            self.Time1 = datetime.datetime.now()
                            # print(self.Time1)
                            self.ClockInButton.setEnabled(True)

                        else:
                            print('Not clicked.')
                            self.ClockInButton.setEnabled(True)

            elif self.ClockOutButton.isChecked():
                self.ClockOutButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                        if (name != 'unknown'):

                            buttonReply = QMessageBox.question(self, 'Cheers ' + name, 'Are you going to Time Outt?',
                                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                            if buttonReply == QMessageBox.Yes:
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
                                storage = firebase.storage()

                                folder = "ImagesAttendance"

                                date_time_string = datetime.datetime.now().strftime("%y|%m|%d %I:%M:%p")
                                f.writelines(f'\n{name},{date_time_string},Clock Out')
                                self.ClockOutButton.setChecked(False)

                                date_now = datetime.datetime.now().strftime("%m|%d|%Y")
                                time_now = datetime.datetime.now().strftime("%I:%M:%p")

                                time_in = database.child("Attendance").child(date_now).child(name).child("Time In").get()

                                self.NameLabel.setText(name)
                                self.StatusLabel.setText('Timed Out')
                                self.Time2 = datetime.datetime.now()
                                #print(self.Time2)

                                self.ElapseList(name)
                                self.TimeList2.append(datetime.datetime.now())
                                CheckInTime = self.TimeList1[-1]
                                CheckOutTime = self.TimeList2[-1]
                                self.ElapseHours = (CheckOutTime - CheckInTime)
                                mins = ("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60) % 60) + ' mins')
                                hours = ("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60 ** 2)) + ' hrs')
                                self.TimeMeasure_2.setText(str(hours) + " and " + str(mins))
                                measure = (str(hours) + " and " + str(mins))
                                data = {"Name": name, "Time In": time_in.val(), "Time Out": time_now, "Working Hours": measure}
                                database.child("Attendance").child(date_now).child(name).set(data)
                                self.ClockOutButton.setEnabled(True)

                                os.remove(folder + "/" + str(name) +".jpg")
                            else:
                                print('Not clicked.')
                                self.ClockOutButton.setEnabled(True)

        #Blinker
        font = cv2.FONT_HERSHEY_SIMPLEX
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        def midpoint(p1, p2):
            return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

        def get_blinking_ratio(eye_points, facial_landmarks):
            left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
            right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
            center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
            center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

            hor_line = cv2.line(frame, left_point, right_point, 1)
            ver_line = cv2.line(frame, center_top, center_bottom, 1)

            hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
            ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

            ratio = hor_line_length / ver_line_length
            return ratio

        _, frame = self.capture.read()
        frameS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = detector(frameS)

        for face in faces:
            landmarks = predictor(frameS, face)

            left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
            blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

            if blinking_ratio > 5.7:
                print("Blinking")

                # face recognition
                faces_cur_frame = face_recognition.face_locations(frame)
                encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
                # count = 0
                for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
                    match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
                    face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
                    name = "unknown"
                    best_match_index = np.argmin(face_dis)
                    # print("s",best_match_index)
                    if match[best_match_index]:
                        name = class_names[best_match_index].upper()
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, name, (x1 + 6, y2 - 6), font, 0.5, (255, 255, 255), 1)
                    mark_attendance(name)

        return frame

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


    def ElapseList(self,name):
        with open('Attendance.csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 2

            Time1 = datetime.datetime.now()
            Time2 = datetime.datetime.now()
            for row in csv_reader:
                for field in row:
                    if field in row:
                        if field == 'Clock In':
                            if row[0] == name:
                                #print(f'\t ROW 0 {row[0]}  ROW 1 {row[1]} ROW2 {row[2]}.')
                                Time1 = (datetime.datetime.strptime(row[1], '%y|%m|%d %I:%M:%p'))
                                self.TimeList1.append(Time1)
                        if field == 'Clock Out':
                            if row[0] == name:
                                #print(f'\t ROW 0 {row[0]}  ROW 1 {row[1]} ROW2 {row[2]}.')
                                Time2 = (datetime.datetime.strptime(row[1], '%y|%m|%d %I:%M:%p'))
                                self.TimeList2.append(Time2)
                                #print(Time2)


    def update_frame(self):
        _, self.image = self.capture.read()
        self.displayImage(self.image, self.encode_list, self.class_names, 1)

    def displayImage(self, image, encode_list, class_names, window=1):
        """
        :param image: frame from camera
        :param encode_list: known face encoding list
        :param class_names: known face names
        :param window: number of window
        :return:
        """
        image = cv2.resize(image, (1040, 880))
        try:
            image = self.face_rec_(image, encode_list, class_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)




