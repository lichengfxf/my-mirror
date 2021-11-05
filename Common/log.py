#
# 日志模块
#
# 2021-11-05
# by 李成
#
import logging

# 初始化日志
def init():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)d - %(message)s')
