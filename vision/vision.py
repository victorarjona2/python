# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 19:32:53 2021

@author: vargo
"""

"""
xml pulled from:
    https://github.com/opencv/opencv/tree/master/data/haarcascades

code pulled from:
    https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
"""

import cv2
# import msvcrt

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Display
    cv2.imshow('img', img)
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    
    if k==27:
        cv2.destroyAllWindows()
        break
    
# Release the VideoCapture object
cap.release()