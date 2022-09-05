# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diseño_prueba.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_general(object):
    def setupUi(self, Form_general):
        if not Form_general.objectName():
            Form_general.setObjectName(u"Form_general")
        Form_general.resize(740, 598)
        self.horizontalLayout = QHBoxLayout(Form_general)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_padre = QFrame(Form_general)
        self.frame_padre.setObjectName(u"frame_padre")
        self.frame_padre.setFrameShape(QFrame.StyledPanel)
        self.frame_padre.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_padre)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_padre)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_inicio = QPushButton(self.frame_control)
        self.bt_inicio.setObjectName(u"bt_inicio")

        self.verticalLayout.addWidget(self.bt_inicio)

        self.bt_ajustes = QPushButton(self.frame_control)
        self.bt_ajustes.setObjectName(u"bt_ajustes")

        self.verticalLayout.addWidget(self.bt_ajustes)

        self.verticalSpacer = QSpacerItem(20, 475, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_contenedor = QFrame(self.frame_padre)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_contenedor)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_ajustes = QWidget()
        self.page_ajustes.setObjectName(u"page_ajustes")
        self.stackedWidget.addWidget(self.page_ajustes)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_contenedor)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)

        self.horizontalLayout.addWidget(self.frame_padre)


        self.retranslateUi(Form_general)

        QMetaObject.connectSlotsByName(Form_general)
    # setupUi

    def retranslateUi(self, Form_general):
        Form_general.setWindowTitle(QCoreApplication.translate("Form_general", u"Form", None))
        self.bt_inicio.setText(QCoreApplication.translate("Form_general", u"INICIO", None))
        self.bt_ajustes.setText(QCoreApplication.translate("Form_general", u"AJUSTES", None))
    # retranslateUi

