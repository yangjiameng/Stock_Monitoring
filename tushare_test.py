import tushare as ts
import pandas as pd
from time import sleep
import datetime
import tkinter.messagebox
import tkinter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QMutex, QTimer, Qt, QDate, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
import qtawesome as qw
import pyqtgraph as pg
import numpy as np
import sys
import os
from Stock_Monitoring import config_rw
from Stock_Monitoring.StockUI import Ui_Stock_Monitoring
from Stock_Monitoring.up_down_stock_list import get_date

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
                if df_percentages > 10.0 or df_percentages1 > 10.0:
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
        self.csv_flag = True
        self.setWindowIcon(QIcon("Icons/main_icon.ico"))
        self.mouth_k = self.graphicsView_matplot.addPlot()
        self.daily_k = self.graphicsView_daily_line.addPlot(title="分时K线图")
        self.daily_k.setXRange(0, 240)
        self.arr_data = []
        self.line_list_time = [0]
        self.line_list_price = [40.18]
        self.process_value = 100 / 7200
        self.step = 100 / 7200
        self.pre_close = ''
        config_rw.config.read('message.ini')
        self.lineEdit_1.setText(config_rw.config['DEFAULT']['first_code'])
        self.lineEdit_2.setText(config_rw.config['DEFAULT']['second_code'])
        self.time_begin = datetime.datetime.now().strftime('%H%M')
        self.dateEdit_begin.setDate(QDate.fromString(config_rw.config['DEFAULT']['start_date'], "yyyyMMdd"))
        self.dateEdit_end.setDate(QDate.fromString(datetime.datetime.now().date().strftime("%Y%m%d"), "yyyyMMdd"))
        self.tabWidget.setCurrentIndex(1)
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
        # self.timer.timeout.connect(self.line)
        self.timer.timeout.connect(self.sell_and_buy_price_realtime)
        self.timer.start(2000)
        self.work = work_thread()
        self.comboBox.addItems(['--请选择--', '上海市场', '深圳市场'])
        self.slot_signal()

    def combobox_select(self):
        if self.comboBox.currentText() == '--请选择--':
            self.comboBox_2.clear()
            self.comboBox_3.clear()
        elif self.comboBox.currentText() == '上海市场':
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_2.addItems(self.read_csv(True, 2))
            self.comboBox_3.addItems(self.read_csv(True, 0))
        else:
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox_2.addItems(self.read_csv(False, 2))
            self.comboBox_3.addItems(self.read_csv(False, 0))

    def combobox2_select(self):
        index = self.comboBox_2.currentIndex()
        self.comboBox_3.setCurrentIndex(index)

    def slot_signal(self):
        self.comboBox.activated.connect(self.combobox_select)
        self.comboBox_2.activated.connect(self.combobox2_select)
        self.pushButton.clicked.connect(self.profit)
        self.pushButton_search.clicked.connect(self.work_event)
        self.pushButton_clear.clicked.connect(self.work_clear)
        self.pushButton_get_zd_data.clicked.connect(self.download_data)
        self.lineEdit_1.editingFinished.connect(self.k_plot)
        self.dateEdit_begin.dateChanged.connect(self.k_plot)
        self.dateEdit_end.dateChanged.connect(self.k_plot)
        self.menu_open.triggered.connect(self.open_excel)
        self.action_support.triggered.connect(self.support)

    def asd(self):
        print('1')

    def profit(self):
        self.listWidget_person_msg.clear()
        config_rw.config.read('message.ini')
        self.listWidget_person_msg.addItems(['今日盈亏' + ':' + config_rw.config['profit_message']['今日盈亏'],
                                             '资产剩余' + ':' + config_rw.config['profit_message']['资产剩余'],
                                             '总收益率' + ':' + config_rw.config['profit_message']['总收益率'],
                                             '持有公司' + ':' + config_rw.config['profit_message']['持有公司'],
                                             '持仓占比' + ':' + config_rw.config['profit_message']['持仓占比'],
                                             '投资风格' + ':' + config_rw.config['profit_message']['投资风格']])

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
        # self.lineEdit_1.hasFocus()
        self.mouth_k.clear()
        self.mouth_k.setLabel("bottom", "Time/(min)")
        self.mouth_k.setLabel("left", "Increase/(%)")
        code = self.lineEdit_1.text()
        start = self.dateEdit_begin.date().toString("yyyyMMdd")
        end = self.dateEdit_end.date().toString("yyyyMMdd")
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
        self.work.start()

    def work_clear(self):
        self.listWidget_show_msg.clear()

    def read_csv(self, csv_flag, i):
        if csv_flag:
            csv_data = pd.read_csv('Listed_company_msg/tushare_stock_basic_SH.csv', usecols=[i])
        else:
            csv_data = pd.read_csv('Listed_company_msg/tushare_stock_basic_SZ.csv', usecols=[i])
        arr = np.array(csv_data)
        self.arr_data = arr.flatten()
        return self.arr_data

    def sell_and_buy_price_realtime(self):
        try:
            data = ts.get_realtime_quotes('000815')
            sell_buy_amount = []
            df = pd.DataFrame(data=data)
            self.pre_close = df.loc[0, 'pre_close']
            self.lcdNumber_current_price.display(format(float(df.loc[0, 'price']), '.2f'))
            sell_buy_amount.append((df.loc[0, 'a1_v'], df.loc[0, 'a2_v'], df.loc[0, 'a3_v'],
                                    df.loc[0, 'a4_v'], df.loc[0, 'a5_v']))
            sell_buy_amount.append((df.loc[0, 'b1_v'], df.loc[0, 'b2_v'], df.loc[0, 'b3_v'],
                                    df.loc[0, 'b4_v'], df.loc[0, 'b5_v']))
            sell_buy_amount.append((df.loc[0, 'a1_p'], df.loc[0, 'a2_p'], df.loc[0, 'a3_p'],
                                    df.loc[0, 'a4_p'], df.loc[0, 'a5_p']))
            sell_buy_amount.append((df.loc[0, 'b1_p'], df.loc[0, 'b2_p'], df.loc[0, 'b3_p'],
                                    df.loc[0, 'b4_p'], df.loc[0, 'b5_p']))
            self.label_sell1.setText('卖1    ' + format(float(sell_buy_amount[2][0]), '.2f'))
            self.label_sell2.setText('卖2    ' + format(float(sell_buy_amount[2][1]), '.2f'))
            self.label_sell3.setText('卖3    ' + format(float(sell_buy_amount[2][2]), '.2f'))
            self.label_sell4.setText('卖4    ' + format(float(sell_buy_amount[2][3]), '.2f'))
            self.label_sell5.setText('卖5    ' + format(float(sell_buy_amount[2][4]), '.2f'))
            self.label_buy1.setText('买1    ' + format(float(sell_buy_amount[3][0]), '.2f'))
            self.label_buy2.setText('买2    ' + format(float(sell_buy_amount[3][1]), '.2f'))
            self.label_buy3.setText('买3    ' + format(float(sell_buy_amount[3][2]), '.2f'))
            self.label_buy4.setText('买4    ' + format(float(sell_buy_amount[3][3]), '.2f'))
            self.label_buy5.setText('买5    ' + format(float(sell_buy_amount[3][4]), '.2f'))
            label_sb = [self.label_s1, self.label_s2, self.label_s3, self.label_s4, self.label_s5,
                        self.label_b1, self.label_b2, self.label_b3, self.label_b4, self.label_b5]
            value_sb = [sell_buy_amount[0][0], sell_buy_amount[0][1], sell_buy_amount[0][2],
                        sell_buy_amount[0][3], sell_buy_amount[0][4], sell_buy_amount[1][0],
                        sell_buy_amount[1][1], sell_buy_amount[1][2], sell_buy_amount[1][3],
                        sell_buy_amount[1][4]]
            for i in range(0, 10):
                if value_sb[i] == '':
                    label_sb[i].setText('0')
                else:
                    c = int(value_sb[i])
                    if c >= 10000:
                        label_sb[i].setText(str(round(c / 10000, 2)) + '万')
                    else:
                        label_sb[i].setText(value_sb[i])
            self.max_value(sell_buy_amount)
        except Exception as e:
            print(e)

    def max_value(self, sell_buy_amount):
        max_list = []
        price_list = []
        value_len = [self.progressBar_s1, self.progressBar_s2, self.progressBar_s3,
                     self.progressBar_s4, self.progressBar_s5,
                     self.progressBar_b1, self.progressBar_b2, self.progressBar_b3,
                     self.progressBar_b4, self.progressBar_b5]
        for i in range(0, 2):
            for j in range(0, 5):
                if sell_buy_amount[i][j] == '':
                    max_list.append(0)
                else:
                    max_list.append(int(sell_buy_amount[i][j]))
        for h in range(2, 4):
            for g in range(0, 5):
                price_list.append(float(sell_buy_amount[h][g]))
        num = max(max_list)
        for k in range(0, 10):
            value_len[k].setValue(int(100 * max_list[k] / num))
            if price_list[k] < float(self.pre_close):
                value_len[k].setStyleSheet('')
            else:
                value_len[k].setStyleSheet('QProgressBar::chunk {background-color: rgb(255, 0, 0);}')

    def download_data(self):
        get_date()
        self.listWidget_show_msg.addItem('今日涨跌停数据下载成功！')

    def open_excel(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls , *.csv)')
        if openfile_name[0] != '':
            os.startfile(openfile_name[0])
            print(openfile_name[0])

    def support(self):
        QDesktopServices.openUrl(QUrl('https://github.com/yangjiameng/Stock_Monitoring'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_ui()
    ui.show()
    sys.exit(app.exec_())
