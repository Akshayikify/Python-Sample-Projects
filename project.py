import cv2 #imported the opencv package
detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#Acessing the haarcascade classifier
imp_img=cv2.VideoCapture("images/mark.jpg")#Processing the elon.jpg
res,img=imp_img.read()#Here the res is storing the result-True/False(Whether image read or not) and img->Imagecoordinates
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #COnverting the image into gray scale image
faces=detect.detectMultiScale(gray,1.3,5) #Detect faces of different sizes

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
cv2.imshow("Mark Zukenberg Image",img) 
cv2.waitKey(0) #It shows the delay at which the image appears
imp_img.release() #Releasing the captured image

cv2.destroyAllWindows() #Destroying the windows that opened the image
