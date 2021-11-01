#
# 使用opencv自带的人脸检测分类器，检测人脸
# 将检测到的人脸保存到当前目录
#
# 2021-09-10
# by 李成
#

import os
import cv2

# 载入人类检测分类器
face_casc = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

# 打开摄像头
camera = cv2.VideoCapture(0)

# 人脸的保存位置
face_save_dir = "./img_face/licheng"
if not os.access(face_save_dir, os.F_OK):
    os.mkdir(face_save_dir)

# 开始检测
while True:
    # 标记是否检测到了人脸
    is_face_detected = False

    # 获取1帧
    ret, frame = camera.read()

    # 转成灰度图片，提高检测速度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 开始检测人脸
    faces = face_casc.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(10, 10))
    if len(faces) > 0:
        is_face_detected = True        
    print("发现{0}个目标!".format(len(faces)))

    # 绘制提示文字
    cv2.putText(frame, "press key S to save", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # 框出人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 2)
        img_face = frame[y:y+h, x:x+w]
        img_face_gray = cv2.cvtColor(img_face, cv2.COLOR_BGR2GRAY)
        cv2.imshow("face", img_face_gray)
        # 检测用户输入
        key = cv2.waitKey(1000) & 0xff
        if key == ord('s'):
            file_path = "{0}/{1:0>4d}.jpg".format(face_save_dir, len(os.listdir(face_save_dir)))
            cv2.imwrite(file_path, img_face_gray)
            print("save file {0}".format(file_path))

    # 显示这一帧图片
    cv2.imshow("frame", frame)

    if not is_face_detected:
        key = cv2.waitKey(1)
        if key == 'q':
            break

# 释放资源
camera.release()
cv2.destroyAllWindows()

