#
# AI模块入口
#
# 包括：人脸识别
#
# 2021-11-01
# by 李成
#

from AI.FaceRecognition import face_util
from AI.FaceRecognition import face_collect
from AI.FaceRecognition import face_recognition

def start():
    face_util.init()
    face_collect.init()
    face_recognition.init()