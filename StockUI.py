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
        Stock_Monitoring.resize(866, 661)
        Stock_Monitoring.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Stock_Monitoring)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progressBar_stock = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_stock.setProperty("value", 100)
        self.progressBar_stock.setObjectName("progressBar_stock")
        self.gridLayout_3.addWidget(self.progressBar_stock, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
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
        self.groupBox_realtime = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_realtime.setObjectName("groupBox_realtime")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_realtime)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listWidget_show_msg = QtWidgets.QListWidget(self.groupBox_realtime)
        self.listWidget_show_msg.setObjectName("listWidget_show_msg")
        self.gridLayout_6.addWidget(self.listWidget_show_msg, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_realtime, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 2, 2, 1, 1)
        self.groupBox_stock = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_stock.setObjectName("groupBox_stock")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_stock)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_stock)
        self.pushButton_clear.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 6, 2, 1, 1)
        self.dateEdit_end = QtWidgets.QDateEdit(self.groupBox_stock)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.gridLayout.addWidget(self.dateEdit_end, 4, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 2, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 1)
        self.dateEdit_begin = QtWidgets.QDateEdit(self.groupBox_stock)
        self.dateEdit_begin.setObjectName("dateEdit_begin")
        self.gridLayout.addWidget(self.dateEdit_begin, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_stock)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_stock)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_stock)
        self.pushButton_search.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_search.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_stock)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_stock)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_stock, 0, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 11, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 3, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
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
        Stock_Monitoring.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stock_Monitoring)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 23))
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
        self.menu_file.addAction(self.menu_new)
        self.menu_edit.addAction(self.menu_select)
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
        self.label_5.setText(_translate("Stock_Monitoring", "进度"))
        self.groupBox.setTitle(_translate("Stock_Monitoring", "我的盈亏信息"))
        self.label_6.setText(_translate("Stock_Monitoring", "我的本金"))
        self.pushButton.setText(_translate("Stock_Monitoring", "收益计算"))
        self.checkBox_remember.setText(_translate("Stock_Monitoring", "记住我"))
        self.radioButton_2.setText(_translate("Stock_Monitoring", "减持"))
        self.radioButton.setText(_translate("Stock_Monitoring", "增持"))
        self.label_7.setText(_translate("Stock_Monitoring", "增减仓位"))
        self.groupBox_realtime.setTitle(_translate("Stock_Monitoring", "即时信息"))
        self.groupBox_stock.setTitle(_translate("Stock_Monitoring", "股票代码"))
        self.lineEdit_1.setText(_translate("Stock_Monitoring", "600733"))
        self.lineEdit_2.setText(_translate("Stock_Monitoring", "600111"))
        self.pushButton_clear.setText(_translate("Stock_Monitoring", "清空"))
        self.lineEdit_4.setText(_translate("Stock_Monitoring", "20210818"))
        self.lineEdit_4.setPlaceholderText(_translate("Stock_Monitoring", "结束日期"))
        self.lineEdit_3.setText(_translate("Stock_Monitoring", "20210801"))
        self.lineEdit_3.setPlaceholderText(_translate("Stock_Monitoring", "开始日期"))
        self.label_3.setText(_translate("Stock_Monitoring", "主代码"))
        self.label_2.setText(_translate("Stock_Monitoring", "结束日期"))
        self.pushButton_search.setText(_translate("Stock_Monitoring", "获取"))
        self.label.setText(_translate("Stock_Monitoring", "开始日期"))
        self.label_4.setText(_translate("Stock_Monitoring", "副代码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_daily), _translate("Stock_Monitoring", "日走势图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_30_K), _translate("Stock_Monitoring", "30日K线图"))
        self.menu_file.setTitle(_translate("Stock_Monitoring", "文件"))
        self.menu_edit.setTitle(_translate("Stock_Monitoring", "编辑"))
        self.menu_set.setTitle(_translate("Stock_Monitoring", "设置"))
        self.menu_help.setTitle(_translate("Stock_Monitoring", "帮助"))
        self.menu_new.setText(_translate("Stock_Monitoring", "新建"))
        self.menu_select.setText(_translate("Stock_Monitoring", "选择"))
from pyqtgraph import GraphicsLayoutWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stock_Monitoring = QtWidgets.QMainWindow()
    ui = Ui_Stock_Monitoring()
    ui.setupUi(Stock_Monitoring)
    Stock_Monitoring.show()
    sys.exit(app.exec_())
