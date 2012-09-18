from PyQt4 import QtGui, QtCore
from utils import loadUi
from shop.models import ClientProduct
from shop.new_sale_view import NewSaleView
#from django.conf import settings


class BaseView(QtGui.QMainWindow):
    def __init__(self, default_queryset=None, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)
        self.ui = loadUi("base.ui", self)
        self.connect(self.ui.new_sale,
                     QtCore.SIGNAL("triggered()"),
                     self.on_new_sale)


    def on_new_sale(self):
        self.ui.setCentralWidget(NewSaleView())
