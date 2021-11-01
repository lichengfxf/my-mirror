#
# 使用face_collect.py收集到的人脸数据进行训练
#
# 2021-09-10
# by 李成
#

import cv2
import os
import numpy
import json
from PIL import Image

#
# 从目录载入图像
#
# 返回值：@train_imgs图像数组
#        处理的图像文件个数
#
def load_imgs(img_dir, train_imgs):
    files = os.listdir(img_dir)
    for file in files:        
        img = Image.open(os.path.join(img_dir, file))
        img = img.resize((150, 150), Image.ANTIALIAS)
        img_array = numpy.array(img)
        train_imgs.append(img_array)
    return len(files)
#
# 从文件读取图像和标签
#
# 返回值：图像数组和标签数组
#
def load_img_and_lables(lable_file_path):
    train_imgs = []
    train_lables = []
    # 从json文件读取配置信息
    fp = open(lable_file_path)
    j = json.load(fp)
    config = j["config"]
    for c in config:
        name = c["name"]
        lable = c["lable"]
        img_dir = c["img_dir"]
        
        count = load_imgs(img_dir, train_imgs)
        for i in range(count):
            train_lables.append(lable)
    return train_imgs, train_lables

#
# 主函数
#
if __name__ == "__main__":
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    train_imgs, train_lables = load_img_and_lables("img_lables_conf.json")
    recognizer.train(train_imgs, numpy.array(train_lables))
    recognizer.save("lbph_face_recong.yml")