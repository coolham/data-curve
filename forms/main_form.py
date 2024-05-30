import time
import queue
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QVBoxLayout, QMessageBox


from utils.config import MasterConfig
from utils.logger_factory import create_logger
from version import VERSION
from forms.rt_curve_form import RtCurveForm
from forms.tab2_form import Tab2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logger = create_logger()
        self.config = MasterConfig()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.setMinimumSize(800, 600)
        
        # Create the tab widget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Create the first tab
        self.tab1 = RtCurveForm()

        # Create the second tab
        self.tab2 = Tab2()
       
        # Add the tabs to the tab widget
        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")




