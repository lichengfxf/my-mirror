from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5 import QtCore
from . import Ui_maindlg

class MainDlg(QDialog, Ui_maindlg.Ui_Dialog):
    def __init__(self):
        # 初始化
        super(MainDlg, self).__init__()
        self.setupUi(self)
        # 隐藏标题栏
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # 绑定按钮点击事件
        #self.btnHello.clicked.connect(self.OnBtnHelloClick)
    
    # 按钮点击事件
    def OnBtnHelloClick(self):
        QMessageBox.information(self, "hello", "你好")