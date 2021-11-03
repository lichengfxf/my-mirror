#
# 使用opencv自带的人脸检测分类器，检测人脸
# 将检测到的人脸保存到当前目录
#
# 2021-11-03
# by 李成
#

import os
from PIL.Image import init
import cv2
from numpy.lib.function_base import select
from config import *
from Common import video
from PyQt5.QtCore import QThread
from datetime import datetime

#
# 全局变量
#
g_face_casc = None
g_fc_thread = None

# 收集人脸数据保存到文件
def collect_face_to_file(img, face_name):
    now = datetime.now()
    dir = "{}/{}".format(config_ai_fr_data_collect, face_name)
    if not os.access(dir, os.F_OK):
        os.makedirs(dir)
    file_path = "{}/{}.jpg".format(dir, now.strftime('%H_%M_%S'))
    cv2.imwrite(file_path, img)

# 收集人脸数据到视频文件
def collect_face_to_video(img, face_name):
    pass

#
# 后台数据收集线程
#
class face_collect_thread(QThread):
    start_colletc = False
    face_name = ""

    # 收集线程
    def run(self):
        while True:
            self.sleep(1)
            
            # 等待收集信号开启
            if not self.start_colletc:
                continue

            ret, frame = video.read_frame()
            if ret:                        
                # 转成灰度图片，提高检测速度
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 开始检测人脸
                faces = g_face_casc.detectMultiScale(frame_gray, scaleFactor=1.15, minNeighbors=5, minSize=(10, 10))
                if len(faces) > 0:
                    # 框出人脸
                    for (x, y, w, h) in faces:
                        img_face_gray = frame_gray[y:y+h, x:x+w]
                        collect_face_to_file(img_face_gray, self.face_name)

    # 启动收集
    def slot_start_collect(self, face_name):
        self.face_name = face_name
        self.start_colletc = True

# 初始化
def init():
    global g_face_casc
    global g_fc_thread

    # 载入人类检测分类器
    g_face_casc = cv2.CascadeClassifier(config_ai_fr_face_cascad_file_path)

    # 创建相关目录
    if not os.access(config_ai_fr_data_collect, os.F_OK):
        os.makedirs(config_ai_fr_data_collect)

    # 创建后台人脸收集线程
    g_fc_thread = face_collect_thread()
    g_fc_thread.start()