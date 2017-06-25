# FaceRecognition
It's a simple face recognition in python 3.6. In this project uses next modules:
- OpenCV3(for a face recognition)
- PyQt5(for user interface)

Recognition method and display result:
```python
imagePath = self.fname
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30)
        )

print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
save = "recog.png"
cv2.imwrite(save, image)
px = QPixmap(save)
self.ui.label_5.setPixmap(px)
```
View application 
----------------
![alt text](https://github.com/skinex/FaceRecognition/blob/master/demo.png)
