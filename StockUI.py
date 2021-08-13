# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget


class Ui_Stock_Monitoring(object):
    def setupUi(self, Stock_Monitoring):
        Stock_Monitoring.setObjectName("Stock_Monitoring")
        Stock_Monitoring.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Stock_Monitoring)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 2)
        self.groupBox_stock = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_stock.setObjectName("groupBox_stock")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_stock)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_stock)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_stock)
        self.pushButton_search.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_stock, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.listWidget_show_msg = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_show_msg.setObjectName("listWidget_show_msg")
        self.gridLayout_3.addWidget(self.listWidget_show_msg, 1, 2, 1, 1)
        self.graphicsView_matplot = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView_matplot.setObjectName("graphicsView_matplot")
        self.gridLayout_3.addWidget(self.graphicsView_matplot, 2, 2, 1, 1)
        Stock_Monitoring.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stock_Monitoring)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        QtCore.QMetaObject.connectSlotsByName(Stock_Monitoring)

    def retranslateUi(self, Stock_Monitoring):
        _translate = QtCore.QCoreApplication.translate
        Stock_Monitoring.setWindowTitle(_translate("Stock_Monitoring", "Stock_Monitoring"))
        self.groupBox_stock.setTitle(_translate("Stock_Monitoring", "股票代码"))
        self.lineEdit_2.setText(_translate("Stock_Monitoring", "600111"))
        self.lineEdit_1.setText(_translate("Stock_Monitoring", "000848"))
        self.lineEdit_4.setText(_translate("Stock_Monitoring", "xxxxxx"))
        self.lineEdit_3.setText(_translate("Stock_Monitoring", "xxxxxx"))
        self.pushButton_search.setText(_translate("Stock_Monitoring", "确定"))
        self.menu_file.setTitle(_translate("Stock_Monitoring", "文件"))
        self.menu_edit.setTitle(_translate("Stock_Monitoring", "编辑"))
        self.menu_set.setTitle(_translate("Stock_Monitoring", "设置"))
        self.menu_help.setTitle(_translate("Stock_Monitoring", "帮助"))
        self.menu_new.setText(_translate("Stock_Monitoring", "新建"))
        self.menu_select.setText(_translate("Stock_Monitoring", "选择"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Stock_Monitoring = QtWidgets.QMainWindow()
    ui = Ui_Stock_Monitoring()
    ui.setupUi(Stock_Monitoring)
    Stock_Monitoring.show()
    sys.exit(app.exec_())
