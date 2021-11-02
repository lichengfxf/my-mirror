from UI import ui
from Advance import advance
import time

#
# 加载各个模块
#
def load_modules():
    # 扩展模块
    advance.run()
    # 加载界面
    ui.run()

# 运行
if __name__ == "__main__":
    # 加载模块
    load_modules()

    # 永远不结束
    while True:
        time.sleep(1)
