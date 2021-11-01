#
# 使用face_train.py训练的数据进行人脸识别
#
# 2021-09-11
# by 李成
#

import cv2
from PIL import Image
import face_detect
from config import *

#
# 主函数
#
if __name__ == "__main__":
    # 载入人类检测分类器
    face_cascad = cv2.CascadeClassifier(config_face_cascad_file_path)
    # 载入人脸识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('lbph_face_recong.yml')

    # 检测人脸
    img_face, rect = face_detect.detect_from_file("img/1 (1).png", face_cascad)
    cv2.imshow("img", img_face)
    # 识别人脸
    lable, confidence = recognizer.predict(img_face)
    print("lable:{}, confidence:{}".format(lable, confidence))

    cv2.waitKey(0)