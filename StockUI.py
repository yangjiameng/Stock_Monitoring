# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stock_Monitoring(object):
    def setupUi(self, Stock_Monitoring):
        Stock_Monitoring.setObjectName("Stock_Monitoring")
        Stock_Monitoring.resize(873, 651)
        Stock_Monitoring.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Stock_Monitoring)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progressBar_stock = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_stock.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_stock.setStyleSheet("")
        self.progressBar_stock.setProperty("value", 80)
        self.progressBar_stock.setTextVisible(False)
        self.progressBar_stock.setObjectName("progressBar_stock")
        self.gridLayout_3.addWidget(self.progressBar_stock, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.listWidget_zd_msg = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_zd_msg.setObjectName("listWidget_zd_msg")
        self.gridLayout_9.addWidget(self.listWidget_zd_msg, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_daily_up = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_daily_up.setObjectName("groupBox_daily_up")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_daily_up)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_daily_up)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_daily_up)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_daily_up)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.pushButton_get_zd_data = QtWidgets.QPushButton(self.groupBox_daily_up)
        self.pushButton_get_zd_data.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_get_zd_data.setObjectName("pushButton_get_zd_data")
        self.horizontalLayout.addWidget(self.pushButton_get_zd_data)
        self.gridLayout_2.addWidget(self.groupBox_daily_up, 1, 0, 1, 2)
        self.groupBox_stock = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_stock.setObjectName("groupBox_stock")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_stock)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEdit_begin = QtWidgets.QDateEdit(self.groupBox_stock)
        self.dateEdit_begin.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 10, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_begin.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.dateEdit_begin.setMinimumDate(QtCore.QDate(2008, 1, 1))
        self.dateEdit_begin.setCalendarPopup(True)
        self.dateEdit_begin.setObjectName("dateEdit_begin")
        self.gridLayout.addWidget(self.dateEdit_begin, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_stock)
        self.pushButton_search.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_search.setStyleSheet("")
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_2.addWidget(self.pushButton_search)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_stock)
        self.pushButton_clear.setStyleSheet("")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_2.addWidget(self.pushButton_clear)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 4, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_stock)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_stock)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_stock)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_stock)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.dateEdit_end = QtWidgets.QDateEdit(self.groupBox_stock)
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 10, 13), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.dateEdit_end.setMinimumDate(QtCore.QDate(2008, 1, 1))
        self.dateEdit_end.setCalendarPopup(True)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.gridLayout.addWidget(self.dateEdit_end, 4, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_stock, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_daily = QtWidgets.QWidget()
        self.tab_daily.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_daily.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab_daily.setObjectName("tab_daily")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_daily)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView_daily_line = GraphicsLayoutWidget(self.tab_daily)
        self.graphicsView_daily_line.setObjectName("graphicsView_daily_line")
        self.gridLayout_4.addWidget(self.graphicsView_daily_line, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_daily, "")
        self.tab_30_K = QtWidgets.QWidget()
        self.tab_30_K.setObjectName("tab_30_K")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_30_K)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphicsView_matplot = GraphicsLayoutWidget(self.tab_30_K)
        self.graphicsView_matplot.setObjectName("graphicsView_matplot")
        self.gridLayout_5.addWidget(self.graphicsView_matplot, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_30_K, "")
        self.gridLayout_3.addWidget(self.tabWidget, 3, 1, 2, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_7.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.listWidget_person_msg = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_person_msg.setObjectName("listWidget_person_msg")
        self.gridLayout_7.addWidget(self.listWidget_person_msg, 2, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 0, 4, 1, 1)
        self.checkBox_remember = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_remember.setObjectName("checkBox_remember")
        self.gridLayout_7.addWidget(self.checkBox_remember, 0, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_7.addWidget(self.radioButton_2, 1, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_7.addWidget(self.radioButton, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 3, 1, 1)
        self.doubleSpinBox_my_money = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_my_money.setEnabled(True)
        self.doubleSpinBox_my_money.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_my_money.setMaximum(10000000.0)
        self.doubleSpinBox_my_money.setObjectName("doubleSpinBox_my_money")
        self.gridLayout_7.addWidget(self.doubleSpinBox_my_money, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.groupBox_realtime = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_realtime.setMaximumSize(QtCore.QSize(16777215, 240))
        self.groupBox_realtime.setObjectName("groupBox_realtime")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_realtime)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lcdNumber_current_price = QtWidgets.QLCDNumber(self.groupBox_realtime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.lcdNumber_current_price.sizePolicy().hasHeightForWidth())
        self.lcdNumber_current_price.setSizePolicy(sizePolicy)
        self.lcdNumber_current_price.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lcdNumber_current_price.setFont(font)
        self.lcdNumber_current_price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdNumber_current_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.lcdNumber_current_price.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_current_price.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_current_price.setLineWidth(1)
        self.lcdNumber_current_price.setSmallDecimalPoint(False)
        self.lcdNumber_current_price.setDigitCount(6)
        self.lcdNumber_current_price.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_current_price.setProperty("value", 0.0)
        self.lcdNumber_current_price.setObjectName("lcdNumber_current_price")
        self.gridLayout_6.addWidget(self.lcdNumber_current_price, 1, 1, 1, 1)
        self.listWidget_show_msg = QtWidgets.QListWidget(self.groupBox_realtime)
        self.listWidget_show_msg.setMaximumSize(QtCore.QSize(16777215, 80))
        self.listWidget_show_msg.setObjectName("listWidget_show_msg")
        self.gridLayout_6.addWidget(self.listWidget_show_msg, 0, 0, 1, 2)
        self.label_name = QtWidgets.QLabel(self.groupBox_realtime)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_name.setAutoFillBackground(False)
        self.label_name.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_name.setText("")
        self.label_name.setWordWrap(False)
        self.label_name.setObjectName("label_name")
        self.gridLayout_6.addWidget(self.label_name, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_realtime, 1, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.progressBar_b3 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_b3.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_b3.setStyleSheet("")
        self.progressBar_b3.setProperty("value", 50)
        self.progressBar_b3.setTextVisible(False)
        self.progressBar_b3.setObjectName("progressBar_b3")
        self.gridLayout_8.addWidget(self.progressBar_b3, 3, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_8.addWidget(self.line, 1, 3, 5, 1)
        self.label_s2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_s2.setObjectName("label_s2")
        self.gridLayout_8.addWidget(self.label_s2, 2, 2, 1, 1)
        self.label_b2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_b2.setObjectName("label_b2")
        self.gridLayout_8.addWidget(self.label_b2, 2, 6, 1, 1)
        self.label_b1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_b1.setObjectName("label_b1")
        self.gridLayout_8.addWidget(self.label_b1, 1, 6, 1, 1)
        self.label_sell5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_sell5.setObjectName("label_sell5")
        self.gridLayout_8.addWidget(self.label_sell5, 5, 0, 1, 1)
        self.label_s1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_s1.setObjectName("label_s1")
        self.gridLayout_8.addWidget(self.label_s1, 1, 2, 1, 1)
        self.progressBar_b1 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_b1.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_b1.setStyleSheet("")
        self.progressBar_b1.setProperty("value", 50)
        self.progressBar_b1.setTextVisible(False)
        self.progressBar_b1.setObjectName("progressBar_b1")
        self.gridLayout_8.addWidget(self.progressBar_b1, 1, 5, 1, 1)
        self.label_sell2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_sell2.setObjectName("label_sell2")
        self.gridLayout_8.addWidget(self.label_sell2, 2, 0, 1, 1)
        self.label_sell1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_sell1.setObjectName("label_sell1")
        self.gridLayout_8.addWidget(self.label_sell1, 1, 0, 1, 1)
        self.label_buy3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_buy3.setObjectName("label_buy3")
        self.gridLayout_8.addWidget(self.label_buy3, 3, 4, 1, 1)
        self.label_buy4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_buy4.setObjectName("label_buy4")
        self.gridLayout_8.addWidget(self.label_buy4, 4, 4, 1, 1)
        self.progressBar_s4 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_s4.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_s4.setStyleSheet("")
        self.progressBar_s4.setProperty("value", 50)
        self.progressBar_s4.setTextVisible(False)
        self.progressBar_s4.setObjectName("progressBar_s4")
        self.gridLayout_8.addWidget(self.progressBar_s4, 4, 1, 1, 1)
        self.progressBar_s5 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_s5.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_s5.setStyleSheet("")
        self.progressBar_s5.setProperty("value", 50)
        self.progressBar_s5.setTextVisible(False)
        self.progressBar_s5.setObjectName("progressBar_s5")
        self.gridLayout_8.addWidget(self.progressBar_s5, 5, 1, 1, 1)
        self.label_buy2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_buy2.setObjectName("label_buy2")
        self.gridLayout_8.addWidget(self.label_buy2, 2, 4, 1, 1)
        self.label_sell3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_sell3.setObjectName("label_sell3")
        self.gridLayout_8.addWidget(self.label_sell3, 3, 0, 1, 1)
        self.label_buy1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_buy1.setObjectName("label_buy1")
        self.gridLayout_8.addWidget(self.label_buy1, 1, 4, 1, 1)
        self.label_b4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_b4.setObjectName("label_b4")
        self.gridLayout_8.addWidget(self.label_b4, 4, 6, 1, 1)
        self.progressBar_s3 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_s3.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_s3.setStyleSheet("")
        self.progressBar_s3.setProperty("value", 50)
        self.progressBar_s3.setTextVisible(False)
        self.progressBar_s3.setObjectName("progressBar_s3")
        self.gridLayout_8.addWidget(self.progressBar_s3, 3, 1, 1, 1)
        self.progressBar_s1 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_s1.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_s1.setStyleSheet("")
        self.progressBar_s1.setProperty("value", 50)
        self.progressBar_s1.setTextVisible(False)
        self.progressBar_s1.setObjectName("progressBar_s1")
        self.gridLayout_8.addWidget(self.progressBar_s1, 1, 1, 1, 1)
        self.label_s5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_s5.setObjectName("label_s5")
        self.gridLayout_8.addWidget(self.label_s5, 5, 2, 1, 1)
        self.label_buy5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_buy5.setObjectName("label_buy5")
        self.gridLayout_8.addWidget(self.label_buy5, 5, 4, 1, 1)
        self.label_s4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_s4.setObjectName("label_s4")
        self.gridLayout_8.addWidget(self.label_s4, 4, 2, 1, 1)
        self.progressBar_s2 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_s2.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_s2.setStyleSheet("")
        self.progressBar_s2.setProperty("value", 50)
        self.progressBar_s2.setTextVisible(False)
        self.progressBar_s2.setObjectName("progressBar_s2")
        self.gridLayout_8.addWidget(self.progressBar_s2, 2, 1, 1, 1)
        self.label_b5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_b5.setObjectName("label_b5")
        self.gridLayout_8.addWidget(self.label_b5, 5, 6, 1, 1)
        self.progressBar_b4 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_b4.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_b4.setStyleSheet("")
        self.progressBar_b4.setProperty("value", 50)
        self.progressBar_b4.setTextVisible(False)
        self.progressBar_b4.setObjectName("progressBar_b4")
        self.gridLayout_8.addWidget(self.progressBar_b4, 4, 5, 1, 1)
        self.label_b3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_b3.setObjectName("label_b3")
        self.gridLayout_8.addWidget(self.label_b3, 3, 6, 1, 1)
        self.progressBar_b2 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_b2.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_b2.setStyleSheet("")
        self.progressBar_b2.setProperty("value", 50)
        self.progressBar_b2.setTextVisible(False)
        self.progressBar_b2.setObjectName("progressBar_b2")
        self.gridLayout_8.addWidget(self.progressBar_b2, 2, 5, 1, 1)
        self.label_s3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_s3.setObjectName("label_s3")
        self.gridLayout_8.addWidget(self.label_s3, 3, 2, 1, 1)
        self.progressBar_b5 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_b5.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar_b5.setStyleSheet("")
        self.progressBar_b5.setProperty("value", 50)
        self.progressBar_b5.setTextVisible(False)
        self.progressBar_b5.setObjectName("progressBar_b5")
        self.gridLayout_8.addWidget(self.progressBar_b5, 5, 5, 1, 1)
        self.label_sell4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_sell4.setObjectName("label_sell4")
        self.gridLayout_8.addWidget(self.label_sell4, 4, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 1, 1, 2)
        Stock_Monitoring.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stock_Monitoring)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_set = QtWidgets.QMenu(self.menubar)
        self.menu_set.setObjectName("menu_set")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        Stock_Monitoring.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stock_Monitoring)
        self.statusbar.setObjectName("statusbar")
        Stock_Monitoring.setStatusBar(self.statusbar)
        self.menu_new = QtWidgets.QAction(Stock_Monitoring)
        self.menu_new.setObjectName("menu_new")
        self.menu_select = QtWidgets.QAction(Stock_Monitoring)
        self.menu_select.setObjectName("menu_select")
        self.menu_open = QtWidgets.QAction(Stock_Monitoring)
        self.menu_open.setObjectName("menu_open")
        self.action_support = QtWidgets.QAction(Stock_Monitoring)
        self.action_support.setShortcut("")
        self.action_support.setObjectName("action_support")
        self.action_about = QtWidgets.QAction(Stock_Monitoring)
        self.action_about.setObjectName("action_about")
        self.menu_file.addAction(self.menu_new)
        self.menu_file.addAction(self.menu_open)
        self.menu_edit.addAction(self.menu_select)
        self.menu_help.addAction(self.action_support)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_set.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(Stock_Monitoring)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Stock_Monitoring)

    def retranslateUi(self, Stock_Monitoring):
        _translate = QtCore.QCoreApplication.translate
        Stock_Monitoring.setWindowTitle(_translate("Stock_Monitoring", "Stock_Monitoring"))
        self.groupBox_3.setTitle(_translate("Stock_Monitoring", "涨跌基本信息"))
        self.groupBox_daily_up.setTitle(_translate("Stock_Monitoring", "每日涨跌停统计 "))
        self.pushButton_get_zd_data.setText(_translate("Stock_Monitoring", "获取数据"))
        self.groupBox_stock.setTitle(_translate("Stock_Monitoring", "股票代码"))
        self.dateEdit_begin.setDisplayFormat(_translate("Stock_Monitoring", "yyyy/MM/dd"))
        self.pushButton_search.setText(_translate("Stock_Monitoring", "获取"))
        self.pushButton_clear.setText(_translate("Stock_Monitoring", "清空"))
        self.lineEdit_1.setText(_translate("Stock_Monitoring", "600733"))
        self.lineEdit_2.setText(_translate("Stock_Monitoring", "600111"))
        self.label_4.setText(_translate("Stock_Monitoring", "自选二"))
        self.label.setText(_translate("Stock_Monitoring", "开始日期"))
        self.label_3.setText(_translate("Stock_Monitoring", "自选一"))
        self.label_2.setText(_translate("Stock_Monitoring", "结束日期"))
        self.dateEdit_end.setDisplayFormat(_translate("Stock_Monitoring", "yyyy/MM/dd"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_daily), _translate("Stock_Monitoring", "日走势图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_30_K), _translate("Stock_Monitoring", "30日K线图"))
        self.groupBox.setTitle(_translate("Stock_Monitoring", "我的盈亏信息"))
        self.label_6.setText(_translate("Stock_Monitoring", "我的本金"))
        self.pushButton.setText(_translate("Stock_Monitoring", "收益计算"))
        self.checkBox_remember.setText(_translate("Stock_Monitoring", "记住我"))
        self.radioButton_2.setText(_translate("Stock_Monitoring", "减持"))
        self.radioButton.setText(_translate("Stock_Monitoring", "增持"))
        self.label_7.setText(_translate("Stock_Monitoring", "增减仓位"))
        self.label_5.setText(_translate("Stock_Monitoring", "进度"))
        self.groupBox_realtime.setTitle(_translate("Stock_Monitoring", "即时信息"))
        self.groupBox_2.setTitle(_translate("Stock_Monitoring", "实时委托详情"))
        self.label_s2.setText(_translate("Stock_Monitoring", "0"))
        self.label_b2.setText(_translate("Stock_Monitoring", "0"))
        self.label_b1.setText(_translate("Stock_Monitoring", "0"))
        self.label_sell5.setText(_translate("Stock_Monitoring", "卖5   0"))
        self.label_s1.setText(_translate("Stock_Monitoring", "0"))
        self.label_sell2.setText(_translate("Stock_Monitoring", "卖2   0"))
        self.label_sell1.setText(_translate("Stock_Monitoring", "卖1   0"))
        self.label_buy3.setText(_translate("Stock_Monitoring", "买3   0"))
        self.label_buy4.setText(_translate("Stock_Monitoring", "买4   0"))
        self.label_buy2.setText(_translate("Stock_Monitoring", "买2   0"))
        self.label_sell3.setText(_translate("Stock_Monitoring", "卖3   0"))
        self.label_buy1.setText(_translate("Stock_Monitoring", "买1   0"))
        self.label_b4.setText(_translate("Stock_Monitoring", "0"))
        self.label_s5.setText(_translate("Stock_Monitoring", "0"))
        self.label_buy5.setText(_translate("Stock_Monitoring", "买5   0"))
        self.label_s4.setText(_translate("Stock_Monitoring", "0"))
        self.label_b5.setText(_translate("Stock_Monitoring", "0"))
        self.label_b3.setText(_translate("Stock_Monitoring", "0"))
        self.label_s3.setText(_translate("Stock_Monitoring", "0"))
        self.label_sell4.setText(_translate("Stock_Monitoring", "卖4   0"))
        self.menu_file.setTitle(_translate("Stock_Monitoring", "文件"))
        self.menu_edit.setTitle(_translate("Stock_Monitoring", "编辑"))
        self.menu_set.setTitle(_translate("Stock_Monitoring", "设置"))
        self.menu_help.setTitle(_translate("Stock_Monitoring", "帮助"))
        self.menu_new.setText(_translate("Stock_Monitoring", "新建"))
        self.menu_new.setShortcut(_translate("Stock_Monitoring", "Ctrl+N"))
        self.menu_select.setText(_translate("Stock_Monitoring", "选择"))
        self.menu_open.setText(_translate("Stock_Monitoring", "打开"))
        self.action_support.setText(_translate("Stock_Monitoring", "联系支持"))
        self.action_about.setText(_translate("Stock_Monitoring", "关于"))
from pyqtgraph import GraphicsLayoutWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stock_Monitoring = QtWidgets.QMainWindow()
    ui = Ui_Stock_Monitoring()
    ui.setupUi(Stock_Monitoring)
    Stock_Monitoring.show()
    sys.exit(app.exec_())
