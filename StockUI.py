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
        Stock_Monitoring.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Stock_Monitoring)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 0, 1, 1, 1)
        Stock_Monitoring.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stock_Monitoring)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        Stock_Monitoring.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stock_Monitoring)
        self.statusbar.setObjectName("statusbar")
        Stock_Monitoring.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(Stock_Monitoring)
        self.pushButton.clicked.connect(Stock_Monitoring.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(Stock_Monitoring)

    def retranslateUi(self, Stock_Monitoring):
        _translate = QtCore.QCoreApplication.translate
        Stock_Monitoring.setWindowTitle(_translate("Stock_Monitoring", "Stock_Monitoring"))
        self.groupBox.setTitle(_translate("Stock_Monitoring", "股票代码"))
        self.pushButton.setText(_translate("Stock_Monitoring", "确定"))
        self.menu.setTitle(_translate("Stock_Monitoring", "文件"))
        self.menu_2.setTitle(_translate("Stock_Monitoring", "编辑"))
        self.menu_3.setTitle(_translate("Stock_Monitoring", "设置"))
        self.menu_4.setTitle(_translate("Stock_Monitoring", "帮助"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stock_Monitoring = QtWidgets.QMainWindow()
    ui = Ui_Stock_Monitoring()
    ui.setupUi(Stock_Monitoring)
    Stock_Monitoring.show()
    sys.exit(app.exec_())
