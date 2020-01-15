# TrexGame
A python script to play Trex game (not only when your internet goes down :p) with your hand gestures , i use Keras to build the CNN that can predict if the hand is open or close, to produce your owen data set you can use the same script in the main.py and add a output to save the video in tne blue square. after that you can use video2image to cut the video into images after that train te sequential model, i upload the data to drive so i can use it in collab ( i don't have GPU :'( ).

if you wanna use my dataset : https://drive.google.com/open?id=1j8xrydRcJ94oVr5M2-WJrrgWFxEn1d8y


## Requirements
```
cv2
numpy
tensorflow
keras
pyautogui
```
Use the pip commande to install this requirements : pip install "package name"