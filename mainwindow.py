# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 755)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.black_bg = QtWidgets.QLabel(parent=self.centralwidget)
        self.black_bg.setGeometry(QtCore.QRect(-60, -50, 1581, 811))
        self.black_bg.setText("")
        self.black_bg.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/B.G/Black_Template.jpg"))
        self.black_bg.setScaledContents(True)
        self.black_bg.setObjectName("black_bg")
        self.gif_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(490, 230, 441, 261))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/Jarvis_Gui (1).gif"))
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.gif_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gif_2.setGeometry(QtCore.QRect(430, 50, 581, 141))
        self.gif_2.setText("")
        self.gif_2.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/initial.gif"))
        self.gif_2.setScaledContents(True)
        self.gif_2.setObjectName("gif_2")
        self.gif_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gif_3.setGeometry(QtCore.QRect(20, 540, 391, 201))
        self.gif_3.setText("")
        self.gif_3.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/Code_Template.gif"))
        self.gif_3.setScaledContents(True)
        self.gif_3.setObjectName("gif_3")
        self.gif_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gif_4.setGeometry(QtCore.QRect(1180, 40, 211, 151))
        self.gif_4.setText("")
        self.gif_4.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/Earth.gif"))
        self.gif_4.setScaledContents(True)
        self.gif_4.setObjectName("gif_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1200, 260, 191, 61))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(24, 243, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1200, 340, 191, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(24, 243, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.bg_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(1010, 520, 401, 231))
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/B.G/gyhf.jpg"))
        self.bg_2.setScaledContents(True)
        self.bg_2.setObjectName("bg_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1070, 550, 281, 51))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1070, 670, 281, 51))
        self.textBrowser_2.setStyleSheet("background-color:transparent;\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gif_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gif_5.setGeometry(QtCore.QRect(10, 20, 351, 221))
        self.gif_5.setText("")
        self.gif_5.setPixmap(QtGui.QPixmap("../Downloads/Jarvis_Gui_Materials-main/Jarvis_Gui_Materials-main/jarvis_materials/drive-download-20230414T100055Z-001/VoiceReg/__1.gif"))
        self.gif_5.setScaledContents(True)
        self.gif_5.setObjectName("gif_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
