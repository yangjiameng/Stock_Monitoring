import tushare as ts
import pandas as pd
from time import sleep
import tkinter.messagebox
import tkinter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QMutex
import pyqtgraph as pg
import numpy as np
import sys
from Stock_Monitoring.StockUI import Ui_Stock_Monitoring
import matplotlib


def data_frame(data):
    df = pd.DataFrame(data=data)
    df_name = df.loc[0, 'name']
    df_price = df.loc[0, 'price']
    df_pre_close = df.loc[0, 'pre_close']
    df_percentage = (float(df_price) - float(df_pre_close)) / float(df_pre_close) * 100
    if df_percentage >= 0:
        a_color = '红!'
    else:
        a_color = '绿!'
    detail = df_name + '价格:' + df_price, '涨幅:' + str(round(df_percentage, 2)) + '%', a_color
    return detail, df_percentage


class work_thread(QThread):
    trigger = pyqtSignal(str)
    lock = QMutex()
    time = QDateTime.currentDateTime()
    time_format = time.toString("yyyy-MM-dd hh:mm:ss")

    def __init__(self):
        super(work_thread, self).__init__()

    def run(self):
        self.lock.lock()
        while True:
            sleep(2)
            try:
                data_1 = ui.lineEdit_1.text()
                data_2 = ui.lineEdit_2.text()
                data_shui = ts.get_realtime_quotes(data_1)
                data_lulu = ts.get_realtime_quotes(data_2)
                details1, df_percentages1 = data_frame(data_lulu)
                details, df_percentages = data_frame(data_shui)
                self.connect(str(details1))
                # self.trigger.emit(str(details1))
                print(details, details1)
                if df_percentages > 10.0 or df_percentages1 > 5.0:
                    tkinter.messagebox.showwarning('warning', '干')
            except Exception as e:
                print(e)
                continue
        self.lock.unlock()

    def connect(self, str_):
        self.time = QDateTime.currentDateTime()
        self.time_format = self.time.toString("yyyy-MM-dd hh:mm:ss")
        ui.listWidget_show_msg.addItem(str_ + " : " + self.time_format)
        ui.listWidget_show_msg.scrollToBottom()

    def graph(self):
        pg.plot()


class main_ui(QMainWindow, Ui_Stock_Monitoring):
    # time = QDateTime.currentDateTime()
    # time_format = time.toString("yyyy-MM-dd hh:mm:ss")

    def __init__(self):
        super(main_ui, self).__init__()
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "d")
        self.setupUi(self)
        self.work = work_thread()
        self.pushButton_search.clicked.connect(self.work_event)

    def work_event(self):
        self.work.start()
        # self.work.trigger.connect(self.con)

    # def con(self, str_):
    #     self.time = QDateTime.currentDateTime()
    #     self.time_format = self.time.toString("yyyy-MM-dd hh:mm:ss")
    #     self.listWidget.addItem(str_ + " : " + self.time_format)
    #     self.listWidget.scrollToBottom()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_ui()
    ui.show()
    sys.exit(app.exec_())
