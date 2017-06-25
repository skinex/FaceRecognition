import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from ui import *

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showDialog)
        self.show()

    def showDialog(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/')[0]
        pixmap = QPixmap(self.fname)
        self.ui.label_3.setPixmap(pixmap)
        self.recognition()

    def recognition(self):
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = form()
    sys.exit(app.exec_())
