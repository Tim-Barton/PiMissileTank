from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
while True:
    s, img = cam.read()
    if s:    # frame captured without any errors
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        