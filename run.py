#from accounts.ui_views import LoginDialog
import sys
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_shop.settings")
#    from django.core.management import execute_from_command_line
#    execute_from_command_line(sys.argv)
    from shop.base_view import BaseView
    from PyQt4 import QtGui

    app = QtGui.QApplication(sys.argv)
    myapp = BaseView()
    myapp.show()
    sys.exit(app.exec_())
