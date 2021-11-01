import imp
from PIL.Image import WEB
from six import with_metaclass
from config import *
from cvzone.FaceDetectionModule import FaceDetector
from datetime import datetime

# 保存图片
def save_img(img):
    now = datetime.now()
    file_path = "{}/{}/{}.jpg".format(config_advance_monitor_data_dir, now().strftime('%Y%m%d'), now.strftime('%h_%M_%s'))
    with open(file_path, "wb") as f:
        f.write(img)

# 检测图片, 如果有人类则保存
def run(img):
    detector = FaceDetector()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        save_img(img)

#
# 模块初始化
#
def init():
    detector = FaceDetector()
