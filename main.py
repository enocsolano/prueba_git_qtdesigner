import sys
from diseño import *

from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog, QListWidget, QLabel, QStackedWidget, QHBoxLayout, QApplication

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        #CREAMOS ESTE OBJETO/PROPIEDAD UI PARA ACCEDER A LOS DIFERENTES COMPONENTES DEL DISEÑO
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #ACEEDER A LAS DIFERENTES PÁGINAS CON LOS BOTONES
        self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.bt_registros.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_registros))
        self.ui.bt_base_datos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_base_datos))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())