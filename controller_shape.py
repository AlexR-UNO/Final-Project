from PyQt5.QtWidgets import *

from Shape_Size_Calculator import view
from Shape_Size_Calculator.view import *
from Shape_Size_Calculator.Shapes.area import *
from Shape_Size_Calculator.Shapes.perimeter import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class shapeSizeCalculator(QMainWindow, view.Ui_MainWindow):
    def __int__(self):
        super().__init__()

    def runFollowupSetupCommands(self) -> None:
        """
        Builds the application, since the constructor is still finicky.

        :return: Nothing
        """
        self.label_prompt_1.setHidden(False)
        self.lineEdit_prompt_1.setHidden(False)

        self.label_prompt_2.setHidden(True)
        self.lineEdit_prompt_2.setHidden(True)

        self.label_prompt_3.setHidden(True)
        self.lineEdit_prompt_3.setHidden(True)

        self.radioButton_circle.setChecked(True)
        self.radioButton_area.setChecked(True)
        self.radioButton_circle.toggled.connect(self.radioButtonToggle)
        self.radioButton_triangle.toggled.connect(self.radioButtonToggle)
        self.radioButton_square.toggled.connect(self.radioButtonToggle)
        self.radioButton_rectangle.toggled.connect(self.radioButtonToggle)
        self.radioButton_area.toggled.connect(self.radioButtonToggle)
        self.radioButton_perimeter.toggled.connect(self.radioButtonToggle)

        self.button_calculate.pressed.connect(self.calcuateButton)

        self.setFixedSize(self.size())

    def validateInput(self, shape: str = "circle", calculation: str = "area") -> str:
        """
        Takes user input from GUI, ensures the input is of the proper format,
        calls for a calculation based on the given arguments, then returns the answer as a string.

        :param shape: (str) "circle", "rectangle", "square", or "triangle"
        :param calculation: (str) "area" or "perimeter"
        :return: (str) The result of the chosen shape's chosen calculation, i.e, area of a circle.
        """

        msg_box = QMessageBox()

        print("Validating Input")

        output = ""

        try:

            if calculation == "area":

                if shape == "circle":

                    return str(area_circle(float(self.lineEdit_prompt_1.text())))

                elif shape == "rectangle":

                    return str(area_rectangle(float(self.lineEdit_prompt_1.text()),
                                              float(self.lineEdit_prompt_2.text())))

                elif shape == "square":

                    return str(area_square(float(self.lineEdit_prompt_1.text())))

                elif shape == "triangle":

                    return str(area_triangle(float(self.lineEdit_prompt_1.text()),
                                             float(self.lineEdit_prompt_2.text())))

            elif calculation == "perimeter":

                if shape == "circle":

                    return str(peri_circle(float(self.lineEdit_prompt_1.text())))

                elif shape == "rectangle":

                    return str(peri_rectangle(float(self.lineEdit_prompt_1.text()),
                                              float(self.lineEdit_prompt_2.text())))

                elif shape == "square":

                    return str(peri_square(float(self.lineEdit_prompt_1.text())))

                elif shape == "triangle":

                    return str(peri_triangle(float(self.lineEdit_prompt_1.text()),
                                             float(self.lineEdit_prompt_2.text()),
                                             float(self.lineEdit_prompt_3.text())))

        except ValueError:
            output = "ERROR: ValueError"
            msg_box.setText("Warning: Please Enter Valid Numbers")
            # msg_box.show() Currently Non-Functional - Work on this later
            return output
        except TypeError:
            output = "ERROR: TypeError"
            msg_box.setText("Warning: Please Enter Valid Numbers")
            # msg_box.show() Currently Non-Functional - Work on this later
            return output

    def calcuateButton(self) -> None:
        """
        Fires when the calculate button is pressed; sets output to its new value.

        :return: Nothing
        """
        print("Button pressed")

        if self.radioButton_circle.isChecked():

            if self.radioButton_area.isChecked():

                self.lineEdit_output.setText(self.validateInput("circle", "area"))

            elif self.radioButton_perimeter.isChecked():

                self.lineEdit_output.setText(self.validateInput("circle", "perimeter"))

        elif self.radioButton_rectangle.isChecked():

            if self.radioButton_area.isChecked():

                self.lineEdit_output.setText(self.validateInput("rectangle", "area"))

            elif self.radioButton_perimeter.isChecked():

                self.lineEdit_output.setText(self.validateInput("rectangle", "perimeter"))

        elif self.radioButton_square.isChecked():

            if self.radioButton_area.isChecked():

                self.lineEdit_output.setText(self.validateInput("square", "area"))

            elif self.radioButton_perimeter.isChecked():

                self.lineEdit_output.setText(self.validateInput("square", "perimeter"))

        elif self.radioButton_triangle.isChecked():

            if self.radioButton_area.isChecked():

                self.lineEdit_output.setText(self.validateInput("triangle", "area"))

            elif self.radioButton_perimeter.isChecked():

                self.lineEdit_output.setText(self.validateInput("triangle", "perimeter"))

    def radioButtonToggle(self) -> None:
        """
        When a radiobutton is toggled, reveals/hides relevant input boxes.

        :return: Nothing
        """
        if self.radioButton_circle.isChecked():

            self.label_prompt_1.setHidden(False)
            self.lineEdit_prompt_1.setHidden(False)
            self.label_prompt_1.setText("Circle Radius")

            self.label_prompt_2.setHidden(True)
            self.lineEdit_prompt_2.setHidden(True)

            self.label_prompt_3.setHidden(True)
            self.lineEdit_prompt_3.setHidden(True)

            if self.radioButton_area.isChecked():
                self.label_output.setText("Area of Circle")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Area")

            elif self.radioButton_perimeter.isChecked():
                self.label_output.setText("Perimeter of Circle")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Perimeter")

        elif self.radioButton_rectangle.isChecked():

            self.label_prompt_1.setHidden(False)
            self.lineEdit_prompt_1.setHidden(False)
            self.label_prompt_1.setText("Rectangle Length")

            self.label_prompt_2.setHidden(False)
            self.lineEdit_prompt_2.setHidden(False)
            self.label_prompt_2.setText("Rectangle Width")

            self.label_prompt_3.setHidden(True)
            self.lineEdit_prompt_3.setHidden(True)

            if self.radioButton_area.isChecked():
                self.label_output.setText("Area of Rectangle")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Area")

            elif self.radioButton_perimeter.isChecked():
                self.label_output.setText("Perimeter of Rectangle")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Perimeter")

        elif self.radioButton_square.isChecked():

            self.label_prompt_1.setHidden(False)
            self.lineEdit_prompt_1.setHidden(False)
            self.label_prompt_1.setText("Square Side Length")

            self.label_prompt_2.setHidden(True)
            self.lineEdit_prompt_2.setHidden(True)

            self.label_prompt_3.setHidden(True)
            self.lineEdit_prompt_3.setHidden(True)

            if self.radioButton_area.isChecked():
                self.label_output.setText("Area of Square")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Area")

            elif self.radioButton_perimeter.isChecked():
                self.label_output.setText("Perimeter of Square")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Perimeter")

        elif self.radioButton_triangle.isChecked():

            self.label_prompt_1.setHidden(False)
            self.lineEdit_prompt_1.setHidden(False)
            self.label_prompt_1.setText("Triangle Length")

            self.label_prompt_2.setHidden(False)
            self.lineEdit_prompt_2.setHidden(False)
            self.label_prompt_2.setText("Triangle Width")

            self.label_prompt_3.setHidden(True)
            self.lineEdit_prompt_3.setHidden(True)

            if self.radioButton_area.isChecked():
                self.label_output.setText("Area of Triangle")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Area")

            elif self.radioButton_perimeter.isChecked():
                self.label_prompt_3.setHidden(False)
                self.lineEdit_prompt_3.setHidden(False)

                self.label_prompt_1.setText("Triangle Side 1")
                self.label_prompt_2.setText("Triangle Side 2")
                self.label_prompt_3.setText("Triangle Side 3")

                self.label_output.setText("Perimeter of Triangle")
                self.lineEdit_output.setText("")
                self.button_calculate.setText("Calculate Perimeter")
