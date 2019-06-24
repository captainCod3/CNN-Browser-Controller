import cv2
import imutils
import numpy as np
import os
import numpy as np

from keras.models import model_from_json

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
	if num_of_frames%50==0:
		resized = cv2.resize(roi,(IMG_SIZE,IMG_SIZE))
		print(np.argmax(loaded_model.predict(resized.reshape(1,IMG_SIZE,IMG_SIZE,3)))+1)

    # if num_of_frames%50==0:
    #     resized = cv2.resize(roi,(IMG_SIZE,IMG_SIZE))
    #     print(np.argmax(loaded_model.predict(resized.reshape(1,IMG_SIZE,IMG_SIZE,3)))+1)

	# if num_of_frames>50:
	# 	cv2.imwrite(dir_path+"/data_new/6/"+str(i)+'.jpg',roi)
	# 	i+=1
	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

