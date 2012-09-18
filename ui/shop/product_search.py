# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/shop/product_search.ui'
#
# Created: Tue Sep 18 21:56:41 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProductSearch(object):
    def setupUi(self, ProductSearch):
        ProductSearch.setObjectName(_fromUtf8("ProductSearch"))
        ProductSearch.setWindowModality(QtCore.Qt.ApplicationModal)
        ProductSearch.resize(500, 400)
        ProductSearch.setMinimumSize(QtCore.QSize(500, 400))
        ProductSearch.setMaximumSize(QtCore.QSize(500, 400))
        self.gridLayout = QtGui.QGridLayout(ProductSearch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rearch_text = QtGui.QLineEdit(ProductSearch)
        self.rearch_text.setObjectName(_fromUtf8("rearch_text"))
        self.gridLayout.addWidget(self.rearch_text, 2, 1, 1, 1)
        self.result_table = QtGui.QTableWidget(ProductSearch)
        self.result_table.setMinimumSize(QtCore.QSize(482, 0))
        self.result_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.result_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.result_table.setObjectName(_fromUtf8("result_table"))
        self.result_table.setColumnCount(3)
        self.result_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        self.result_table.horizontalHeader().setHighlightSections(False)
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.result_table, 0, 0, 1, 3)
        self.search_button = QtGui.QPushButton(ProductSearch)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.gridLayout.addWidget(self.search_button, 2, 0, 1, 1)
        self.close_button = QtGui.QPushButton(ProductSearch)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.gridLayout.addWidget(self.close_button, 2, 2, 1, 1)

        self.retranslateUi(ProductSearch)
        QtCore.QMetaObject.connectSlotsByName(ProductSearch)

    def retranslateUi(self, ProductSearch):
        ProductSearch.setWindowTitle(QtGui.QApplication.translate("ProductSearch", "Form", None, QtGui.QApplication.UnicodeUTF8))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("ProductSearch", "Наименование товара", None, QtGui.QApplication.UnicodeUTF8))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("ProductSearch", "Количество", None, QtGui.QApplication.UnicodeUTF8))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("ProductSearch", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setText(QtGui.QApplication.translate("ProductSearch", "Поиск", None, QtGui.QApplication.UnicodeUTF8))
        self.close_button.setText(QtGui.QApplication.translate("ProductSearch", "Выход", None, QtGui.QApplication.UnicodeUTF8))

