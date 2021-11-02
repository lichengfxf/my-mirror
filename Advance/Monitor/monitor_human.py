import imp
from PIL.Image import WEB
from six import with_metaclass
from config import *
from cvzone.FaceDetectionModule import FaceDetector
from datetime import datetime
import os
import cv2

#
# 全局变量
#
g_mh_detector = None

#
# 接口函数
#

# 检测图片, 如果有人脸则保存
def monitor(img):
    img, bboxs = g_mh_detector.findFaces(img)
    if len(bboxs) > 0:
        _save_img(img)

#
# 辅助函数
#

# 保存图片
def _save_img(img):
    now = datetime.now()
    dir = "{}/{}".format(config_advance_monitor_data_dir, now.strftime('%Y%m%d'))
    if not os.access(dir, os.F_OK):
        os.makedirs(dir)
    file_path = "{}/{}.jpg".format(dir, now.strftime('%H_%M_%S'))
    cv2.imwrite(file_path, img)
    # with open(file_path, "wb") as f:
    #     f.write(img)

#
# 模块初始化
#
def init():
    global g_mh_detector
    g_mh_detector = FaceDetector()
