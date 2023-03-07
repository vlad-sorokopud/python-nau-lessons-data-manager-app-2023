from PyQt5.QtWidgets import QMainWindow, QFileDialog


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

        # bind button events
        self.ui.welcome_page_data_mode_button.clicked.connect(self.go_to_data_mode_page)
        self.ui.welcome_page_cv_mode_button.clicked.connect(self.go_to_cv_mode_page)
        self.ui.data_mode_page_file_button.clicked.connect(self.on_data_mode_page_select_file_button_clicked)

    # ------- UI EVENTS --------------------------------------------------------------------------------------------- #

    def on_data_mode_page_select_file_button_clicked(self):
        # print("On method {0}".format("on_data_mode_page_select_file_button_clicked"))

        file, check = QFileDialog.getOpenFileName(None, "Select data file", "",
                                                  "Text Files (*.txt);;All Files (*)")

        if not check:
            return

    # ------- UI ACTION --------------------------------------------------------------------------------------------- #

    def go_to_data_mode_page(self):
        print("On method {0}".format("go_to_data_mode_page"))
        self.ui.stacked_widget.setCurrentIndex(1)

    def go_to_cv_mode_page(self):
        # print("On method {0}".format("go_to_cv_mode_page"))
        self.ui.stacked_widget.setCurrentIndex(2)


