import tushare as ts
import pandas as pd
from time import sleep
import datetime
import tkinter.messagebox
import tkinter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QMutex, QTimer
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import sys
from Stock_Monitoring import config_rw
from Stock_Monitoring.StockUI import Ui_Stock_Monitoring

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


def ts_pro_api(code, start, end):
    result_open_red = []
    result_close_red = []
    result_open_green = []
    result_close_green = []
    result_date_red = []
    result_date_green = []
    result_high_red = []
    result_low_red = []
    result_high_green = []
    result_low_green = []
    if code[0] == '0':
        suffix = '.SZ'
    else:
        suffix = '.SH'
    pro = ts.pro_api(token)
    data = pro.daily(ts_code=code + suffix, start_date=start, end_date=end)
    df = pd.DataFrame(data)
    for i in range(0, df.shape[0]):
        df_close = df.loc[i, 'close']
        df_open = df.loc[i, 'open']
        df_high = df.loc[i, 'high']
        df_low = df.loc[i, 'low']
        if df_close - df_open >= 0:
            result_open_red.append(df_open)
            result_close_red.append(df_close - df_open)
            result_high_red.append(df_high)
            result_low_red.append(df_low)
            result_date_red.append(df.shape[0] - i)
        else:
            result_open_green.append(df_open)
            result_close_green.append(df_close - df_open)
            result_high_green.append(df_high)
            result_low_green.append(df_low)
            result_date_green.append(df.shape[0] - i)
    return result_open_red, result_close_red, result_date_red, result_open_green, result_close_green, \
        result_date_green, result_high_red, result_low_red, result_high_green, result_low_green


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

    pg.setConfigOption("background", "w")
    pg.setConfigOption("foreground", "k")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = True
        self.setWindowIcon(QIcon("Icons/main_icon.ico"))
        self.mouth_k = self.graphicsView_matplot.addPlot(title="30K线图")
        self.daily_k = self.graphicsView_daily_line.addPlot(title="分时K线图")
        self.daily_k.setXRange(0, 240)
        self.line_list_time = [0]
        self.line_list_price = [40.18]
        self.process_value = 100 / 7200
        self.step = 100 / 7200
        self.time_begin = datetime.datetime.now().strftime('%H%M')
        if '0930' <= self.time_begin <= '1130':
            self.process_value = (int(self.time_begin) - 930) * 30 * self.step
            self.progressBar_stock.setValue(int(self.process_value))
        elif '1300' <= self.time_begin <= '1500':
            self.process_value = (int(self.time_begin) - 1180) * 30 * self.step
            self.progressBar_stock.setValue(int(self.process_value))
        self.time_begin = '0000'
        self.time_flag = '0000'
        self.doubleSpinBox_my_money.setValue(config_rw.config_read())
        self.k_plot()
        self.timer = QTimer()
        self.timer.timeout.connect(self.line)
        self.timer.start(2000)
        self.work = work_thread()
        self.comboBox.addItems(['--请选择--', '深圳市场', '上海市场'])
        self.slot_signal()

    def slot_signal(self):
        self.pushButton_search.clicked.connect(self.work_event)
        self.pushButton_clear.clicked.connect(self.work_clear)
        self.lineEdit_1.textChanged.connect(self.k_plot)
        self.lineEdit_3.textChanged.connect(self.k_plot)
        self.lineEdit_4.textChanged.connect(self.k_plot)

    def line(self):
        self.time_begin = datetime.datetime.now().strftime('%H%M')
        if '0930' <= self.time_begin <= '1130' or '1300' <= self.time_begin <= '1500':
            self.progressBar_stock.setValue(int(self.process_value))
            self.process_value += self.step
            self.daily_k.clear()
            data_pan = ts.get_realtime_quotes(self.lineEdit_2.text())
            data_pd = pd.DataFrame(data_pan)
            price = float(data_pd.loc[0, 'price'])
            if self.time_begin == self.time_flag:
                self.line_list_price[-1] = price
            else:
                self.line_list_price.append(price)
                # self.line_list_time.append(int(self.time_flag))
                self.time_flag = self.time_begin
            self.daily_k.setLabel("bottom", "Time/(h:s)")
            self.daily_k.setLabel("left", "Price/(¥)")
            self.daily_k.plot(fillLevel=40.18, brush=(50, 50, 200, 100)).setData(pen=pg.mkPen(color='r', width=2),
                                                                                 y=self.line_list_price)
            self.daily_k.showGrid(y=True)

    def k_plot(self):
        self.mouth_k.clear()
        self.mouth_k.setLabel("bottom", "Time/(min)")
        self.mouth_k.setLabel("left", "Increase/(%)")
        code = self.lineEdit_1.text()
        start = self.lineEdit_3.text()
        end = self.lineEdit_4.text()
        open_price_r, close_price_r, date_r, open_price_g, close_price_g, date_g, high_r, \
            low_r, high_g, low_g = ts_pro_api(code, start, end)
        bg1 = pg.BarGraphItem(y0=open_price_r, x=date_r, height=close_price_r, width=0.3, brush='r')
        bg2 = pg.BarGraphItem(y0=open_price_g, x=date_g, height=close_price_g, width=0.3, brush='g')
        for i in range(0, len(date_r)):
            self.mouth_k.plot(pen=pg.mkPen(color='r', width=2), x=[date_r[i], date_r[i]], y=[low_r[i], high_r[i]])
        for j in range(0, len(date_g)):
            self.mouth_k.plot(pen=pg.mkPen(color='g', width=2), x=[date_g[j], date_g[j]], y=[low_g[j], high_g[j]])
        self.mouth_k.addItem(bg1)
        self.mouth_k.addItem(bg2)
        self.mouth_k.showGrid(y=True)

    def work_event(self):
        if self.flag:
            self.work.start()
            # self.flag = False
        else:
            self.work.wait()
            self.flag = True

    def work_clear(self):
        self.listWidget_show_msg.clear()

    def read_csv(self):
        self.csv_SH = pd.read_csv('Listed_company_msg/tushare_stock_basic_SH.csv')
        self.csv_SZ = pd.read_csv('Listed_company_msg/tushare_stock_basic_SZ.csv')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_ui()
    ui.show()
    sys.exit(app.exec_())
