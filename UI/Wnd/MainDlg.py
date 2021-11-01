from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtWidgets import  QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore
from . import Ui_maindlg
import cv2
from cvzone.FaceDetectionModule import FaceDetector

#
# 主界面
#
class MainDlg(QDialog, Ui_maindlg.Ui_Dialog):
    def __init__(self):
        # 初始化
        super(MainDlg, self).__init__()
        self.setupUi(self)
        # 设置窗口大小
        self.resize(800, 1000)
        # 隐藏标题栏
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # 绑定按钮点击事件
        #self.btnHello.clicked.connect(self.OnBtnHelloClick)

        # 创建视频显示线程，绑定后台线程图片显示事件
        self.vedio_show_thread = VideoThread(self)
        self.vedio_show_thread.show_vedio_img.connect(self.ShowImg)
        self.vedio_show_thread.start()
    
    # 按钮点击事件
    def OnBtnHelloClick(self):
        QMessageBox.information(self, "hello", "你好")

    # 显示图片
    def ShowImg(self, image):
        self.VideoShow.setPixmap(QPixmap.fromImage(image))

#
# 后台线程获取视频数据
#
class VideoThread(QThread):
    #
    # 通过信号把视频图片发送到主界面
    #
    show_vedio_img = pyqtSignal(QImage)

    detector = FaceDetector()

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                # 因为摄像头看到的是镜像的图片，所以水平翻转图片
                frame = cv2.flip(frame, 1)
                frame, bboxs = self.detector.findFaces(frame)
                rgbImage  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 转换成QImage
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                img = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                # 发送到主界面显示
                self.show_vedio_img.emit(img)