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
        MainWindow.resize(644, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel {\n"
"    font: 9pt;\n"
"    color: #3e3e3e;\n"
"}\n"
"\n"
"#yourSelectionsLabel {\n"
"    font: bold 10pt;\n"
"}\n"
"\n"
"QWidget#centralwidget {\n"
"      background-color: #EDFCEE;\n"
"}\n"
"\n"
"#topContainer, #footerLabel {\n"
"    background-color: #85EA8C;\n"
"}\n"
"\n"
"#ptsAvailableInfo, #ptsUsedInfo {\n"
"    background-color: #A8F0AD;\n"
"}\n"
"\n"
"#ctgGroup, #teamNameInfo {\n"
"    background-color: #CBF6CE;\n"
"    font: bold 9pt;\n"
"    color: #3e3e3e;\n"
"}\n"
"\n"
"#ctgGroupContainer {\n"
"    background-color: #CBF6CE;\n"
"}\n"
"\n"
"#footerLabel {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    font: 10pt;\n"
"    color: black;\n"
"}\n"
"\n"
"#teamNameTitle {\n"
"    font: bold;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font: bold 10pt;\n"
"    color: #2e2e2e;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topContainer.sizePolicy().hasHeightForWidth())
        self.topContainer.setSizePolicy(sizePolicy)
        self.topContainer.setMaximumSize(QtCore.QSize(16777215, 80))
        self.topContainer.setAutoFillBackground(False)
        self.topContainer.setStyleSheet("")
        self.topContainer.setObjectName("topContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.topContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.yourSelectionsLabel = QtWidgets.QLabel(self.topContainer)
        self.yourSelectionsLabel.setObjectName("yourSelectionsLabel")
        self.verticalLayout.addWidget(self.yourSelectionsLabel)
        self.categoriesContainer = QtWidgets.QHBoxLayout()
        self.categoriesContainer.setContentsMargins(7, 7, 7, 7)
        self.categoriesContainer.setSpacing(14)
        self.categoriesContainer.setObjectName("categoriesContainer")
        self.batInfo = QtWidgets.QHBoxLayout()
        self.batInfo.setObjectName("batInfo")
        self.batLabel = QtWidgets.QLabel(self.topContainer)
        self.batLabel.setObjectName("batLabel")
        self.batInfo.addWidget(self.batLabel)
        self.batTextEdit = QtWidgets.QLineEdit(self.topContainer)
        self.batTextEdit.setEnabled(False)
        self.batTextEdit.setMinimumSize(QtCore.QSize(30, 0))
        self.batTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.batTextEdit.setObjectName("batTextEdit")
        self.batInfo.addWidget(self.batTextEdit)
        self.categoriesContainer.addLayout(self.batInfo)
        self.bowInfo = QtWidgets.QHBoxLayout()
        self.bowInfo.setObjectName("bowInfo")
        self.bowLabel = QtWidgets.QLabel(self.topContainer)
        self.bowLabel.setObjectName("bowLabel")
        self.bowInfo.addWidget(self.bowLabel)
        self.bowTextEdit = QtWidgets.QLineEdit(self.topContainer)
        self.bowTextEdit.setEnabled(False)
        self.bowTextEdit.setMinimumSize(QtCore.QSize(30, 0))
        self.bowTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.bowTextEdit.setObjectName("bowTextEdit")
        self.bowInfo.addWidget(self.bowTextEdit)
        self.categoriesContainer.addLayout(self.bowInfo)
        self.arInfo = QtWidgets.QHBoxLayout()
        self.arInfo.setObjectName("arInfo")
        self.arLabel = QtWidgets.QLabel(self.topContainer)
        self.arLabel.setObjectName("arLabel")
        self.arInfo.addWidget(self.arLabel)
        self.arTextEdit = QtWidgets.QLineEdit(self.topContainer)
        self.arTextEdit.setEnabled(False)
        self.arTextEdit.setMinimumSize(QtCore.QSize(30, 0))
        self.arTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.arTextEdit.setObjectName("arTextEdit")
        self.arInfo.addWidget(self.arTextEdit)
        self.categoriesContainer.addLayout(self.arInfo)
        self.wkInfo = QtWidgets.QHBoxLayout()
        self.wkInfo.setObjectName("wkInfo")
        self.wkLabel = QtWidgets.QLabel(self.topContainer)
        self.wkLabel.setObjectName("wkLabel")
        self.wkInfo.addWidget(self.wkLabel)
        self.wkTextEdit = QtWidgets.QLineEdit(self.topContainer)
        self.wkTextEdit.setEnabled(False)
        self.wkTextEdit.setMinimumSize(QtCore.QSize(30, 0))
        self.wkTextEdit.setAlignment(QtCore.Qt.AlignCenter)
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
        self.leftPanel.setStyleSheet("")
        self.leftPanel.setObjectName("leftPanel")
        self.leftSide = QtWidgets.QVBoxLayout(self.leftPanel)
        self.leftSide.setContentsMargins(9, 9, 9, 9)
        self.leftSide.setSpacing(0)
        self.leftSide.setObjectName("leftSide")
        self.ptsAvailableInfo = QtWidgets.QWidget(self.leftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ptsAvailableInfo.sizePolicy().hasHeightForWidth())
        self.ptsAvailableInfo.setSizePolicy(sizePolicy)
        self.ptsAvailableInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ptsAvailableInfo.setObjectName("ptsAvailableInfo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ptsAvailableInfo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ptsAvailableLabel = QtWidgets.QLabel(self.ptsAvailableInfo)
        self.ptsAvailableLabel.setObjectName("ptsAvailableLabel")
        self.horizontalLayout_3.addWidget(self.ptsAvailableLabel)
        self.ptsAvailableTextEdit = QtWidgets.QLineEdit(self.ptsAvailableInfo)
        self.ptsAvailableTextEdit.setEnabled(False)
        self.ptsAvailableTextEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.ptsAvailableTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ptsAvailableTextEdit.setObjectName("ptsAvailableTextEdit")
        self.horizontalLayout_3.addWidget(self.ptsAvailableTextEdit)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.leftSide.addWidget(self.ptsAvailableInfo)
        self.ctgGroupContainer = QtWidgets.QWidget(self.leftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctgGroupContainer.sizePolicy().hasHeightForWidth())
        self.ctgGroupContainer.setSizePolicy(sizePolicy)
        self.ctgGroupContainer.setMaximumSize(QtCore.QSize(16777215, 60))
        self.ctgGroupContainer.setObjectName("ctgGroupContainer")
        self.ctgContainer = QtWidgets.QVBoxLayout(self.ctgGroupContainer)
        self.ctgContainer.setContentsMargins(0, 6, 0, 0)
        self.ctgContainer.setObjectName("ctgContainer")
        self.ctgGroup = QtWidgets.QGroupBox(self.ctgGroupContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctgGroup.sizePolicy().hasHeightForWidth())
        self.ctgGroup.setSizePolicy(sizePolicy)
        self.ctgGroup.setMinimumSize(QtCore.QSize(0, 50))
        self.ctgGroup.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ctgGroup.setBaseSize(QtCore.QSize(0, 0))
        self.ctgGroup.setFlat(False)
        self.ctgGroup.setCheckable(False)
        self.ctgGroup.setObjectName("ctgGroup")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ctgGroup)
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, -1)
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
        self.leftSide.addWidget(self.ctgGroupContainer)
        self.availablePlayersList = QtWidgets.QListWidget(self.leftPanel)
        self.availablePlayersList.setObjectName("availablePlayersList")
        self.leftSide.addWidget(self.availablePlayersList)
        self.horizontalLayout.addWidget(self.leftPanel)
        self.rightPanel = QtWidgets.QWidget(self.bottomContainer)
        self.rightPanel.setStyleSheet("")
        self.rightPanel.setObjectName("rightPanel")
        self.rightSIde = QtWidgets.QVBoxLayout(self.rightPanel)
        self.rightSIde.setContentsMargins(9, 9, 9, 9)
        self.rightSIde.setSpacing(0)
        self.rightSIde.setObjectName("rightSIde")
        self.ptsUsedInfo = QtWidgets.QWidget(self.rightPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ptsUsedInfo.sizePolicy().hasHeightForWidth())
        self.ptsUsedInfo.setSizePolicy(sizePolicy)
        self.ptsUsedInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ptsUsedInfo.setObjectName("ptsUsedInfo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ptsUsedInfo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ptsUsedLabel = QtWidgets.QLabel(self.ptsUsedInfo)
        self.ptsUsedLabel.setObjectName("ptsUsedLabel")
        self.horizontalLayout_4.addWidget(self.ptsUsedLabel)
        self.ptsUsedTextEdit = QtWidgets.QLineEdit(self.ptsUsedInfo)
        self.ptsUsedTextEdit.setEnabled(False)
        self.ptsUsedTextEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.ptsUsedTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ptsUsedTextEdit.setObjectName("ptsUsedTextEdit")
        self.horizontalLayout_4.addWidget(self.ptsUsedTextEdit)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.rightSIde.addWidget(self.ptsUsedInfo)
        self.teamInfo = QtWidgets.QVBoxLayout()
        self.teamInfo.setSpacing(0)
        self.teamInfo.setObjectName("teamInfo")
        self.teamNameInfo = QtWidgets.QWidget(self.rightPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamNameInfo.sizePolicy().hasHeightForWidth())
        self.teamNameInfo.setSizePolicy(sizePolicy)
        self.teamNameInfo.setMinimumSize(QtCore.QSize(0, 60))
        self.teamNameInfo.setMaximumSize(QtCore.QSize(16777215, 66))
        self.teamNameInfo.setObjectName("teamNameInfo")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.teamNameInfo)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.teamNameTitle = QtWidgets.QLabel(self.teamNameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamNameTitle.sizePolicy().hasHeightForWidth())
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
        self.rightPanel.raise_()
        self.leftPanel.raise_()
        self.verticalLayout_2.addWidget(self.bottomContainer)
        self.footerLabel = QtWidgets.QLabel(self.centralwidget)
        self.footerLabel.setObjectName("footerLabel")
        self.verticalLayout_2.addWidget(self.footerLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
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
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # setting window icon
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        # connect handle functions
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu_handler)
        for rb in [self.batRadio, self.bowRadio, self.arRadio, self.wkRadio]:
            rb.toggled.connect(self.radio_button_handler)

        # set default variables and update them in up
        self.set_default_variables()
        self.update_ui()

        # list double clicked actions
        self.availablePlayersList.itemDoubleClicked.connect(self.remove_from_available_players)
        self.chosenPlayersList.itemDoubleClicked.connect(self.remove_from_chosen_players)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.yourSelectionsLabel.setText(_translate("MainWindow", "Your Selections"))
        self.batLabel.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.batTextEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.bowLabel.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.bowTextEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.arLabel.setText(_translate("MainWindow", "All Rounders (AR)"))
        self.arTextEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.wkLabel.setText(_translate("MainWindow", "Wicket Keeper (WK)"))
        self.wkTextEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.ptsAvailableLabel.setText(_translate("MainWindow", "Points Available"))
        self.ptsAvailableTextEdit.setPlaceholderText(_translate("MainWindow", "1000"))
        self.ctgGroup.setTitle(_translate("MainWindow", "Categories"))
        self.batRadio.setText(_translate("MainWindow", "BAT"))
        self.bowRadio.setText(_translate("MainWindow", "BOW"))
        self.arRadio.setText(_translate("MainWindow", "AR"))
        self.wkRadio.setText(_translate("MainWindow", "WK"))
        self.ptsUsedLabel.setText(_translate("MainWindow", "Points Used"))
        self.ptsUsedTextEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.teamNameTitle.setText(_translate("MainWindow", "Team Name"))
        self.teamNameLabel.setText(_translate("MainWindow", "TEAM_NAME_HERE"))
        self.footerLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">Fantasy Cricket Team Manager</span></p></body></html>"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNewTeam.setText(_translate("MainWindow", "NEW Team"))
        self.actionNewTeam.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpenTeam.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOpenTeam.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSaveTeam.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSaveTeam.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEvaluateTeam.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEvaluateTeam.setShortcut(_translate("MainWindow", "Ctrl+E"))

    def menu_handler(self, action):
        action_performed = action.text()
        if action_performed == 'NEW Team':
            self.create_new_team()
        elif action_performed == 'OPEN Team':
            try:
                self.open_team()
                print('MESSAGE: team opened successfully')
            except Exception as error:
                print(f'ERROR: {error}')
        elif action_performed == 'SAVE Team':
            try:
                self.save_team()
                print('MESSAGE: team saved successfully')
                self.show_message(heading = 'Success', desc = 'Team Saved Successfully')
            except ValueError as error:
                print(f'ERROR: {error}')
                self.show_message(heading = 'Error', desc = str(error), icon='critical')
            except Exception as error:
                print(f'ERROR: {error}')
                self.show_message(heading = 'Error', desc = str(error), icon='critical')
        elif action_performed == 'EVALUATE Team':
            try:
                self.evaluate_team()
            except Exception as error:
                print(f'ERROR: {error}')
                self.show_message(heading = 'Error', desc = str(error), icon='critical')

    def radio_button_handler(self):
        for rb in [self.batRadio, self.bowRadio, self.arRadio, self.wkRadio]:
            if(rb.isChecked()):
                self.populate_available_players_list(rb.text())

    def set_default_variables(self):
        self.batsmen = 0
        self.bowlers = 0
        self.all_rounders = 0
        self.wicket_keeper = 0
        self.points_available = 1000
        self.points_used = 0
        self.team_name = 'NO_TEAM_SELECTED'
        self.radio_buttons_enabled = False

        total_players = {}
        cricket_db_cursor.execute('SELECT player, value, ctg FROM stats;')
        for record in cricket_db_cursor.fetchall():
            total_players.update(
                {
                    record[0]: {
                        "name": record[0],
                        "value": record[1],
                        "ctg": record[2]
                    }
                }
            )

        self.total_players = total_players.copy()

        # clearing both lists
        self.availablePlayersList.clear()
        self.chosenPlayersList.clear()

    def update_ui(self):
        # update ui according to current variables
        self.batTextEdit.setText(str(self.batsmen))
        self.bowTextEdit.setText(str(self.bowlers))
        self.arTextEdit.setText(str(self.all_rounders))
        self.wkTextEdit.setText(str(self.wicket_keeper))
        self.ptsAvailableTextEdit.setText(str(self.points_available))
        self.ptsUsedTextEdit.setText(str(self.points_used))
        self.teamNameLabel.setText(self.team_name)

        radio_buttons = [self.batRadio, self.bowRadio, self.arRadio, self.wkRadio]
        if(self.radio_buttons_enabled):
            for rb in radio_buttons:
                rb.setEnabled(True)
        else:
            for rb in radio_buttons:
                rb.setEnabled(False)
                rb.setChecked(False)

    def populate_available_players_list(self, category = 'ALL'):
        self.availablePlayersList.clear()

        chosen_players = []
        for index in range(self.chosenPlayersList.count()):
            chosen_players.append(self.chosenPlayersList.item(index).text())

        for player in self.total_players.values():
            # if player already in chosen list dont add it to available players
            if player['name'] in chosen_players:
                continue

            # category in radio button is BOW but in db its BWL
            if(category == 'BOW'):
                category = 'BWL'

            if category == 'ALL':
                self.availablePlayersList.addItem(player['name'])
            elif category == player['ctg']:
                self.availablePlayersList.addItem(player['name'])


    def remove_from_available_players(self, item):
        try:
            self.add_player_to_team(item.text())
            self.availablePlayersList.takeItem(self.availablePlayersList.row(item))
            self.chosenPlayersList.addItem(item.text())
        except ValueError as error:
            print(f'ERROR: {error}')
            self.show_message(heading = 'Error', desc = str(error), icon='critical')


    def remove_from_chosen_players(self, item):
        self.chosenPlayersList.takeItem(self.chosenPlayersList.row(item))
        self.availablePlayersList.addItem(item.text())
        self.remove_player_from_team(item.text())

        # update list according to category seletect in radio button
        self.radio_button_handler()

    def add_player_to_team(self, name):        
        player = self.total_players[name]

        try:
            self.validate_logic(points_available = self.points_available - player['value'])            
            if player['ctg'] == 'BAT':
                self.validate_logic(batsmen = self.batsmen + 1)
                self.batsmen += 1
            elif player['ctg'] == 'BWL':
                self.validate_logic(bowlers = self.bowlers + 1)
                self.bowlers += 1
            elif player['ctg'] == 'AR':
                self.validate_logic(all_rounders = self.all_rounders + 1)
                self.all_rounders +=1
            elif player['ctg'] == 'WK':
                self.validate_logic(wicket_keeper = self.wicket_keeper + 1)
                self.wicket_keeper += 1

            self.points_available -= player['value']
            self.points_used += player['value']
        except ValueError as error:
            raise error

        
        self.update_ui()

    def remove_player_from_team(self, name):
        player = self.total_players[name]

        if player['ctg'] == 'BAT':
            self.batsmen -= 1
        elif player['ctg'] == 'BWL':
            self.bowlers -= 1
        elif player['ctg'] == 'AR':
            self.all_rounders -=1
        elif player['ctg'] == 'WK':
            self.wicket_keeper -= 1

        self.points_available += player['value']
        self.points_used -= player['value']
        self.update_ui()

    def create_new_team(self):
        value, confirmed = QtWidgets.QInputDialog.getText(MainWindow, 'Fantasy Cricket', 'Enter Team Name')
        if confirmed:
            valid, message = self.is_valid_team_name(value)
            if not valid:
                print(f'ERROR: {message}')
                self.show_message(heading = 'Error', desc = str(message), icon='critical')
                return self.create_new_team()
            
            self.set_default_variables()
            self.team_name = value
            self.populate_available_players_list()
            self.radio_buttons_enabled = True
            self.update_ui()
        
            
    def is_valid_team_name(self, name):
        if(len(name) < 4):
            return (False, 'Team Name should contain atleast 4 characters')
        try:
            teams = []
            cricket_db_cursor.execute('SELECT name FROM teams')
            for record in cricket_db_cursor.fetchall():
                teams.append(record[0])
            
            if name in teams:
                return (False, 'Team with this name already exists')
        except:
            print('ERROR: couldn\'t fetch team names')
        
        if name == 'NO_TEAM_SELECTED':
            return (False, 'Team name invalid')

        return (True, 'Team Name is valid')
    

    def validate_logic( self, points_available = None, batsmen = None, bowlers = None, all_rounders = None, wicket_keeper = None):
        # not directly using current variables so that function
        # can also be used to check other states
        if not points_available: points_available = self.points_available
        if not batsmen: batsmen = self.batsmen
        if not bowlers: bowlers = self.bowlers
        if not all_rounders: all_rounders = self.all_rounders
        if not wicket_keeper: wicket_keeper = self.wicket_keeper

        if points_available < 0:
            raise ValueError('You don\'t have enough points available')        
        if wicket_keeper > 1:
            raise ValueError('You can only have one Wicket Keeper in team')        
        if batsmen > 5:
            raise ValueError('You cat\'t have more than 5 Batsmen in team')
        if bowlers > 5:
            raise ValueError('You can\'t have more than 5 Bowlers in team')
        if all_rounders > 3:
            raise ValueError('You can\'t have more than 3 all rounders in team')

        return True

    def save_team(self):
        team_players = self.batsmen + self.bowlers + self.all_rounders + self.wicket_keeper
        
        # if team name is NO_TEAM_SELECTED this means user didn't create team yet
        if self.team_name == 'NO_TEAM_SELECTED':
            raise ValueError('No team selected, create or open a team')

        try:
            self.validate_logic()
        except ValueError as error:
            raise error

        if team_players > 11:
            raise ValueError('You can only have 11 players in team')
        if team_players < 11:
            raise ValueError('You must have atleast 11 players in team')

        team_name = self.team_name
        team_players_string = ''
        team_value = 0

        for i in range(self.chosenPlayersList.count()):
            player_name = self.chosenPlayersList.item(i).text()
            team_players_string += player_name if i == 0 else f':{player_name}'
            team_value += self.total_players[player_name]['value']

        try:
            sql = f"""INSERT INTO teams (name, players, value) 
                VALUES ("{team_name}", "{team_players_string}", {team_value})
                ON CONFLICT(name) 
                DO UPDATE SET players = "{team_players_string}", value = {team_value} WHERE name = "{team_name}";"""
            cricket_db_cursor.execute(sql)
            cricket_db.commit()
        except Exception as error:
            cricket_db.rollback()
            raise error

        return True

    def open_team(self):        
        # getting teams
        teams = {}
        try:
            cricket_db_cursor.execute('SELECT name, players, value FROM teams')
            for record in cricket_db_cursor.fetchall():
                teams.update({
                    record[0]: {
                        "name": record[0],
                        "players": record[1].split(':'),
                        "value": record[2]
                    }
                })
        except Exception as error:
            raise error

        if len(teams):
            opened_team, confirmed = QtWidgets.QInputDialog.getItem(MainWindow, "Fantasy Cricket", "Choose a team", teams.keys(), 0, False)
        else:
            raise ValueError('No saved teams found')

        if not confirmed:
            raise ValueError('No team selected')
        
        # loading defaults and updating ui
        self.set_default_variables()
        self.update_ui()

        # updating variable values to the opened team
        self.team_name = opened_team
        self.points_available -= teams[opened_team]['value']
        self.points_used = teams[opened_team]['value']

        for player_name in teams[self.team_name]['players']:
            if self.total_players[player_name]['ctg'] == 'BAT':
                self.batsmen += 1
            elif self.total_players[player_name]['ctg'] == 'BWL':
                self.bowlers += 1
            elif self.total_players[player_name]['ctg'] == 'AR':
                self.all_rounders +=1
            elif self.total_players[player_name]['ctg'] == 'WK':
                self.wicket_keeper += 1
            
            self.chosenPlayersList.addItem(player_name)
        
        
        # refreshing ui
        self.populate_available_players_list()
        self.radio_buttons_enabled = True
        self.update_ui()

    def evaluate_team(self):
        # check if atleast one team is present in database
        try:
            cricket_db_cursor.execute('SELECT name, players, value FROM teams')
        except Exception as error:
            raise error

        if len(cricket_db_cursor.fetchall()):
            # open evaluate dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_EvaluateTeamDialog()
            ui.setupUi(Dialog)
            result = Dialog.exec()
        else:
            raise ValueError('No saved teams found')

    def show_message(self, heading = 'Error', desc = 'Unknown Error Occured', icon = None):
        QMessageBox = QtWidgets.QMessageBox
        if not icon: icon = QMessageBox.Information
        if icon == 'critical': icon = QMessageBox.Critical
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(heading)
        msg.setInformativeText(desc + '\t\t\t')
        msg.setWindowTitle('Fantasy Cricket')
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.exec_()       


if __name__ == "__main__":
    import sys
    import sqlite3
    from evaluateTeam import Ui_EvaluateTeamDialog

    # db connection
    cricket_db = sqlite3.connect('fantasy-cricket.db')
    cricket_db_cursor = cricket_db.cursor()

    # ui initialization
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
