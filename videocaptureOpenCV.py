import cv2

video = cv2.VideoCapture("Megamind.avi") # capturing the video
a = 1 # create variale to count the no of frames

while video.isOpened(): # isOpened method return True if video is captured successfully esle False
    a += 1 # increment no of frame count
    check, frame = video.read() # read() method retrun True and frames if video captured esle False None
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converting the colored image in grayscale
    cv2.imshow("video", gray) # displaying the image on screen
    key = cv2.waitKey(20) # delay the key
    if key == ord("q"): # if user press q then loop break
        break
    
print(a) # printing no of frames
video.release() # release video
cv2.destroyAllWindows() # close all windows