import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # cascade classifier contains face features

img = cv2.imread("lena.jpg", 1) # read the colored image

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert colored image to grayscale image

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5) # detect the face co-ordinates of the image

print(type(faces)) # numpy.ndarray
print(faces) # print face co-ordinates

for x,y,w,h in faces:
    gray_img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 2) # draw rectangle on face

resized = cv2.resize(gray_img, (int(gray_img.shape[0]/2), int(gray_img.shape[1]/2))) # resized the image

cv2.imshow("faceDetected", resized) # displaying the image on screen

cv2.waitKey(0) # delay the destory command 

cv2.destroyAllWindows() # destroy window

