from PyQt4 import QtCore, QtGui, uic
#from accounts.ui_views import LoginDialog
import sys
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_shop.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    from shop.product_search_view import ProductSearchView


    app = QtGui.QApplication(sys.argv)
    myapp = ProductSearchView()
    myapp.show()
    sys.exit(app.exec_())
