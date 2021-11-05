#
# Common入口模块
#
# 此模块封装以下通用的、其他模块都会使用到的功能
#
# 2021-11-02
# by 李成
#

from Common import video
from Common import log
def start():
    log.init()
    video.init()