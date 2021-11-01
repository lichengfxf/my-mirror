import imp
from PIL.Image import WEB
from six import with_metaclass
from config import *
from cvzone.FaceDetectionModule import FaceDetector
from datetime import datetime

#
# 全局变量
#
g_mh_detector = None

#
# 接口函数
#

# 检测图片, 如果有人类则保存
def run(img):    
    img, bboxs = g_mh_detector.findFaces(img)
    if bboxs:
        _save_img(img)

#
# 辅助函数
#

# 保存图片
def _save_img(img):
    now = datetime.now()
    file_path = "{}/{}/{}.jpg".format(config_advance_monitor_data_dir, now().strftime('%Y%m%d'), now.strftime('%h_%M_%s'))
    with open(file_path, "wb") as f:
        f.write(img)

#
# 模块初始化
#
def init():
    global g_mh_detector
    g_mh_detector = FaceDetector()
