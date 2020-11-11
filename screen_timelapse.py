# convert map into data
import time
import cv2
# screen captuer library that is the fastest if have found so far
import mss
import mss.tools
import numpy as np

CAP_INTERVAL = 1.0
MONITOR_NUM = 2
SAVE_FILE_NAME = 'outvideo.avi'
DOWNSAMPLE = .5

def grabEntireScreen():
	with mss.mss() as sct:
		monitorNumber = MONITOR_NUM
		monitor = sct.monitors[monitorNumber]

		entireScreen = {
			'top': int(monitor['top']),
			'left': int(monitor['left']),
			'width': int(1920),
			'height': int(1080),
			'mon': monitorNumber,
		}

		capturedImage = sct.grab(entireScreen)
		return np.array(capturedImage)[:,:,0:3]

if(__name__ == '__main__'):

	size = (1920, 1080)
	if DOWNSAMPLE < 1.0:
		size = (int(size[0] * DOWNSAMPLE),  int(size[1] * DOWNSAMPLE))
	print(str(size))

	video = cv2.VideoWriter(SAVE_FILE_NAME, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

	while 1:
		time.sleep(CAP_INTERVAL)
		frame = grabEntireScreen()

		if DOWNSAMPLE < 1.0:
			frame = cv2.resize(frame, size)

		video.write(frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	video.release()

