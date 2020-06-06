# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(235, 235, 235);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.topContainer.sizePolicy().hasHeightForWidth())
        self.topContainer.setSizePolicy(sizePolicy)
        self.topContainer.setMaximumSize(QtCore.QSize(16777215, 80))
        self.topContainer.setAutoFillBackground(False)
        self.topContainer.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.topContainer.setObjectName("topContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.topContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.topContainer)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.categoriesContainer = QtWidgets.QHBoxLayout()
        self.categoriesContainer.setContentsMargins(7, 7, 7, 7)
        self.categoriesContainer.setSpacing(14)
        self.categoriesContainer.setObjectName("categoriesContainer")
        self.batInfo = QtWidgets.QHBoxLayout()
        self.batInfo.setObjectName("batInfo")
        self.batLabel = QtWidgets.QLabel(self.topContainer)
        self.batLabel.setObjectName("batLabel")
        self.batInfo.addWidget(self.batLabel)
        self.batTextEdit = QtWidgets.QTextEdit(self.topContainer)
        self.batTextEdit.setEnabled(False)
        self.batTextEdit.setObjectName("batTextEdit")
        self.batInfo.addWidget(self.batTextEdit)
        self.categoriesContainer.addLayout(self.batInfo)
        self.bowInfo = QtWidgets.QHBoxLayout()
        self.bowInfo.setObjectName("bowInfo")
        self.bowLabel = QtWidgets.QLabel(self.topContainer)
        self.bowLabel.setObjectName("bowLabel")
        self.bowInfo.addWidget(self.bowLabel)
        self.bowTextEdit = QtWidgets.QTextEdit(self.topContainer)
        self.bowTextEdit.setEnabled(False)
        self.bowTextEdit.setObjectName("bowTextEdit")
        self.bowInfo.addWidget(self.bowTextEdit)
        self.categoriesContainer.addLayout(self.bowInfo)
        self.arInfo = QtWidgets.QHBoxLayout()
        self.arInfo.setObjectName("arInfo")
        self.arLabel = QtWidgets.QLabel(self.topContainer)
        self.arLabel.setObjectName("arLabel")
        self.arInfo.addWidget(self.arLabel)
        self.arTextEdit = QtWidgets.QTextEdit(self.topContainer)
        self.arTextEdit.setEnabled(False)
        self.arTextEdit.setObjectName("arTextEdit")
        self.arInfo.addWidget(self.arTextEdit)
        self.categoriesContainer.addLayout(self.arInfo)
        self.wkInfo = QtWidgets.QHBoxLayout()
        self.wkInfo.setObjectName("wkInfo")
        self.wkLabel = QtWidgets.QLabel(self.topContainer)
        self.wkLabel.setObjectName("wkLabel")
        self.wkInfo.addWidget(self.wkLabel)
        self.wkTextEdit = QtWidgets.QTextEdit(self.topContainer)
        self.wkTextEdit.setEnabled(False)
        self.wkTextEdit.setObjectName("wkTextEdit")
        self.wkInfo.addWidget(self.wkTextEdit)
        self.categoriesContainer.addLayout(self.wkInfo)
        self.verticalLayout.addLayout(self.categoriesContainer)
        self.verticalLayout_2.addWidget(self.topContainer)
        self.bottomContainer = QtWidgets.QWidget(self.centralwidget)
        self.bottomContainer.setObjectName("bottomContainer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomContainer)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftPanel = QtWidgets.QWidget(self.bottomContainer)
        self.leftPanel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.leftPanel.setObjectName("leftPanel")
        self.leftSide = QtWidgets.QVBoxLayout(self.leftPanel)
        self.leftSide.setContentsMargins(9, 9, 9, 9)
        self.leftSide.setSpacing(9)
        self.leftSide.setObjectName("leftSide")
        self.ptsAvailableInfo = QtWidgets.QWidget(self.leftPanel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ptsAvailableInfo.sizePolicy().hasHeightForWidth())
        self.ptsAvailableInfo.setSizePolicy(sizePolicy)
        self.ptsAvailableInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ptsAvailableInfo.setObjectName("ptsAvailableInfo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ptsAvailableInfo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ptsAvailableLabel = QtWidgets.QLabel(self.ptsAvailableInfo)
        self.ptsAvailableLabel.setObjectName("ptsAvailableLabel")
        self.horizontalLayout_3.addWidget(self.ptsAvailableLabel)
        self.ptsAvailableTextEdit = QtWidgets.QTextEdit(self.ptsAvailableInfo)
        self.ptsAvailableTextEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ptsAvailableTextEdit.sizePolicy().hasHeightForWidth())
        self.ptsAvailableTextEdit.setSizePolicy(sizePolicy)
        self.ptsAvailableTextEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ptsAvailableTextEdit.setObjectName("ptsAvailableTextEdit")
        self.horizontalLayout_3.addWidget(self.ptsAvailableTextEdit)
        spacerItem = QtWidgets.QSpacerItem(
            100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.leftSide.addWidget(self.ptsAvailableInfo)
        self.ctgContainer = QtWidgets.QVBoxLayout()
        self.ctgContainer.setObjectName("ctgContainer")
        self.ctgGroup = QtWidgets.QGroupBox(self.leftPanel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ctgGroup.sizePolicy().hasHeightForWidth())
        self.ctgGroup.setSizePolicy(sizePolicy)
        self.ctgGroup.setMinimumSize(QtCore.QSize(0, 50))
        self.ctgGroup.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ctgGroup.setBaseSize(QtCore.QSize(0, 0))
        self.ctgGroup.setObjectName("ctgGroup")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ctgGroup)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.batRadio = QtWidgets.QRadioButton(self.ctgGroup)
        self.batRadio.setObjectName("batRadio")
        self.horizontalLayout_6.addWidget(self.batRadio)
        self.bowRadio = QtWidgets.QRadioButton(self.ctgGroup)
        self.bowRadio.setObjectName("bowRadio")
        self.horizontalLayout_6.addWidget(self.bowRadio)
        self.arRadio = QtWidgets.QRadioButton(self.ctgGroup)
        self.arRadio.setObjectName("arRadio")
        self.horizontalLayout_6.addWidget(self.arRadio)
        self.wkRadio = QtWidgets.QRadioButton(self.ctgGroup)
        self.wkRadio.setObjectName("wkRadio")
        self.horizontalLayout_6.addWidget(self.wkRadio)
        self.ctgContainer.addWidget(self.ctgGroup)
        self.leftSide.addLayout(self.ctgContainer)
        self.availablePlayersList = QtWidgets.QListWidget(self.leftPanel)
        self.availablePlayersList.setObjectName("availablePlayersList")
        self.leftSide.addWidget(self.availablePlayersList)
        self.horizontalLayout.addWidget(self.leftPanel)
        spacerItem1 = QtWidgets.QSpacerItem(
            30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.rightPanel = QtWidgets.QWidget(self.bottomContainer)
        self.rightPanel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rightPanel.setObjectName("rightPanel")
        self.rightSIde = QtWidgets.QVBoxLayout(self.rightPanel)
        self.rightSIde.setContentsMargins(9, 9, 9, 9)
        self.rightSIde.setObjectName("rightSIde")
        self.ptsUsedInfo = QtWidgets.QWidget(self.rightPanel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ptsUsedInfo.sizePolicy().hasHeightForWidth())
        self.ptsUsedInfo.setSizePolicy(sizePolicy)
        self.ptsUsedInfo.setMaximumSize(QtCore.QSize(16777215, 55))
        self.ptsUsedInfo.setObjectName("ptsUsedInfo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ptsUsedInfo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ptsUsedLabel = QtWidgets.QLabel(self.ptsUsedInfo)
        self.ptsUsedLabel.setObjectName("ptsUsedLabel")
        self.horizontalLayout_4.addWidget(self.ptsUsedLabel)
        self.ptsUsedTextEdit = QtWidgets.QTextEdit(self.ptsUsedInfo)
        self.ptsUsedTextEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ptsUsedTextEdit.sizePolicy().hasHeightForWidth())
        self.ptsUsedTextEdit.setSizePolicy(sizePolicy)
        self.ptsUsedTextEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ptsUsedTextEdit.setObjectName("ptsUsedTextEdit")
        self.horizontalLayout_4.addWidget(self.ptsUsedTextEdit)
        spacerItem2 = QtWidgets.QSpacerItem(
            100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.rightSIde.addWidget(self.ptsUsedInfo)
        self.teamInfo = QtWidgets.QVBoxLayout()
        self.teamInfo.setObjectName("teamInfo")
        self.teamNameInfo = QtWidgets.QWidget(self.rightPanel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.teamNameInfo.sizePolicy().hasHeightForWidth())
        self.teamNameInfo.setSizePolicy(sizePolicy)
        self.teamNameInfo.setMinimumSize(QtCore.QSize(0, 50))
        self.teamNameInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.teamNameInfo.setObjectName("teamNameInfo")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.teamNameInfo)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.teamNameTitle = QtWidgets.QLabel(self.teamNameInfo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.teamNameTitle.sizePolicy().hasHeightForWidth())
        self.teamNameTitle.setSizePolicy(sizePolicy)
        self.teamNameTitle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.teamNameTitle.setObjectName("teamNameTitle")
        self.horizontalLayout_7.addWidget(self.teamNameTitle)
        self.teamNameLabel = QtWidgets.QLabel(self.teamNameInfo)
        self.teamNameLabel.setObjectName("teamNameLabel")
        self.horizontalLayout_7.addWidget(self.teamNameLabel)
        self.teamInfo.addWidget(self.teamNameInfo)
        self.chosenPlayersList = QtWidgets.QListWidget(self.rightPanel)
        self.chosenPlayersList.setObjectName("chosenPlayersList")
        self.teamInfo.addWidget(self.chosenPlayersList)
        self.rightSIde.addLayout(self.teamInfo)
        self.horizontalLayout.addWidget(self.rightPanel)
        self.verticalLayout_2.addWidget(self.bottomContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewTeam = QtWidgets.QAction(MainWindow)
        self.actionNewTeam.setObjectName("actionNewTeam")
        self.actionOpenTeam = QtWidgets.QAction(MainWindow)
        self.actionOpenTeam.setObjectName("actionOpenTeam")
        self.actionSaveTeam = QtWidgets.QAction(MainWindow)
        self.actionSaveTeam.setObjectName("actionSaveTeam")
        self.actionEvaluateTeam = QtWidgets.QAction(MainWindow)
        self.actionEvaluateTeam.setObjectName("actionEvaluateTeam")
        self.menuManage_Teams.addAction(self.actionNewTeam)
        self.menuManage_Teams.addAction(self.actionOpenTeam)
        self.menuManage_Teams.addAction(self.actionSaveTeam)
        self.menuManage_Teams.addAction(self.actionEvaluateTeam)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(
            self.menu_handler)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set default variables and update them in up
        self.set_default_variables()
        self.update_ui()

        # list double clicked actions
        self.availablePlayersList.itemDoubleClicked.connect(
            self.remove_from_available_players)
        self.chosenPlayersList.itemDoubleClicked.connect(
            self.remove_from_chosen_players)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.batLabel.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.bowLabel.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.arLabel.setText(_translate("MainWindow", "All Rounders (AR)"))
        self.wkLabel.setText(_translate("MainWindow", "Wicket Keeper (WK)"))
        self.ptsAvailableLabel.setText(
            _translate("MainWindow", "Points Available"))
        self.ctgGroup.setTitle(_translate("MainWindow", "Categories"))
        self.batRadio.setText(_translate("MainWindow", "BAT"))
        self.bowRadio.setText(_translate("MainWindow", "BOW"))
        self.arRadio.setText(_translate("MainWindow", "AR"))
        self.wkRadio.setText(_translate("MainWindow", "WK"))
        self.ptsUsedLabel.setText(_translate("MainWindow", "Points Used"))
        self.teamNameTitle.setText(_translate("MainWindow", "Team Name"))
        self.teamNameLabel.setText(_translate("MainWindow", "TEAM_NAME_HERE"))
        self.menuManage_Teams.setTitle(
            _translate("MainWindow", "Manage Teams"))
        self.actionNewTeam.setText(_translate("MainWindow", "NEW Team"))
        self.actionOpenTeam.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSaveTeam.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEvaluateTeam.setText(
            _translate("MainWindow", "EVALUATE Team"))

    def menu_handler(self, action):
        action_performed = action.text()
        if action_performed == 'NEW Team':
            print('new')
        elif action_performed == 'OPEN Team':
            print('open')
        elif action_performed == 'SAVE Team':
            print('save')
        elif action_performed == 'EVALUATE Team':
            print('evaluate')

    def set_default_variables(self):
        self.batsmen = 0
        self.bowlers = 0
        self.all_rounders = 0
        self.wicket_keeper = 0
        self.points_available = 1000
        self.points_used = 0
        self.team_name = 'TEAM_NAME'
        self.radio_buttons_enabled = False
        self.available_players = {}

    def update_ui(self):
        # update ui according to current variables
        self.batTextEdit.setText(str(self.batsmen))
        self.bowTextEdit.setText(str(self.bowlers))
        self.arTextEdit.setText(str(self.all_rounders))
        self.wkTextEdit.setText(str(self.wicket_keeper))
        self.ptsAvailableTextEdit.setText(str(self.points_available))
        self.ptsUsedTextEdit.setText(str(self.points_used))
        self.teamNameLabel.setText(self.team_name)

        radio_buttons = [self.batRadio,
                         self.bowRadio, self.arRadio, self.wkRadio]
        if(self.radio_buttons_enabled):
            for rb in radio_buttons:
                rb.setEnabled(True)
        else:
            for rb in radio_buttons:
                rb.setEnabled(False)

    def populate_available_players_list(self, category):
        pass

    def remove_from_available_players(self, item):
        self.availablePlayersList.takeItem(self.availablePlayersList.row(item))
        self.chosenPlayersList.addItem(item.text())

    def remove_from_chosen_players(self, item):
        self.chosenPlayersList.takeItem(self.chosenPlayersList.row(item))
        self.availablePlayersList.addItem(item.text())


if __name__ == "__main__":
    import sys
    import sqlite3
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
