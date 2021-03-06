from PyQt4 import QtGui, QtCore, Qt
from utils import loadUi
from shop.models import ClientProduct
#from django.conf import settings


class ProductSearchView(QtGui.QWidget):
    def __init__(self, default_queryset=None, *args, **kwargs):
        super(ProductSearchView, self).__init__(*args, **kwargs)
        self.default_queryset = default_queryset
        if self.default_queryset is None:
            self.default_queryset = ClientProduct.objects.all()
        self.ui = loadUi("shop/product_search.ui", self)
        self.ui.result_table.setColumnWidth(0, 310)
        self.ui.result_table.setColumnWidth(1, 90)
        self.ui.result_table.horizontalHeader().setResizeMode(
                                                      QtGui.QHeaderView.Fixed)
        self.set_items(self.default_queryset)
        self.ui.close_button.setShortcut('Esc')
        self.connect(self.ui.close_button,
                     QtCore.SIGNAL('clicked()'),
                     self.close)

    def set_items(self, qs):
        self.ui.result_table.setRowCount(len(qs))
        for i, item in enumerate(qs):
            self.ui.result_table.setItem(i, 0,
                                 QtGui.QTableWidgetItem(item.product.name))
            self.ui.result_table.setItem(i, 1,
                                 QtGui.QTableWidgetItem(str(item.quantity)))
            self.ui.result_table.setItem(i, 2,
                                 QtGui.QTableWidgetItem(str(item.price_out)))
