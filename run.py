from Common import common
from Advance import advance
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
    # 加载界面
    ui.start()

# 运行
if __name__ == "__main__":
    # 加载模块
    load_modules()

    # 永远不结束
    while True:
        time.sleep(1)
