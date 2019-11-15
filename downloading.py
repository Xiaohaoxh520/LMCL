import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QDialog
from downloadingui import *


class MainWindow(QDialog, Ui_Downloading_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # QDarkStyle
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # 关闭窗口事件
    def closeEvent(self, event):
        # reply = QMessageBox.question(self, 'Stop Downloading?', "Are you sure to stop downloading right now?",
        #                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     # 调用event的accept方法才会真正关闭窗口
        #     event.accept()
        # else:
        #     # 调用event的ignore方法取消窗口的关闭动作
        event.ignore()


# if __name__ == '__main__':
app = QApplication(sys.argv)
MainWin = MainWindow()
MainWin.show()
# sys.exit(app.exec_())
