#
# 图形界面主窗口
#
# 2021-10-23
# by 李成
#

from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore
import cv2
import numpy as np
from Common import video
from . import Ui_main_wnd
from AI.FaceRecognition import face_collect
from AI.FaceRecognition import face_train
from AI.FaceRecognition import face_recognition

#
# 主界面
#
class MainDlg(QDialog, Ui_main_wnd.Ui_Dialog):
    def __init__(self):
        # 初始化
        super(MainDlg, self).__init__()
        self.setupUi(self)
        # 设置窗口大小
        self.resize(800, 1000)
        # 隐藏标题栏
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # 绑定按钮点击事件
        self.btnStartCollect.clicked.connect(self.OnBtnStartCollectClick)
        self.btnStartTrain.clicked.connect(self.OnBtnStartTrainClick)
        self.btnStartPredict.clicked.connect(self.OnBtnStartPredictClick)

        # 创建视频显示线程，绑定后台线程图片显示事件
        self.vedio_show_thread = VideoThread(self)
        self.vedio_show_thread.show_vedio_img.connect(self.ShowImg)
        self.vedio_show_thread.start()

        # 开始识别人脸
        self.start_predict = False
    
    # 收集人脸数据
    def OnBtnStartCollectClick(self):
        face_name = self.txtFaceName.toPlainText()
        face_collect.g_fc_thread.slot_start_collect(face_name)

    # 开始训练人脸模型
    def OnBtnStartTrainClick(self):
        face_train.train()

    # 开始识别人脸
    def OnBtnStartPredictClick(self):
        self.start_predict = True

    # 显示图片
    def ShowImg(self, frame):
        if self.start_predict:
            face_recognition.predict_from_img(frame)
            self.start_predict = False

        # 转换成QImage
        img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.VideoShow.setPixmap(QPixmap.fromImage(img))

#
# 后台线程获取视频数据
#
class VideoThread(QThread):
    #
    # 通过信号把视频图片发送到主界面
    #
    show_vedio_img = pyqtSignal(np.ndarray)

    def run(self):
        while True:
            ret, frame = video.read_frame()
            if ret:
                # 发送到主界面显示
                self.show_vedio_img.emit(frame)
