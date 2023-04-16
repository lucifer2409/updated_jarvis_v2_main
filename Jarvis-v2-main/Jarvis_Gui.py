from Jarvis_Ui import Ui_Jarvisui
from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt , QTimer , QTime , QDate
from PyQt6.uic import loadUiType
import main_file
import sys

class MainThread(QThread):


    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        main_file.__name__()

start_Execution = MainThread()

def Start_Task(self):
    self.gui.label1 = QtGui.QMovie("Downloads/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/Jarvis_Gui (1).gif")
    self.gui.gif_1.setMovie(self.gui.label1)
    self.gui.label1.start()

    self.gui.label2 = QtGui.QMovie("Downloads/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/Earth.gif")
    self.gui.gif_2.setMovie(self.gui.label2)
    self.gui.label2.start()

    self.gui.label3 = QtGui.QMovie("Downloads/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/Code_Template.gif")
    self.gui.gif_3.setMovie(self.gui.label3)
    self.gui.label3.start()

    self.gui.label4 = QtGui.QMovie("Downloads/jarvis_materials/drive-download-20230414T100055Z-001/ExtraGui/initial.gif")
    self.gui.gif_4.setMovie(self.gui.label4)
    self.gui.label4.start()

    start_Execution.start()
class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_Jarvisui()
        self.gui.setupUi(self)

        self.gui.Start_Push_Button.clicked.connect(self.Start_Task)
        self.gui.Stop_Push_Button.clicked.connect(self.Close_Task)




Gui_App = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(Gui_App._exec())