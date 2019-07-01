import cv2
import imutils
import numpy as np
import os

from keras.models import model_from_json

from pykeyboard import PyKeyboard
#import the sleep function
from time import sleep
#initialize the keyboard simulator
k = PyKeyboard()

# k.press_key(k.control_key)
# k.press_key(k.alt_key)
# k.tap_key('t')
# k.release_key(k.alt_key)
# k.release_key(k.control_key)

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")


cap = cv2.VideoCapture(0)
dir_path = os.path.dirname(os.path.realpath(__file__))
top, right, bottom, left = 10, 350, 350, 650

num_of_frames = 0
IMG_SIZE = 160

while True:
	ret, frame = cap.read()
	frame = imutils.resize(frame, width=700)
	frame = cv2.flip(frame, 1)
	roi = frame[top:bottom, right:left]
	num_of_frames+=1
	cv2.imshow('frame',frame)
	cv2.imshow("roi", roi)
	if num_of_frames%100==0 and num_of_frames>150:
		resized = cv2.resize(roi,(IMG_SIZE,IMG_SIZE))
		print(np.argmax(loaded_model.predict(resized.reshape(1,IMG_SIZE,IMG_SIZE,3)))+1)
		val = np.argmax(loaded_model.predict(resized.reshape(1,IMG_SIZE,IMG_SIZE,3)))+1
		if val==1:
			k.press_key(k.control_key)
			k.tap_key('n')
			k.release_key(k.control_key)
		elif val==2:
			k.press_key(k.control_key)
			k.tap_key('t')
			k.release_key(k.control_key)
		elif val==3:
			k.press_key(k.control_key)
			k.press_key(k.shift_key)
			k.tap_key('t')
			k.release_key(k.shift_key)
			k.release_key(k.control_key)
		elif val==4:
			k.press_key(k.control_key)
			k.press_key(k.shift_key)
			k.tap_key('n')
			k.release_key(k.shift_key)
			k.release_key(k.control_key)
		elif val==5:
			k.press_key(k.control_key)
			k.press_key(k.shift_key)
			k.tap_key(k.tab_key)
			k.release_key(k.shift_key)
			k.release_key(k.control_key)
		elif val==6:
			k.press_key(k.control_key)
			k.press_key(k.shift_key)
			k.tap_key('n')
			k.release_key(k.shift_key)
			k.release_key(k.control_key)

	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
