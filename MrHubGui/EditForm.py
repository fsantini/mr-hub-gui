from PySide2.QtGui import QRegExpValidator

from .edit_form_ui import Ui_EditFormWindow
from .github_credentials_ui import Ui_GithubCredentialsDialog
from PySide2.QtWidgets import QMainWindow, QHeaderView, QFileDialog, QMessageBox, QDialog, QInputDialog
from PySide2.QtCore import QAbstractTableModel, Qt, Slot, QRegExp
import json
import requests
from .GitTools import check_git_settings, initialize_github, copy_image, add_package, get_push_command_help


class GithubCredentialsDialog(QDialog, Ui_GithubCredentialsDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.userpass_widget.setVisible(False)
        self.buttonBox.accepted.connect(lambda: self.exit_dialog(True))
        self.buttonBox.rejected.connect(lambda: self.exit_dialog(False))
        self.localFolder_Browse_Button.clicked.connect(self.browse_folder)

        branchValidator = QRegExpValidator(QRegExp(r'[A-Za-z0-9_-]+'))
        self.newBranch_text.setValidator(branchValidator)

        self.credentials = None
        self.accepted = False
        self.local_folder = None
        self.branch = None

        self.setModal(True)

    def browse_folder(self):
        d = QFileDialog.getExistingDirectory(self, 'Select the folder for the local repository')
        self.localFolder_text.setText(d)

    def exit_dialog(self, accepted):
        self.accepted = accepted
        self.close()

    def closeEvent(self, event):
        if self.userpass_radio.isChecked():
            self.credentials = (self.username_text.text(), self.password_text.text())
        else:
            self.credentials = self.accessToken_text.text()
        self.local_folder = self.localFolder_text.text()
        self.branch = self.newBranch_text.text()


class TableModel(QAbstractTableModel):
    def __init__(self, header):
        QAbstractTableModel.__init__(self)
        self.ncols = len(header)
        self.header = header
        self.keywordList = []

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]
            else:
                return str(section+1)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.keywordList[index.row()][self.header[index.column()]]

    def rowCount(self, index):
        return len(self.keywordList)

    def columnCount(self, index):
        return self.ncols

    def setData(self, index, value, role=None):
        if role == Qt.EditRole:
            self.keywordList[index.row()][self.header[index.column()]] = value
            return True

    def flags(self, index):
        return Qt.ItemIsEditable | QAbstractTableModel.flags(self, index)

    def insertRow(self, row, parent=None, *args, **kwargs):
        self.keywordList.insert(row, {k:'' for k in self.header})
        print("inserting row. Len", len(self.keywordList))
        self.layoutChanged.emit()
        return True

    def appendRow(self):
        return self.insertRow(len(self.keywordList)+1)

    def deleteRow(self, row):
        del self.keywordList[row]
        self.layoutChanged.emit()

    def getList(self):
        return self.keywordList

    def setList(self, dataList):
        self.keywordList = dataList
        self.layoutChanged.emit()

def table_row_delete(model, view):
    try:
        row = view.selectedIndexes()[0].row()
    except:
        print('No row selected')
        return
    model.deleteRow(row)
    

class EditForm(QMainWindow, Ui_EditFormWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('MR-HUB GUI')

        self.keyword_model = TableModel(['Keyword'])
        self.keywords_table.setModel(self.keyword_model)
        self.keywords_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.addKeyword_button.clicked.connect(self.keyword_model.appendRow)
        self.removeKeyword_button.clicked.connect(lambda : table_row_delete(self.keyword_model, self.keywords_table))

        self.reference_model = TableModel(['Description', 'URL'])
        self.reference_table.setModel(self.reference_model)
        self.reference_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addReference_button.clicked.connect(self.reference_model.appendRow)
        self.removeReference_button.clicked.connect(lambda : table_row_delete(self.reference_model, self.reference_table))

        self.extraResources_model = TableModel(['Resource type', 'URL'])
        self.extraResources_Table.setModel(self.extraResources_model)
        self.extraResources_Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addExtraResources_button.clicked.connect(self.extraResources_model.appendRow)
        self.removeExtraResources_button.clicked.connect(lambda: table_row_delete(self.extraResources_model, self.extraResources_Table))

        self.imageBrowse_button.clicked.connect(self.set_image_path)

        self.actionLoad_JSON.triggered.connect(self.loadJSON)
        self.actionSave_JSON.triggered.connect(self.saveJSON)

        self.actionUpload_to_MR_HUB.triggered.connect(self.prepare_mr_hub)

        self.citationTest_button.clicked.connect(self.test_semantic_scholar)

    def get_output_dict(self):
        def make_keyword_list():
            return [v['Keyword'] for v in self.keyword_model.getList()]

        def make_reference_list():
            return [{'referenceText': v['Description'], 'referenceURL': v['URL']} for v in
                    self.reference_model.getList()]

        def make_resource_list():
            return [{'resourceType': v['Resource type'], 'URL': v['URL']} for v in
                    self.extraResources_model.getList()]

        output = {
            'name': self.name_text.text(),
            'category': self.category_box.currentText(),
            'shortDescription': self.shortDescription_text.text(),
            'imageFile': self.imageFilename_text.text(),
            'mainURL': self.mainURL_text.text(),
            'repoURL': self.repoURL_text.text(),
            'principalDevelopers': self.principalDevelopers_text.text(),
            'longDescription': self.longDescription_text.toPlainText(),
            'keywords': make_keyword_list(),
            'keyReferences': make_reference_list(),
            'extraResources': make_resource_list(),
            'dateAddedToMRHub': self.dateAdded_text.text(),
            'dateSoftwareLastUpdated': self.dateUpdated_text.text(),
            'citationSearchString': self.citationString_text.text(),
            'citationCount': ''
        }

        return output

    def load_dict(self, input):
        def load_keyword_list(keywords):
            self.keyword_model.setList(
                [{'Keyword': k} for k in keywords]
            )

        def load_reference_list(references):
            self.reference_model.setList(
                [{'Description': v['referenceText'],
                  'URL': v['referenceURL']} for v in references]
            )

        def load_resource_list(resources):
            self.extraResources_model.setList(
                [{'Resource type': v['resourceType'],
                  'URL': v['URL']} for v in resources]
            )

        self.name_text.setText(input['name'])
        self.category_box.setCurrentText(input['category'])
        self.shortDescription_text.setText(input['shortDescription'])
        self.imageFilename_text.setText(input['imageFile'])
        self.mainURL_text.setText(input['mainURL'])
        self.repoURL_text.setText(input['repoURL'])
        self.principalDevelopers_text.setText(input['principalDevelopers'])
        self.longDescription_text.setPlainText(input['longDescription'])
        load_keyword_list(input['keywords'])
        load_reference_list(input['keyReferences'])
        load_resource_list(input['extraResources'])
        self.dateAdded_text.setText(input['dateAddedToMRHub'])
        self.dateUpdated_text.setText(input['dateSoftwareLastUpdated'])
        self.citationString_text.setText(input['citationSearchString'])

    @Slot()
    def loadJSON(self):
        jsonFile, _ = QFileDialog.getOpenFileName(self, caption='Import JSON file',
                                                   filter='JSON files (*.json);;All files (*.*)')

        if not jsonFile: return
        inputDict = json.load(open(jsonFile, 'r'))
        try:
            self.load_dict(inputDict)
        except:
            QMessageBox.critical(self, 'JSON error', 'Malformed JSON File')

    @Slot()
    def saveJSON(self):
        jsonFile, _ = QFileDialog.getSaveFileName(self, caption='Save JSON file',
                                                  filter='JSON files (*.json);;All files (*.*)')

        if not jsonFile: return
        json.dump(self.get_output_dict(), open(jsonFile, 'w'), indent=2)

    @Slot()
    def test_semantic_scholar(self):
        base_url = 'https://api.semanticscholar.org/v1/paper/'
        ss_url = base_url + self.citationString_text.text()
        r = requests.get(ss_url)
        if r.status_code == 404:
            QMessageBox.critical(self, 'SemanticScholar error', 'Paper not found in Semantic Scholar')
        elif r.status_code == 200:
            QMessageBox.information(self, 'Paper found', 'The following paper was found:\n\n' + r.json()['title'])
        else:
            QMessageBox.critical(self, 'SemanticScholar error', 'Unspecified error with Semantic Scholar')

    @Slot()
    def set_image_path(self):
        image_path, _ = QFileDialog.getOpenFileName(self, caption='Select an image file',
                                                    filter='Image files (*.jpg *.png *.gif *.svg);;All files (*.*)')
        self.imagePath_text.setText(image_path)

    @Slot()
    def prepare_mr_hub(self):

        ans = QMessageBox.information(self, 'Forking the repo',
"""This will now create a Git repository that needs to be pushed to Github and from which a pull request can be created.

You need the Git executable to be present in the path and properly configured with a user name and email.
You also need a Github account.

The program will now:
1) fork the original mr-hub repository into your own Github account;
2) clone the repository locally;
3) create a new branch;
4) perform the required changes.

You will need to then push the changes to Github and create a pull request yourself. 
""", QMessageBox.Ok, QMessageBox.Cancel)

        if ans == QMessageBox.Cancel:
            return

        if not check_git_settings():
            QMessageBox.critical(self, 'Git error', 'Git Settings error. Either git is unavailable, or the username is not set.\n' +
                                                    'Install git and/or run the following commands:\n' +
                                                    'git config --global user.name <your username>\n' +
                                                    'git config --global user.email <your email>')

        credential_dialog = GithubCredentialsDialog(self)
        credential_dialog.exec_()
        if not credential_dialog.accepted:
            return

        credentials = credential_dialog.credentials

        if (isinstance(credentials, str) and not credentials) or (
                isinstance(credentials, tuple) and (not credentials[0] or not credentials[1])):
            QMessageBox.critical(self, 'Git error', 'Credentials cannot be empty')
            return


        new_branch = credential_dialog.branch
        if not new_branch:
            QMessageBox.critical(self, 'Git error', 'Specify a new branch name')
            return


        local_folder = credential_dialog.local_folder
        if not local_folder:
            QMessageBox.critical(self, 'Git error', 'Specify a folder to store the repository')
            return

        # initialize the github repo
        initialize_github(credentials, new_branch, local_folder)

        output_dict = self.get_output_dict()

        # if an image is specified, add it
        if self.imagePath_text.text() and output_dict['imageFile']:
            copy_image(self.imagePath_text.text(), output_dict['imageFile'])

        add_package(output_dict)

        QMessageBox.information(self, 'All done', 'Git repository modified!\n'+
                                get_push_command_help() +
                                '\nFinally, create a pull request from the new branch on github')