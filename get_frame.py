from cv2 import *
import sys
import numpy as np
import os
import datetime
import time
def getframe():
    now = datetime.datetime.now()
    faceid = now.strftime('%I:%M:%S%p')

    data_dir = "data/"
    frame_dir = "unidentified/"
    cascpath = data_dir + 'haarcascade_frontalface.xml'
    face_cascade = cv2.CascadeClassifier(cascpath)

    cap = cv2.VideoCapture(0)

    num = 0
    el_tiempo = time.time()
    el_tiempo_now = time.time()
    while not(el_tiempo_now - el_tiempo > 0.2):
        el_tiempo_now = time.time()
        # Capture frame-by-frame
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        x = 0
        y = 20
        text_color = (0,255,0)
        cv2.imwrite(frame_dir + (datetime.datetime.now().strftime('%I:%M:%S%p')) + '.jpeg',frame)
        num = num+1
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
