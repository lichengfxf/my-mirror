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
    app = QApplication(sys.argv)

    w = MainDlg()
    w.show()

    app.exec_()
