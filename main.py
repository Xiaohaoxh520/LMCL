import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from mainui import *
from downloadingui import *
import json
import os
import paper


class MainWindow(QMainWindow, Ui_MainWindow):
    server_path_list = []  # 读取服务器列表

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # QDarkStyle
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # servers.json
        if os.path.isfile("servers.json"):
            servers_json = open("servers.json", "r+")
            servers = servers_json.read()
            servers_py = json.loads(str(servers))
            servers_json.close()

            for i in servers_py:
                self.servers_list.addItem(i['name'])
                self.server_path_list.append(i['path'])

            self.server_path_label.setText(self.server_path_list[self.servers_list.currentIndex()])
            self.get_server_path_and_current_bid()
            self.servers_list.currentIndexChanged.connect(self.get_server_path_and_current_bid)
        else:
            servers_json = open("servers.json", "w+")
            servers_json.write("""[
          {
            "name": "Server1",
            "path": "/home/LMCL/Server1",
            "authlib_injector": true
          }
          {
            "name": "Server2",
            "path": "D:\\LMCL\\Server2",
            "authlib_injector": false
          }
        ]""")
            servers_json.close()
            QMessageBox.warning(self, "Error: 缺少servers.json！", "已自动为您新建servers.json，请自行修改后重试！",
                                QMessageBox.Ok, QMessageBox.Ok)
            sys.exit()

        # 初始化界面:
        self.update_button.hide()  # 隐藏按钮
        self.update_button.setEnabled(True)
        self.LaunchButton.setEnabled(True)

        jpg = QtGui.QPixmap('bg.jpg').scaled(self.pic_lable.width(), self.pic_lable.height())
        self.pic_lable.setPixmap(jpg)  # 设置背景图

        # 检查Paper更新
        bid = paper.get(self.get_server_path_and_current_bid()['ver'])  # 避免多次check
        self.paper_build_id_label.setText(self.get_server_path_and_current_bid()['ver'] +
                                          " #" + bid)

        if int(self.get_server_path_and_current_bid()['bid']) < int(bid):  # 比较得出是否需要更新
            print("[LMCL] You are not using the latest version of paper!")
            self.paper_build_id_label.setStyleSheet("color:rgb(255, 0, 0)")
            self.update_button.show()
            # 调用下载函数
            self.update_button.clicked.connect(self.download)
        else:
            self.paper_build_id_label.setStyleSheet("color:rgb(0, 255, 0)")
            self.paper_build_id_label.setText("Latest Version")

    def get_server_path_and_current_bid(self):
        server_path = self.server_path_list[self.servers_list.currentIndex()]
        self.server_path_label.setText(server_path)

        # 读取当前Build ID
        if os.path.isfile(server_path + "\\version_history.json"):
            bid_and_ver = {'bid': 0, 'ver': '1.8.8', 'string': '1.8.8 #443 (EXAMPLE)'}

            current_bid_json = open(server_path + "\\version_history.json", "r+")
            current_bid = current_bid_json.read()
            current_bid_json.close()
            current_bid_py = json.loads(current_bid)
            current_build = str(current_bid_py["currentVersion"]).replace("git-Paper-", "").find(" (")
            current_build_id = str(current_bid_py["currentVersion"]).replace("git-Paper-", "")[0:current_build]
            current_mc_ver = str(current_bid_py["currentVersion"]).replace("git-Paper-", "").find("(MC: ")
            current_without_unless = str(current_bid_py["currentVersion"]).replace("git-Paper-", "")

            bid_and_ver['bid'] = current_build_id
            bid_and_ver['ver'] = current_without_unless[current_mc_ver + 5:-1]
            bid_and_ver['string'] = current_without_unless[current_mc_ver + 5:-1] + " #" + str(current_build_id)

            self.current_build_id_label.setText(bid_and_ver['string'])
            return bid_and_ver
        else:
            QMessageBox.warning(self, "文件或目录不存在！", "无法找到文件：" + server_path + "\\version_history.json",
                                QMessageBox.Ok, QMessageBox.Ok)

    def download(self):  # 下载函数
        self.update_button.setText('Updating...')
        self.update_button.setEnabled(False)
        self.LaunchButton.setEnabled(False)
        paper.download(self.get_server_path_and_current_bid()['ver'],
                       self.server_path_list[self.servers_list.currentIndex()],
                       self)

    # 更新完成后的操作
    def updated_done(self):
        self.update_button.setEnabled(True)
        self.update_button.setText('Done!')
        self.LaunchButton.setEnabled(True)


if __name__ == '__main__':
    # Hello!
    print("Lite Minecraft Launcher 0.1(a1115) -- by Xiao_Jin")
    print('''
    ██╗     ███╗   ███╗ ██████╗██╗     
    ██║     ████╗ ████║██╔════╝██║     
    ██║     ██╔████╔██║██║     ██║     
    ██║     ██║╚██╔╝██║██║     ██║     
    ███████╗██║ ╚═╝ ██║╚██████╗███████╗
    ╚══════╝╚═╝     ╚═╝ ╚═════╝╚══════╝
    ''')

    # PyQt5
    app = QApplication(sys.argv)
    MainWin = MainWindow()

    MainWin.show()
    sys.exit(app.exec_())
