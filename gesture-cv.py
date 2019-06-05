import cv2
import imutils
import numpy as np
import os


cap = cv2.VideoCapture(0)
dir_path = os.path.dirname(os.path.realpath(__file__))
top, right, bottom, left = 10, 350, 350, 650

i=0
num_of_frames = 0
while True:
	ret, frame = cap.read()
	frame = imutils.resize(frame, width=700)
	frame = cv2.flip(frame, 1)
	roi = frame[top:bottom, right:left]
	num_of_frames+=1
	cv2.imshow('frame',frame)
	cv2.imshow("roi", roi)
	if num_of_frames>50:
		cv2.imwrite(dir_path+"/data_new/6/"+str(i)+'.jpg',roi)
		i+=1
	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()