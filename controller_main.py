from PyQt5.QtWidgets import *


import view
import Unified_Document_Reader.view
import Shape_Size_Calculator.view
import sys
import Unified_Document_Reader.controller_unified
import Shape_Size_Calculator.controller_shape

# from main import *

application_secondary = view.QtWidgets.QApplication(sys.argv)


class mainGUI(QMainWindow, view.Ui_MainWindow):
    def __int__(self):
        super().__init__()

    def runFollowupSetupCommands(self) -> None:
        """
        Builds the application, since the constructor is still finicky.

        :return: Nothing
        """

        self.window_unified = Unified_Document_Reader.controller_unified.unifiedDocumentReader()
        self.window_unified.setupUi(self.window_unified)
        self.window_unified.runFollowupSetupCommands()

        self.window_shapes = Shape_Size_Calculator.controller_shape.shapeSizeCalculator()
        self.window_shapes.setupUi(self.window_shapes)
        self.window_shapes.runFollowupSetupCommands()

        self.pushButton_exec_button.pressed.connect(self.executeSelection)

        self.setFixedSize(self.size())

    def executeSelection(self) -> None:

        if self.comboBox_program_selection.currentIndex() == 0:
            self.window_shapes.show()

        if self.comboBox_program_selection.currentIndex() == 1:
            self.window_unified.show()

        if self.comboBox_program_selection.currentIndex() == 2:
            self.window_shapes.close()
            self.window_unified.close()
            self.close()
