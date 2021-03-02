# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EditFormWindow(object):
    def setupUi(self, EditFormWindow):
        if not EditFormWindow.objectName():
            EditFormWindow.setObjectName(u"EditFormWindow")
        EditFormWindow.resize(1090, 877)
        self.actionLoad_JSON = QAction(EditFormWindow)
        self.actionLoad_JSON.setObjectName(u"actionLoad_JSON")
        self.actionSave_JSON = QAction(EditFormWindow)
        self.actionSave_JSON.setObjectName(u"actionSave_JSON")
        self.actionUpload_to_MR_HUB = QAction(EditFormWindow)
        self.actionUpload_to_MR_HUB.setObjectName(u"actionUpload_to_MR_HUB")
        self.centralwidget = QWidget(EditFormWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.single_fields_widget = QWidget(self.centralwidget)
        self.single_fields_widget.setObjectName(u"single_fields_widget")
        self.formLayout = QFormLayout(self.single_fields_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.single_fields_widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name_text = QLineEdit(self.single_fields_widget)
        self.name_text.setObjectName(u"name_text")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_text)

        self.label_2 = QLabel(self.single_fields_widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.single_fields_widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.single_fields_widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.single_fields_widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.single_fields_widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.single_fields_widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.single_fields_widget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.longDescription_label = QLabel(self.single_fields_widget)
        self.longDescription_label.setObjectName(u"longDescription_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.longDescription_label)

        self.label_10 = QLabel(self.single_fields_widget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.single_fields_widget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.single_fields_widget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_12)

        self.imageFilename_text = QLineEdit(self.single_fields_widget)
        self.imageFilename_text.setObjectName(u"imageFilename_text")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.imageFilename_text)

        self.shortDescription_text = QLineEdit(self.single_fields_widget)
        self.shortDescription_text.setObjectName(u"shortDescription_text")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.shortDescription_text)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imagePath_text = QLineEdit(self.single_fields_widget)
        self.imagePath_text.setObjectName(u"imagePath_text")
        self.imagePath_text.setEnabled(False)

        self.horizontalLayout.addWidget(self.imagePath_text)

        self.imageBrowse_button = QPushButton(self.single_fields_widget)
        self.imageBrowse_button.setObjectName(u"imageBrowse_button")

        self.horizontalLayout.addWidget(self.imageBrowse_button)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout)

        self.mainURL_text = QLineEdit(self.single_fields_widget)
        self.mainURL_text.setObjectName(u"mainURL_text")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.mainURL_text)

        self.repoURL_text = QLineEdit(self.single_fields_widget)
        self.repoURL_text.setObjectName(u"repoURL_text")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.repoURL_text)

        self.principalDevelopers_text = QLineEdit(self.single_fields_widget)
        self.principalDevelopers_text.setObjectName(u"principalDevelopers_text")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.principalDevelopers_text)

        self.longDescription_text = QPlainTextEdit(self.single_fields_widget)
        self.longDescription_text.setObjectName(u"longDescription_text")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.longDescription_text.sizePolicy().hasHeightForWidth())
        self.longDescription_text.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.longDescription_text)

        self.dateAdded_text = QLineEdit(self.single_fields_widget)
        self.dateAdded_text.setObjectName(u"dateAdded_text")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.dateAdded_text)

        self.dateUpdated_text = QLineEdit(self.single_fields_widget)
        self.dateUpdated_text.setObjectName(u"dateUpdated_text")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.dateUpdated_text)

        self.category_box = QComboBox(self.single_fields_widget)
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.setObjectName(u"category_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.category_box.sizePolicy().hasHeightForWidth())
        self.category_box.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.category_box)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.citationString_text = QLineEdit(self.single_fields_widget)
        self.citationString_text.setObjectName(u"citationString_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.citationString_text.sizePolicy().hasHeightForWidth())
        self.citationString_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.citationString_text)

        self.citationTest_button = QPushButton(self.single_fields_widget)
        self.citationTest_button.setObjectName(u"citationTest_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.citationTest_button.sizePolicy().hasHeightForWidth())
        self.citationTest_button.setSizePolicy(sizePolicy3)
        self.citationTest_button.setBaseSize(QSize(1, 0))

        self.horizontalLayout_6.addWidget(self.citationTest_button)


        self.formLayout.setLayout(12, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.single_fields_widget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.keywords_table = QTableView(self.groupBox)
        self.keywords_table.setObjectName(u"keywords_table")

        self.verticalLayout.addWidget(self.keywords_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addKeyword_button = QPushButton(self.groupBox)
        self.addKeyword_button.setObjectName(u"addKeyword_button")

        self.horizontalLayout_2.addWidget(self.addKeyword_button)

        self.removeKeyword_button = QPushButton(self.groupBox)
        self.removeKeyword_button.setObjectName(u"removeKeyword_button")

        self.horizontalLayout_2.addWidget(self.removeKeyword_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.extraResources_Table = QTableView(self.groupBox_2)
        self.extraResources_Table.setObjectName(u"extraResources_Table")

        self.verticalLayout_3.addWidget(self.extraResources_Table)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addExtraResources_button = QPushButton(self.groupBox_2)
        self.addExtraResources_button.setObjectName(u"addExtraResources_button")

        self.horizontalLayout_4.addWidget(self.addExtraResources_button)

        self.removeExtraResources_button = QPushButton(self.groupBox_2)
        self.removeExtraResources_button.setObjectName(u"removeExtraResources_button")

        self.horizontalLayout_4.addWidget(self.removeExtraResources_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reference_table = QTableView(self.groupBox_3)
        self.reference_table.setObjectName(u"reference_table")

        self.horizontalLayout_5.addWidget(self.reference_table)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.addReference_button = QPushButton(self.groupBox_3)
        self.addReference_button.setObjectName(u"addReference_button")

        self.verticalLayout_4.addWidget(self.addReference_button)

        self.removeReference_button = QPushButton(self.groupBox_3)
        self.removeReference_button.setObjectName(u"removeReference_button")

        self.verticalLayout_4.addWidget(self.removeReference_button)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        EditFormWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EditFormWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1090, 32))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        EditFormWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(EditFormWindow)
        self.statusbar.setObjectName(u"statusbar")
        EditFormWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_JSON)
        self.menuFile.addAction(self.actionSave_JSON)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpload_to_MR_HUB)

        self.retranslateUi(EditFormWindow)

        QMetaObject.connectSlotsByName(EditFormWindow)
    # setupUi

    def retranslateUi(self, EditFormWindow):
        EditFormWindow.setWindowTitle(QCoreApplication.translate("EditFormWindow", u"MainWindow", None))
        self.actionLoad_JSON.setText(QCoreApplication.translate("EditFormWindow", u"Load JSON...", None))
        self.actionSave_JSON.setText(QCoreApplication.translate("EditFormWindow", u"Save JSON...", None))
        self.actionUpload_to_MR_HUB.setText(QCoreApplication.translate("EditFormWindow", u"Prepare MR-Hub submission...", None))
        self.label.setText(QCoreApplication.translate("EditFormWindow", u"Name:", None))
        self.name_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"Package name", None))
        self.label_2.setText(QCoreApplication.translate("EditFormWindow", u"Category:", None))
        self.label_3.setText(QCoreApplication.translate("EditFormWindow", u"Short Description:", None))
        self.label_4.setText(QCoreApplication.translate("EditFormWindow", u"Image Filename (remote):", None))
        self.label_5.setText(QCoreApplication.translate("EditFormWindow", u"Select image:", None))
        self.label_6.setText(QCoreApplication.translate("EditFormWindow", u"Main URL:", None))
        self.label_7.setText(QCoreApplication.translate("EditFormWindow", u"Repo URL:", None))
        self.label_8.setText(QCoreApplication.translate("EditFormWindow", u"Principal Developers:", None))
        self.longDescription_label.setText(QCoreApplication.translate("EditFormWindow", u"<html><head/><body><p>Long description:</p><p>({:d}/200 words)</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("EditFormWindow", u"Date added to MR Hub:", None))
        self.label_11.setText(QCoreApplication.translate("EditFormWindow", u"Date sofware last updated:", None))
        self.label_12.setText(QCoreApplication.translate("EditFormWindow", u"Citation search string:", None))
        self.imageFilename_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"your_image.png", None))
        self.shortDescription_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"One-line description", None))
        self.imageBrowse_button.setText(QCoreApplication.translate("EditFormWindow", u"Browse...", None))
        self.mainURL_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"https://www.your.website/", None))
        self.repoURL_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"https://github.com/developer/repo", None))
        self.dateAdded_text.setInputMask(QCoreApplication.translate("EditFormWindow", u"9999-99-99", None))
        self.dateAdded_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"2020-01-01", None))
        self.dateUpdated_text.setInputMask(QCoreApplication.translate("EditFormWindow", u"9999-99-99", None))
        self.dateUpdated_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"YYYY-MM-DD", None))
        self.category_box.setItemText(0, QCoreApplication.translate("EditFormWindow", u"Reconstruction", None))
        self.category_box.setItemText(1, QCoreApplication.translate("EditFormWindow", u"Data format", None))
        self.category_box.setItemText(2, QCoreApplication.translate("EditFormWindow", u"Pulse sequences", None))
        self.category_box.setItemText(3, QCoreApplication.translate("EditFormWindow", u"Educational", None))
        self.category_box.setItemText(4, QCoreApplication.translate("EditFormWindow", u"Simulation", None))
        self.category_box.setItemText(5, QCoreApplication.translate("EditFormWindow", u"Visualisation", None))
        self.category_box.setItemText(6, QCoreApplication.translate("EditFormWindow", u"Spectroscopy", None))
        self.category_box.setItemText(7, QCoreApplication.translate("EditFormWindow", u"Image processing", None))
        self.category_box.setItemText(8, QCoreApplication.translate("EditFormWindow", u"Multipurpose", None))

        self.citationString_text.setPlaceholderText(QCoreApplication.translate("EditFormWindow", u"DOI or paperID for Semantic Scholar", None))
        self.citationTest_button.setText(QCoreApplication.translate("EditFormWindow", u"Test", None))
        self.groupBox.setTitle(QCoreApplication.translate("EditFormWindow", u"Keywords", None))
        self.addKeyword_button.setText(QCoreApplication.translate("EditFormWindow", u"Add", None))
        self.removeKeyword_button.setText(QCoreApplication.translate("EditFormWindow", u"Remove", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("EditFormWindow", u"Extra Resources", None))
        self.addExtraResources_button.setText(QCoreApplication.translate("EditFormWindow", u"Add", None))
        self.removeExtraResources_button.setText(QCoreApplication.translate("EditFormWindow", u"Remove", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("EditFormWindow", u"References", None))
        self.addReference_button.setText(QCoreApplication.translate("EditFormWindow", u"Add", None))
        self.removeReference_button.setText(QCoreApplication.translate("EditFormWindow", u"Remove", None))
        self.menuFile.setTitle(QCoreApplication.translate("EditFormWindow", u"File...", None))
    # retranslateUi

