import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from Wnd.MainDlg import *
 
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainDlg()
    w.show()

    sys.exit(app.exec_())

