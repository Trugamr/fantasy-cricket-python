# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_evaluageTeamDialog(object):
    def setupUi(self, evaluageTeamDialog):
        evaluageTeamDialog.setObjectName("evaluageTeamDialog")
        evaluageTeamDialog.resize(524, 485)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(evaluageTeamDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topContainer = QtWidgets.QWidget(evaluageTeamDialog)
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
        self.playersLabel = QtWidgets.QLabel(evaluageTeamDialog)
        self.playersLabel.setObjectName("playersLabel")
        self.verticalLayout_3.addWidget(self.playersLabel)
        self.playersList = QtWidgets.QListWidget(evaluageTeamDialog)
        self.playersList.setObjectName("playersList")
        self.verticalLayout_3.addWidget(self.playersList)
        self.listsContainer.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.listsContainer.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pointsByPlayerLabel = QtWidgets.QLabel(evaluageTeamDialog)
        self.pointsByPlayerLabel.setObjectName("pointsByPlayerLabel")
        self.verticalLayout_4.addWidget(self.pointsByPlayerLabel)
        self.pointsList = QtWidgets.QListWidget(evaluageTeamDialog)
        self.pointsList.setObjectName("pointsList")
        self.verticalLayout_4.addWidget(self.pointsList)
        self.listsContainer.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.listsContainer)
        self.comboBoxesContainer = QtWidgets.QWidget(evaluageTeamDialog)
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

        self.retranslateUi(evaluageTeamDialog)
        QtCore.QMetaObject.connectSlotsByName(evaluageTeamDialog)

    def retranslateUi(self, evaluageTeamDialog):
        _translate = QtCore.QCoreApplication.translate
        evaluageTeamDialog.setWindowTitle(_translate("evaluageTeamDialog", "Evaluate Team"))
        self.label.setText(_translate("evaluageTeamDialog", "Evaluate You Fantasy Cricket Team"))
        self.teamLabel.setText(_translate("evaluageTeamDialog", "Team: "))
        self.matchLabel.setText(_translate("evaluageTeamDialog", "Match: "))
        self.playersLabel.setText(_translate("evaluageTeamDialog", "Players"))
        self.pointsByPlayerLabel.setText(_translate("evaluageTeamDialog", "Points by Player"))
        self.calcaulateScoreButton.setText(_translate("evaluageTeamDialog", "Calculate Score"))
        self.totalPointsLabel.setText(_translate("evaluageTeamDialog", "Total Points: 0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluageTeamDialog = QtWidgets.QDialog()
    ui = Ui_evaluageTeamDialog()
    ui.setupUi(evaluageTeamDialog)
    evaluageTeamDialog.show()
    sys.exit(app.exec_())