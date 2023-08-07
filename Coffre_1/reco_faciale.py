import face_recognition
import numpy as np
import queue, threading, time
import cv2 as cv
import requests, os, re
from time import perf_counter

webcam = cv.VideoCapture(0)
t1_start = perf_counter()
frame_count = 0
NB_IMAGES = 100
# Get files from openCV : https://github.com/opencv/opencv/tree/3.4/data/haarcascades
classCascadefacial = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
classCascadeEyes = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
classCascadeSmile = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_profileface.xml")



def facialDetectionAndMark(_image, _classCascade):
    imgreturn = _image.copy()
    gray = cv.cvtColor(imgreturn, cv.COLOR_BGR2GRAY)
    faces = _classCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv.rectangle(imgreturn, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return imgreturn


def videoDetection(_haarclass):
    if webcam.isOpened():
        while True:
            bImgReady, imageframe = webcam.read()  # get frame per frame from the webcam
            if bImgReady:
                face = facialDetectionAndMark(imageframe, _haarclass)
                cv.imshow('My webcam', face)  # show the frame
            else:
                print('No image available')
            keystroke = cv.waitKey(20)  # Wait for Key press
            if keystroke == 27:
                break  # if key pressed is ESC then escape the loop

        webcam.release()
        cv.destroyAllWindows()


videoDetection(classCascadefacial)


