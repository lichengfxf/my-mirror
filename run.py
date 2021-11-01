from UI import ui
import time

#
# 加载各个模块
#
def load_modules():
    # 加载界面
    ui.run()

# 运行
if __name__ == "__main__":
    # 加载模块
    load_modules()

    # 永远不结束
    while True:
        time.sleep(1)
