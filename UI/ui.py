import sys
from PyQt5.QtWidgets import QApplication
from UI.Wnd.MainDlg import *

# 执行
def run():
    app = QApplication(sys.argv)

    w = MainDlg()
    w.show()

    app.exec_()
