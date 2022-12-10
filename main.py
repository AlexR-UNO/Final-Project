from controller_main import *
from view import *
import sys


def main():
    application = QtWidgets.QApplication(sys.argv)
    window = mainGUI()
    window.setupUi(window)
    window.runFollowupSetupCommands()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()
