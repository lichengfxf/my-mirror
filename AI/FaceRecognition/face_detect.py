#
# 使用opencv自带的人脸检测分类器，检测人脸
#
# 2021-09-09
# by 李成
#

import os
import cv2

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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 开始检测人脸
    faces = face_cascad.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(10, 10))    
    if len(faces) == 0:
        return [], []

    # 提取图像中的人脸
    (x, y, w, h) = faces[0]
    return gray[y:y+h, x:x+w], faces[0]

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

#
# 从摄像头检测人脸
#
def dectect_from_camera(face_cascad):    
    # 打开摄像头
    camera = cv2.VideoCapture(0)

    # 开始检测
    while True:
        # 获取1帧
        ret, frame = camera.read()

        # 开始检测人脸
        face_gray, rect = face_detect(frame, face_cascad)
        if len(face_gray) == 0:
            continue
        
        # 框出人脸
        (x,y,w,h) = rect
        cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 2)

        # 显示这一帧图片
        cv2.imshow("frame", frame)

        # Display the resulting frame
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

    # 释放资源
    camera.release()
    cv2.destroyAllWindows()

#
# 主函数
#
if __name__ == "__main__":
    # 载入人类检测分类器
    face_cascad = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    #
    # 从摄像头检测人脸
    #
    dectect_from_camera(face_cascad)

    #
    # 从图片文件检测
    #
    src_img_dir = "img/"
    dst_img_dir = "img_face/ssd/"
    for file in os.listdir(src_img_dir):
        file_path = os.path.join(src_img_dir, file)
        face, rect = detect_from_file(file_path, face_cascad)
        if len(face) != 0:
            # 保存检测到的人脸
            cv2.imwrite(dst_img_dir + file, face)
    
    cv2.waitKey(0)