# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EvaluateTeamDialog(object):
    def setupUi(self, EvaluateTeamDialog):
        EvaluateTeamDialog.setObjectName("EvaluateTeamDialog")
        EvaluateTeamDialog.resize(524, 485)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EvaluateTeamDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topContainer = QtWidgets.QWidget(EvaluateTeamDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topContainer.sizePolicy().hasHeightForWidth())
        self.topContainer.setSizePolicy(sizePolicy)
        self.topContainer.setObjectName("topContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.topContainer)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.topContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.teamContainer = QtWidgets.QFormLayout()
        self.teamContainer.setContentsMargins(0, 0, -1, 0)
        self.teamContainer.setObjectName("teamContainer")
        self.teamLabel = QtWidgets.QLabel(self.topContainer)
        self.teamLabel.setObjectName("teamLabel")
        self.teamContainer.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.teamLabel)
        self.teamComboBox = QtWidgets.QComboBox(self.topContainer)
        self.teamComboBox.setObjectName("teamComboBox")
        self.teamContainer.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.teamComboBox)
        self.horizontalLayout_5.addLayout(self.teamContainer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.matchContainer = QtWidgets.QFormLayout()
        self.matchContainer.setObjectName("matchContainer")
        self.matchLabel = QtWidgets.QLabel(self.topContainer)
        self.matchLabel.setObjectName("matchLabel")
        self.matchContainer.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.matchLabel)
        self.matchComboBox = QtWidgets.QComboBox(self.topContainer)
        self.matchComboBox.setObjectName("matchComboBox")
        self.matchContainer.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.matchComboBox)
        self.horizontalLayout_5.addLayout(self.matchContainer)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.topContainer)
        self.listsContainer = QtWidgets.QHBoxLayout()
        self.listsContainer.setObjectName("listsContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.playersLabel = QtWidgets.QLabel(EvaluateTeamDialog)
        self.playersLabel.setObjectName("playersLabel")
        self.verticalLayout_3.addWidget(self.playersLabel)
        self.playersList = QtWidgets.QListWidget(EvaluateTeamDialog)
        self.playersList.setObjectName("playersList")
        self.verticalLayout_3.addWidget(self.playersList)
        self.listsContainer.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.listsContainer.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pointsByPlayerLabel = QtWidgets.QLabel(EvaluateTeamDialog)
        self.pointsByPlayerLabel.setObjectName("pointsByPlayerLabel")
        self.verticalLayout_4.addWidget(self.pointsByPlayerLabel)
        self.pointsList = QtWidgets.QListWidget(EvaluateTeamDialog)
        self.pointsList.setObjectName("pointsList")
        self.verticalLayout_4.addWidget(self.pointsList)
        self.listsContainer.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.listsContainer)
        self.comboBoxesContainer = QtWidgets.QWidget(EvaluateTeamDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxesContainer.sizePolicy().hasHeightForWidth())
        self.comboBoxesContainer.setSizePolicy(sizePolicy)
        self.comboBoxesContainer.setObjectName("comboBoxesContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.comboBoxesContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calcaulateScoreButton = QtWidgets.QPushButton(self.comboBoxesContainer)
        self.calcaulateScoreButton.setObjectName("calcaulateScoreButton")
        self.horizontalLayout_3.addWidget(self.calcaulateScoreButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.totalPointsLabel = QtWidgets.QLabel(self.comboBoxesContainer)
        self.totalPointsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalPointsLabel.setObjectName("totalPointsLabel")
        self.horizontalLayout_3.addWidget(self.totalPointsLabel)
        self.verticalLayout_2.addWidget(self.comboBoxesContainer)

        self.retranslateUi(EvaluateTeamDialog)
        QtCore.QMetaObject.connectSlotsByName(EvaluateTeamDialog)

        # connecting to db
        self.connect_to_db()

        # poulating ui and fetching teams, players and matches at start
        self.populate_ui()

        # adding combo box handlers
        self.teamComboBox.activated.connect(self.team_combo_handler)
        # manually calling once to populate data of first team
        self.team_combo_handler(0)

        # adding calculate button handler
        self.calcaulateScoreButton.clicked.connect(self.calculate_points)

    def retranslateUi(self, EvaluateTeamDialog):
        _translate = QtCore.QCoreApplication.translate
        EvaluateTeamDialog.setWindowTitle(_translate("EvaluateTeamDialog", "Evaluate Team"))
        self.label.setText(_translate("EvaluateTeamDialog", "Evaluate Your Fantasy Cricket Team"))
        self.teamLabel.setText(_translate("EvaluateTeamDialog", "Team: "))
        self.matchLabel.setText(_translate("EvaluateTeamDialog", "Match: "))
        self.playersLabel.setText(_translate("EvaluateTeamDialog", "Players"))
        self.pointsByPlayerLabel.setText(_translate("EvaluateTeamDialog", "Points by Player"))
        self.calcaulateScoreButton.setText(_translate("EvaluateTeamDialog", "Calculate Score"))
        self.totalPointsLabel.setText(_translate("EvaluateTeamDialog", "Total Points: 0"))
    
    def team_combo_handler(self, index):
        team_name = self.teamComboBox.itemText(index)
        team = self.teams[team_name]

        # populating players list widget
        self.playersList.clear()
        for player in team['players']:
            self.playersList.addItem(player)

        # reset points list and counter
        self.pointsList.clear()
        self.totalPointsLabel.setText('Total Points: 0')
    

    def fetch_matches(self):
        matches = { "match" : {} }
        self.cricket_db_cursor.execute('SELECT player, scored, faced, fours, sixes, bowled, maiden, given, wkts, catches, stumping, ro FROM match')
        for record in self.cricket_db_cursor.fetchall():
            matches['match'].update({ record[0]: {
                    "player": record[0],
                    "scored": record[1],
                    "faced": record[2],
                    "fours": record[3],
                    "sixes": record[4],
                    "bowled": record[5],
                    "maiden": record[6],
                    "given": record[7],
                    "wkts": record[8],
                    "catches": record[9],
                    "stumping": record[10],
                    "ro": record[11]
                }
            })
        
        return matches

    def fetch_players(self):
        players = {}
        try:
            self.cricket_db_cursor.execute('SELECT player, value, ctg FROM stats')
            for record in self.cricket_db_cursor.fetchall():
                players.update({ record[0]: {
                        "name": record[0],
                        "value": record[1],
                        "ctg": record[2]
                    }
                })
        except Exception as error:
            raise error

        return players

    def fetch_teams(self):
        teams = {}
        try:
            self.cricket_db_cursor.execute('SELECT name, players, value FROM teams')
        except Exception as error:
            raise error
        
        for record in self.cricket_db_cursor.fetchall():
            teams.update({
                record[0]: {
                    "name": record[0],
                    "players": record[1].split(':'),
                    "value": record[2]
                }
            }) 
        
        return teams

    def calculate_points(self):
        # clear points list
        self.pointsList.clear()

        # selected team and match
        team = self.teams[self.teamComboBox.currentText()]
        match = self.matches[self.matchComboBox.currentText()]
        score_by_player = {}
        total_score = 0

        for player in team['players']:
            score = self.calculate_points_for_player(match[player]) 
            score_by_player.update(score)
            total_score += score[player]

            # adding player score to list
            self.pointsList.addItem(str(score[player]))
        
        # update total points
        self.totalPointsLabel.setText(f'Total Points: {total_score}')

    def calculate_points_for_player(self, data):
        player_points = 0
        # batting
        player_points += data['scored']//2 # 1 pt for for 2 runs
        player_points += 5 if data['scored'] >= 50 else 0 # 5 points for half century
        player_points += 10 if data['scored'] >= 100 else 0 # 10 points for  century
        strike_rate = 0
        try:
            strike_rate = round((data['scored']/data['faced'] * 100))
        except Exception as error:
            print(f'ERROR: {error}')
        player_points += 2 if strike_rate >= 80 else 0 # 2 points for strike rate 80-100
        player_points += 4 if strike_rate > 100 else 0 # 4 addition points for stirke rate > 100
        player_points += data['fours'] # 1 points for 4
        player_points += 2 * data['sixes'] # 2 points for 6

        # bowling
        player_points += 10 * data['wkts'] # 10 for each wicket
        player_points += 5 if data['wkts'] >= 3 else 0 # additional 5 points for 3 wickets
        player_points += 10 if data['wkts'] >= 5 else 0 # addition 10 points for 3 wickets
        economy_rate = None
        try:
            economy_rate = data['given']/(data['bowled']/6) # runs given per over
        except Exception as error:
            print(f'ERROR: {error}')

        if(economy_rate):
            player_points += 4 if economy_rate >= 3.5 and economy_rate < 4.5 else 0 # 10 points if economy rate less than 2
            player_points += 7 if economy_rate >= 2 and economy_rate < 3.5 else 0 # 10 points if economy rate b/w 2 and 3.5
            player_points += 10 if economy_rate < 2 else 0 # 10 points if economy rate less than 2

        # fielding
        player_points += 10 *  (data['catches'] + data['stumping'] + data['ro']) # 10 points each for catch, stumping or run out

        return {data['player']: player_points}

    def populate_ui(self):
        # adding teams to comboBox
        try:
            self.teams = self.fetch_teams()
            for team in self.teams.keys():
                self.teamComboBox.addItem(team)
        except Exception as error:
            print(f'ERROR: {error}')
        
        # adding match to comboBox
        try:
            self.matches = self.fetch_matches()
            for match in self.matches.keys():
                self.matchComboBox.addItem(match)
        except Exception as error:
            raise error

        # fetching all players
        try:
            self.total_players = self.fetch_players()
        except Exception as error:
            raise error
        
    
    def connect_to_db(self):
        import sqlite3

        self.cricket_db = sqlite3.connect('fantasy-cricket.db')
        self.cricket_db_cursor = self.cricket_db.cursor()
    
    def disconnect_db(self):
        self.cricket_db.close()

if __name__ == "__main__":
    import sys

    # ui initialization
    app = QtWidgets.QApplication(sys.argv)
    EvaluateTeamDialog = QtWidgets.QDialog()
    ui = Ui_EvaluateTeamDialog()
    ui.setupUi(EvaluateTeamDialog)
    EvaluateTeamDialog.show()
    sys.exit(app.exec_())
