# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'github_credentials.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GithubCredentialsDialog(object):
    def setupUi(self, GithubCredentialsDialog):
        if not GithubCredentialsDialog.objectName():
            GithubCredentialsDialog.setObjectName(u"GithubCredentialsDialog")
        GithubCredentialsDialog.resize(476, 324)
        self.verticalLayout = QVBoxLayout(GithubCredentialsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(GithubCredentialsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.accessToken_radio = QRadioButton(self.groupBox)
        self.accessToken_radio.setObjectName(u"accessToken_radio")
        self.accessToken_radio.setChecked(True)

        self.horizontalLayout_3.addWidget(self.accessToken_radio)

        self.userpass_radio = QRadioButton(self.groupBox)
        self.userpass_radio.setObjectName(u"userpass_radio")

        self.horizontalLayout_3.addWidget(self.userpass_radio)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.accessToken_widget = QWidget(self.groupBox)
        self.accessToken_widget.setObjectName(u"accessToken_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.accessToken_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.accessToken_widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.accessToken_text = QLineEdit(self.accessToken_widget)
        self.accessToken_text.setObjectName(u"accessToken_text")

        self.horizontalLayout_2.addWidget(self.accessToken_text)


        self.verticalLayout_2.addWidget(self.accessToken_widget)

        self.userpass_widget = QWidget(self.groupBox)
        self.userpass_widget.setObjectName(u"userpass_widget")
        self.horizontalLayout = QHBoxLayout(self.userpass_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.userpass_widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.username_text = QLineEdit(self.userpass_widget)
        self.username_text.setObjectName(u"username_text")

        self.horizontalLayout.addWidget(self.username_text)

        self.label_2 = QLabel(self.userpass_widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.password_text = QLineEdit(self.userpass_widget)
        self.password_text.setObjectName(u"password_text")

        self.horizontalLayout.addWidget(self.password_text)


        self.verticalLayout_2.addWidget(self.userpass_widget)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(GithubCredentialsDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.newBranch_text = QLineEdit(GithubCredentialsDialog)
        self.newBranch_text.setObjectName(u"newBranch_text")

        self.horizontalLayout_4.addWidget(self.newBranch_text)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(GithubCredentialsDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.localFolder_text = QLineEdit(GithubCredentialsDialog)
        self.localFolder_text.setObjectName(u"localFolder_text")
        self.localFolder_text.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.localFolder_text)

        self.localFolder_Browse_Button = QPushButton(GithubCredentialsDialog)
        self.localFolder_Browse_Button.setObjectName(u"localFolder_Browse_Button")

        self.horizontalLayout_5.addWidget(self.localFolder_Browse_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(GithubCredentialsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(GithubCredentialsDialog)
        self.buttonBox.accepted.connect(GithubCredentialsDialog.accept)
        self.buttonBox.rejected.connect(GithubCredentialsDialog.reject)
        self.accessToken_radio.toggled.connect(self.accessToken_widget.setVisible)
        self.userpass_radio.toggled.connect(self.userpass_widget.setVisible)

        QMetaObject.connectSlotsByName(GithubCredentialsDialog)
    # setupUi

    def retranslateUi(self, GithubCredentialsDialog):
        GithubCredentialsDialog.setWindowTitle(QCoreApplication.translate("GithubCredentialsDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("GithubCredentialsDialog", u"Github credentials", None))
        self.accessToken_radio.setText(QCoreApplication.translate("GithubCredentialsDialog", u"Access token", None))
        self.userpass_radio.setText(QCoreApplication.translate("GithubCredentialsDialog", u"User/pass", None))
        self.label_3.setText(QCoreApplication.translate("GithubCredentialsDialog", u"Access token:", None))
        self.label.setText(QCoreApplication.translate("GithubCredentialsDialog", u"User name:", None))
        self.label_2.setText(QCoreApplication.translate("GithubCredentialsDialog", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("GithubCredentialsDialog", u"New branch name:", None))
        self.label_5.setText(QCoreApplication.translate("GithubCredentialsDialog", u"Local repo folder:", None))
        self.localFolder_Browse_Button.setText(QCoreApplication.translate("GithubCredentialsDialog", u"Browse...", None))
    # retranslateUi

