from PyQt5.QtWidgets import QMainWindow


from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """
    Current class describe application main window
    """

    def __init__(self):
        super(MainWindow, self).__init__()  # call parent constructor

        # initialize all UI elements
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
