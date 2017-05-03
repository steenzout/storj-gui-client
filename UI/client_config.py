from PyQt4 import QtCore, QtGui
from .utilities.backend_config import Configuration
from .qt_interfaces.settings_ui_new import Ui_ClientConfiguration
from .utilities.log_manager import logger
from .utilities.account_manager import AccountManager


# Configuration Ui section
class ClientConfigurationUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # register UI
        self.client_configuration_ui = Ui_ClientConfiguration()
        self.client_configuration_ui.setupUi(self)

        self.configuration_manager = Configuration()
        self.account_manager = AccountManager()

        QtCore.QObject.connect(self.client_configuration_ui.apply_bt, QtCore.SIGNAL('clicked()'),
                               self.save_settings)  # save settings action

        QtCore.QObject.connect(self.client_configuration_ui.cancel_bt, QtCore.SIGNAL('clicked()'),
                               self.close)  # close form

        QtCore.QObject.connect(self.client_configuration_ui.crypto_keys_location_select_bt, QtCore.SIGNAL('clicked()'),
                               self.select_crypto_keys_path)  # open path select

        QtCore.QObject.connect(self.client_configuration_ui.logout_bt, QtCore.SIGNAL('clicked()'),
                               self.handle_logout_action)  # logout

        QtCore.QObject.connect(self.client_configuration_ui.clear_logs_bt, QtCore.SIGNAL('clicked()'),
                               self.handle_clear_logs_action)  # clear logs

        QtCore.QObject.connect(self.client_configuration_ui.restore_to_default_bt, QtCore.SIGNAL('clicked()'),
                               self.reset_settings_to_default)  # restore to default settings




        self.configuration_manager.paint_config_to_ui(self.client_configuration_ui)


    def handle_logout_action(self):
        msgBox = QtGui.QMessageBox(
            QtGui.QMessageBox.Question,
            'Question',
            'Are you sure that you want to logout?',
            (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))

        result = msgBox.exec_()
        #self.__logger.debug(result)

        if result == QtGui.QMessageBox.Yes:
            logged_out = self.account_manager.logout()
            if logged_out:
                QtGui.QMessageBox.about(self, 'Success', 'Successfully logged out!')


    def select_crypto_keys_path(self):
        self.client_configuration_ui.crypto_keys_location.setText(str(QtGui.QFileDialog.getSaveFileName(
          self, 'Save file to...', 'storj_client_keyring.sjkr')))

    def save_settings(self):
        # validate settings

        self.configuration_manager.save_client_configuration(self.client_configuration_ui)  # save configuration
        QtGui.QMessageBox.about(self, 'Success', 'Configuration saved successfully!')

    def handle_clear_logs_action(self):
        msgBox = QtGui.QMessageBox(
            QtGui.QMessageBox.Question,
            'Question',
            'Are you sure that you want to clear all logs?',
            (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))

        result = msgBox.exec_()

        if result == QtGui.QMessageBox.Yes:
            QtGui.QMessageBox.about(self, 'Success', 'All logs have been successfully cleared!')


    def reset_settings_to_default(self):
        msgBox = QtGui.QMessageBox(
            QtGui.QMessageBox.Question,
            'Question',
            'Are you sure that you want to restore to default settings?',
            (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))

        result = msgBox.exec_()
        if result == QtGui.QMessageBox.Yes:
            QtGui.QMessageBox.about(self, 'Success', 'Settings successfully restored to default!')
        logger.debug(1)
