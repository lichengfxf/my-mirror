#
# 视频读取模块
#
# 此模块提供一个接口，用于给其他模块读取摄像头数据
#
# 2021-11-02
# by 李成
#

import cv2
from PyQt5.QtCore import QMutex

#
# 全局变量
#

# 摄像头
g_cap = None
g_mutex = None

# 从摄像头读取一帧数据
def read_frame():
    g_mutex.lock()
    ret, frame = g_cap.read()
    g_mutex.unlock()
    if ret:
        # 因为摄像头看到的是镜像的图片，所以水平翻转图片
        frame = cv2.flip(frame, 1)
        return ret, frame
    return ret, frame

# 初始化
def init():    
    global g_cap
    global g_mutex

    g_cap = cv2.VideoCapture(0)
    g_mutex = QMutex()