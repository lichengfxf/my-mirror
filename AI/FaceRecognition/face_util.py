#
# 使用opencv自带的人脸检测分类器，检测人脸
# 将检测到的人脸保存到当前目录
#
# 2021-11-03
# by 李成
#

import cv2
from config import *

#
# 全局变量
#
g_face_casc = None

def detect_from_img(img):
    faces = g_face_casc.detectMultiScale(img, scaleFactor=1.15, minNeighbors=5, minSize=(10, 10))    
    return faces
        
#
# 人脸检测
#
# @img 要检测的图像
# @face_cascad 人脸分类器
#
# 返回值：人脸部图像和对应的坐标，如果图像有多个人脸也仅仅返回1个
#
def face_detect(img, face_cascad): 
    # 转成灰度图片，提高检测速度
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 开始检测人脸
    faces = detect_from_img(img_gray)
    if len(faces) == 0:
        return [], []

    # 提取图像中的人脸
    (x, y, w, h) = faces[0]
    return img_gray[y:y+h, x:x+w], faces[0]

#
# 从图像文件中检测人脸
#
# 返回值：人脸部图像和对应的坐标，如果图像有多个人脸也仅仅返回1个
#
def detect_from_file(file_path, face_cascad):
    img = cv2.imread(file_path)
    face_gray, rect = face_detect(img, face_cascad)
    if len(face_gray) == 0:
        return [], []

    #
    # 调试：显示图片
    # 框出人脸
    #
    (x,y,w,h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)
    cv2.imshow(file_path, img)

    return face_gray, rect

# 初始化
def init():
    global g_face_casc

    # 载入人类检测分类器
    g_face_casc = cv2.CascadeClassifier(config_ai_fr_face_cascad_file_path)
