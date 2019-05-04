"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2
from keras.models import load_model

import numpy as np
from keras.preprocessing import image

from ui_main_window import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = self.face_cascade.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(35,35)
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (50,50,200), 2)
            
            sub_face = image[y:y+h, x:x+w]
            #cv2.imshow("Image",sub_face)
            test_image = cv2.resize(sub_face, (64, 64) )
            #test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = self.new_model.predict(test_image)
            if result[0][0] == 1:
                prediction = 'Anger'
            if result[0][1] == 1:
                prediction = 'Disgust'
            if result[0][2] == 1:
                prediction = 'Happiness'
            if result[0][3] == 1:
                prediction = 'Neutral'
            if result[0][4] == 1:
                prediction = 'Sadness'
            if result[0][5] == 1:
                prediction = 'Surprise'
            cv2.putText(image, prediction, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), lineType=cv2.LINE_AA)
            
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            self.cap = cv2.VideoCapture(0)
            self.new_model = load_model('emotionClassifier.h5')
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
            self.ui.control_bt1.hide()
            self.ui.control_bt2.hide()
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
