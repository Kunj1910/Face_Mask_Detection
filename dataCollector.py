import cv2

video=cv2.VideoCapture(1)

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count=2000

while True:
	ret,frame=video.read()
	faces=facedetect.detectMultiScale(frame,1.3, 5)
	for x,y,w,h in faces:
		count+=1
		name='./images/1/'+ str(count) + '.jpg'
		print("Creating Images........." +name)
		cv2.imwrite(name, frame[y:y+h,x:x+w])
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
	cv2.imshow("WindowFrame", frame)
	cv2.waitKey(1)
	if count>2499:
		break
video.release()
cv2.destroyAllWindows()