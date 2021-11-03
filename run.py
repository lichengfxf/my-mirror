#
# 项目入口模块
#
# 2021-10-20
# by 李成
#

from Common import common
from Advance import advance
from AI import ai
from UI import ui
import time

#
# 加载各个模块
#
def load_modules():
    # 公用模块
    common.start()
    # 扩展模块
    advance.start()
    # 人工智能模块
    ai.start()
    # 加载界面
    ui.start()

# 运行
if __name__ == "__main__":
    # 加载模块
    load_modules()

    # 永远不结束
    while True:
        time.sleep(1)
