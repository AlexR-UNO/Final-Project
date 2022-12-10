from PyQt5.QtWidgets import *

from Unified_Document_Reader import view
from Unified_Document_Reader.view import *

import requests
import bs4

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class unifiedDocumentReader(QMainWindow, view.Ui_MainWindow):
    def __int__(self):
        super().__init__()

    def runFollowupSetupCommands(self) -> None:
        """
        Builds the application, since the constructor is still finicky.

        :return: Nothing
        """

        self.pushButton_retrieve_document.pressed.connect(self.retrieve_document)

        self.setFixedSize(self.size())

    def retrieve_document(self):

        if 'archiveofourown.org' not in self.lineEdit_url.text():
            self.textBrowser_viewer.setText(f'File Name: NYI\n'
                                            f'File URL: {self.lineEdit_url.text()}\n'
                                            f'-------------\n'
                                            f'Document Not Found')
            return

        html_document = requests.get(self.lineEdit_url.text())

        # print(html_document.text)

        try:
            html_document.raise_for_status()
        except Exception as e:
            print("That didn't Work. Here's Why: %s" % e)

        html_parser = bs4.BeautifulSoup(html_document.text, 'html.parser')

        story_content = html_parser.select('div.userstuff.module p')

        print(story_content)

        self.textBrowser_viewer.setText(f'File Name: NYI\n'
                                        f'File URL: {self.lineEdit_url.text()}\n'
                                        f'-------------')
        for line in story_content:
            self.textBrowser_viewer.append(line.getText())


