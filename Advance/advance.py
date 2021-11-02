#
# 高级功能模块入口
#
# 包括：监控模块
#
# 2021-11-02
# by 李成
#

from Advance.Monitor import monitor_human

def start():
    monitor_human.init()