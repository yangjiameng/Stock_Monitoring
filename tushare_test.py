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

token = '8c393a8010030c17c6c93bcc4d798cc2d9e8ecbf7e082a32980b1b97'


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


def ts_pro_api():
    result_open_red = []
    result_close_red = []
    result_open_green = []
    result_close_green = []
    result_date_red = []
    result_date_green = []
    pro = ts.pro_api(token)
    data = pro.daily(ts_code='000848.SZ', start_date='20210701', end_date='20210813')
    df = pd.DataFrame(data)
    for i in range(0, df.shape[0]):
        df_close = df.loc[i, 'change']
        df_open = df.loc[i, 'pre_close']
        if df_close >= 0:
            result_open_red.append(df_open)
            result_close_red.append(df_close)
            result_date_red.append(df.shape[0] - i)
        else:
            result_open_green.append(df_open)
            result_close_green.append(df_close)
            result_date_green.append(df.shape[0] - i)
    # result_open_green.reverse()
    # result_close_green.reverse()
    # # result_open_red.reverse()
    # result_close_red.reverse()
    return result_open_red, result_close_red, result_date_red, result_open_green, result_close_green, result_date_green


class work_thread(QThread):
    trigger = pyqtSignal(float)
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
                self.trigger.emit(df_percentages1)
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

    def __init__(self):
        super().__init__()
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        self.setupUi(self)
        self.k_plot()
        self.work = work_thread()
        self.pushButton_search.clicked.connect(self.work_event)

    def line(self):
        self.graphicsView_matplot.addPlot(title="分时K线图", y=[1, 2, 3], pen=pg.mkPen(color='r', width=2))

    def k_plot(self):
        plt = self.graphicsView_matplot.addPlot(title="K线图")
        plt.setLabel("bottom", "Time/(min)")
        plt.setLabel("left", "Increase/(%)")
        open_price_r, close_price_r, date_r, open_price_g, close_price_g, date_g = ts_pro_api()
        bg1 = pg.BarGraphItem(y0=open_price_r, x=date_r, height=close_price_r, width=0.3, brush='r')
        bg2 = pg.BarGraphItem(y0=open_price_g, x=date_g, height=close_price_g, width=0.3, brush='g')
        plt.addItem(bg1)
        plt.addItem(bg2)
        plt.showGrid(y=True)

    def work_event(self):
        self.work.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_ui()
    ui.show()
    sys.exit(app.exec_())
