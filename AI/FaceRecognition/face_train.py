#
# 使用face_collect.py收集到的人脸数据进行训练
# 使用模型LBPHFaceRecognizer
#
# 2021-11-03
# by 李成
#

'''
在实际人脸识别中，有很多可用方法，如OpenCV自带的EigenFaceRecognizer(基于PCA降维),FisherFaceRecognizer(基于LDA降维)，
LBPHFaceRecognizer(基于LBPH特征)，其中只有LBPHFaceRecognizer是支持直接更新的模型算法；
再如faceNet深度网络模型（128个特征输出）加分类器（如SVM）方式。其他商业应用如旷视科技Megvii Face++,百度AI,等等很多。
我们需要应用的场景是结果好，对于硬件要求不是很高，方便更新模型，低成本的方式。
因此我选择了OpenCV自带的LBPHFaceRecognizer算法，这种算法优点是不会受到光照、缩放、旋转和平移的影响，
这种算法最大的好处就是可以在性能不是很高的ARM板上也可执行，通用化非常好。
————————————————
版权声明：本文为CSDN博主「宋连猛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43521467/article/details/103584342
'''

import cv2
import os
import numpy
import json
from PIL import Image
from config import *

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
# 分析人脸数据收集目录，生成训练配置文件
# 该目录下的文件夹名称作为人名，文件夹内的图片作为人名的训练数据
# 由于训练的时候要求label是int型，所以这里需要建立人名和label的映射关系
# 
def generate_train_config():    
    # 生成人名和图片的映射关系
    name_img_map = {}
    files = os.listdir(config_ai_fr_data_collect)
    for file in files:
        name = file
        img_dir = os.path.join(config_ai_fr_data_collect, file)
        name_img_map[name] = img_dir
    
    # 如果没有找到训练数据，返回失败
    if len(name_img_map) == 0:
        return False

    # 建立人名和label的映射关系
    i = 1
    name_lable_map = {}
    for name in name_img_map:
        name_lable_map[name] = i
        i += 1

    # 写入训练配置文件
    config = []
    for name in name_img_map:
        img_dir = name_img_map[name]
        lable = name_lable_map[name]
        config.append({"name": name, "lable": lable, "img_dir": img_dir})
    with open(config_ai_fr_conf_train_data, "w") as fp:
        json.dump({"config": config}, fp, indent=4, ensure_ascii=False)

    return True

#
# 从训练配置文件读取图像和标签
#
# 返回值：图像数组和标签数组
#
def load_img_and_lables(conf_face_labels):
    train_imgs = []
    train_lables = []
    # 从json文件读取配置信息
    with open(conf_face_labels) as fp:
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
# 从训练配置文件中根据标签获取人名
#
def get_name_by_lable(lable):
    with open(config_ai_fr_conf_train_data) as fp:
        j = json.load(fp)
        config = j["config"]
        for c in config:
            if c["lable"] == lable:
                return c["name"]
    return ""

#
# 训练
#
def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 读取训练数据
    if not generate_train_config():
        print("没有找到训练数据，请先收集训练数据")
        return
    train_imgs, train_lables = load_img_and_lables(config_ai_fr_conf_train_data)
    # 训练
    recognizer.train(train_imgs, numpy.array(train_lables))
    # 保存训练结果
    recognizer.save(config_ai_fr_lbph_face_recong)
