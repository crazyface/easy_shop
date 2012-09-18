from PyQt4 import QtGui, QtCore
from utils import loadUi
from shop.models import ClientProduct
from shop.product_search_view import ProductSearchView
#from django.conf import settings


class NewSaleView(QtGui.QWidget):
    def __init__(self, default_queryset=None, *args, **kwargs):
        super(NewSaleView, self).__init__(*args, **kwargs)
        self.ui = loadUi("shop/new_sale.ui", self)

        self.connect(self.ui.add_product,
                     QtCore.SIGNAL("clicked()"),
                     self.on_product_search)

    def on_product_search(self):
#        self.parent().setCentralWidget()

        self.product_search = ProductSearchView()
        self.product_search.move(250, 50)
        self.parent().layout().addWidget(self.product_search)

#        self.product_search.move(200,200)

#        self.new_sale

#    def new_sale(self):
#        self.ui.setCe
#    def setupUi(self):
#        self.ui = 
#        self.default_queryset = default_queryset
#        if self.default_queryset is None:
#            self.default_queryset = ClientProduct.objects.all()
#        self.ui.result_table.setColumnWidth(0, 310)
#        self.ui.result_table.setColumnWidth(1, 90)
#        self.ui.result_table.horizontalHeader().setResizeMode(
#                                                      QtGui.QHeaderView.Fixed)
#        self.set_items(self.default_queryset)

#    def set_items(self, qs):
#        self.ui.result_table.setRowCount(len(qs))
#        for i, item in enumerate(qs):
#            self.ui.result_table.setItem(i, 0,
#                                 QtGui.QTableWidgetItem(item.product.name))
#            self.ui.result_table.setItem(i, 1,
#                                 QtGui.QTableWidgetItem(str(item.quantity)))
#            self.ui.result_table.setItem(i, 2,
#                                 QtGui.QTableWidgetItem(str(item.price_out)))
