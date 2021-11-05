#
# 图形界面应用程序，负责启动图形界面
#
# 2021-11-03
# by 李成
#

import sys
from PyQt5.QtWidgets import QApplication
from UI.Wnd.main_wnd import *

# 运行主界面
def run():
    # 创建应用程序    
    app = QApplication(sys.argv)

    # 创建主窗口
    w = MainDlg()
    w.show()

    # 运行应用程序
    app.exec_()
