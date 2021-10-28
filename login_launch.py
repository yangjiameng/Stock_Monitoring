from Stock_Monitoring.login import Ui_login
from Stock_Monitoring.tushare_test import *
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget
import socket
import sys
import ssl
import json


class launcher_ui(QDialog, Ui_login):

    def __init__(self):
        super().__init__()
        config_rw.config.read('message.ini')
        self.setupUi(self)
        self.setWindowIcon(QIcon("Icons/main_icon.ico"))
        # self.setStyleSheet("background-image:url(Icons/background.jpg)")
        self.progressBar_load.setVisible(False)
        self.label_load.setVisible(False)
        self.ti = QTimer()
        self.value = 10
        self.login_num = 0
        self.comboBox_user.addItems([config_rw.config['personal_message']['username'], 'clear'])
        self.lineEdit_password.setText(config_rw.config['personal_message']['password'])
        self.pushButton_login.clicked.connect(self.login_push)

    def login_push(self):
        if self.checkBox_remeber.isChecked():
            config_rw.config.set('personal_message', 'username', self.comboBox_user.currentText())
            config_rw.config.set('personal_message', 'password', self.lineEdit_password.text())
            config_rw.config.write(open('message.ini', 'w'))
        if self.soc():
            self.label_log.setText('登录成功!')
            self.label_load.setVisible(True)
            self.progressBar_load.setVisible(True)
            self.ti.start(100)
            self.ti.timeout.connect(self.pro_load)
            ui.timer.start(2000)
            ui.timer.timeout.connect(self.goto_ui)
        else:
            self.label_log.setText('账号或密码错误!')
            self.login_num += 1
            if self.login_num == 3:
                QMessageBox.warning(self, 'warning', '密码错误超过三次，软件退出!')
                ui_login.close()
            else:
                QMessageBox.warning(self, 'warning', '密码错误，重新输入!')

    def goto_ui(self):
        ui_login.close()
        ui.show()

    def pro_load(self):
        self.progressBar_load.setValue(self.value)
        self.value += 10

    def soc(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_client = context.wrap_socket(client)
        ssl_client.connect(('wyzs1314.com', 8080))
        login_msg = {'u': self.comboBox_user.currentText(), 'p': self.lineEdit_password.text()}
        json.dumps(login_msg)
        ssl_client.send(json.dumps(login_msg).encode())
        rec_msg = ssl_client.recv(4096).decode('utf-8')
        print(rec_msg)
        if rec_msg == 'yes':
            ssl_client.close()
            return 1
        ssl_client.close()
        return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_login = launcher_ui()
    ui = main_ui()
    ui_login.show()
    sys.exit(app.exec_())
