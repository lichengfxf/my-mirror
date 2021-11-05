#
# 使用face_train.py训练的数据进行人脸识别
#
# 2021-11-03
# by 李成
#

import cv2
from PIL import Image
from config import *
from . import face_util
from . import face_train

#
# 全局变量
#


#
# 从图片识别人脸
# 
def predict_from_img(img):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(config_ai_fr_lbph_face_recong)

    # 检测人脸
    # 转成灰度图片，提高检测速度
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_util.detect_from_img(img_gray)
    for face in faces:
        # 提取图像中的人脸
        (x, y, w, h) = face
        
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)

        # 识别人脸
        face_img = img_gray[y:y+h, x:x+w]        
        lable, confidence = recognizer.predict(face_img)
        name = face_train.get_name_by_lable(lable)
        print("name:{}, confidence:{:.1f}%".format(name, confidence))
    return img

def init():
    pass
