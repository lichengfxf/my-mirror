#
# 监控模块
#
# 定时检测摄像头，如果发现有人就拍一张照片保存到本地
#
# 2021-11-02
# by 李成
#

from config import *
from cvzone.FaceDetectionModule import FaceDetector
from datetime import datetime, time
from PyQt5.QtCore import QThread
from Common import video
import os
import cv2
# vscode多线程调试断点无法断下，使用pdb手动调试
import pdb

#
# 全局变量
#
g_mh_detector = None
g_mh_thread = None

#
# 定时监控线程
#
class monitor_thread(QThread):
    def run(self):
        while True:
            self.sleep(config_advance_monitor_interval)
            # 设置调试断点
            #pdb.set_trace()
            ret, frame = video.read_frame()
            if ret:
                _detect_and_save(frame)

#
# 辅助函数
#

# 检测图片, 如果有人脸则保存
def _detect_and_save(img):
    img, bboxs = g_mh_detector.findFaces(img)
    if len(bboxs) > 0:
        _save_img(img)

# 保存图片
def _save_img(img):
    now = datetime.now()
    dir = "{}/{}".format(config_advance_monitor_data_dir, now.strftime('%Y%m%d'))
    if not os.access(dir, os.F_OK):
        os.makedirs(dir)
    file_path = "{}/{}.jpg".format(dir, now.strftime('%H_%M_%S'))
    cv2.imwrite(file_path, img)

#
# 模块初始化
#
def init():    
    global g_mh_detector
    global g_mh_thread

    # 初始化人脸检测器
    g_mh_detector = FaceDetector()

    # 启动定时监控线程
    g_mh_thread = monitor_thread()
    g_mh_thread.start()

