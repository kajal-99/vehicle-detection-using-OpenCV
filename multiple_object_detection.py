
import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('vehicles.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output video.avi',fourcc, 20.0,(596,336))
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 30,255, cv2.THRESH_BINARY)
    dialated = cv2.dilate(thresh, None, iterations=4)
    contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)


        if cv2.contourArea(contour) < 1300:
            continue
        cv2.rectangle(frame1,(x,y), (x+w,y+h), (0,0,255), 2)




    #cv2.drawContours(frame1,contours,-1,(0,255,0),3)
    out.write(frame1)
    cv2.imshow("video",frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(40) == 27:

         break



cap.release()
out.release()
cv2.destroyAllWindows()
