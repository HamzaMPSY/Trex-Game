import cv2
import numpy as np
import tensorflow as tf
from keras import backend as K
from keras.models import model_from_json
import pyautogui,time          


def loadModel():
	json_file = open('game.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights("game.h5")
	print("Loaded model from disk")
	return loaded_model

isBgCaptured           = False    # bool, whether the background captured
cap_region_x_begin     = 0.0      # start point/total width
cap_region_y_end       = 0.5      # start point/total width
font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2
bottomLeftCornerOfText = (55,25)


replayBtn = (1044,387) # to change

def restartGame():
	pyautogui.click(replayBtn)

def  pressSpace():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	pyautogui.keyUp('space')


cap = cv2.VideoCapture(0)
ret,first_frame = cap.read()
model = loadModel()
decision = ['jump','continue running']

while ret:
	X = []
	ret,frame = cap.read()
	cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),(int(0.5* frame.shape[1]), int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
	img = frame[0:int(cap_region_y_end * frame.shape[0]),int(cap_region_x_begin * frame.shape[1]):int(0.5* frame.shape[1])]
	img = cv2.resize(img,(128,128))
	X.append(img)
	X = np.array(X)
	X = X/255.
	pred = model.predict(X)
	pred = np.argmax(pred,axis = 1)
	if pred[0] == 0:
		pressSpace() 
	cv2.putText(frame,decision[pred[0]],bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
	cv2.imshow('frame', frame)
	key = cv2.waitKey(10)
	if key == 27:   
		break
cap.release()
cv2.destroyAllWindows()