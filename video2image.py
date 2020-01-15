import cv2
vidcap = cv2.VideoCapture('straight.avi')
success,image = vidcap.read()
count = 1
success = True
while success:
  cv2.imwrite("straight/%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1