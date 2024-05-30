import sys
import time
from PyQt6.QtCore import QTimer, QPoint
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QPushButton, QVBoxLayout




class RtCurveControl(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        # Layout
        self.layout = QVBoxLayout()

        self.status_label = QLabel("Status: Ready", self)
        self.layout.addWidget(self.status_label)

        # Control buttons
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop)
        self.layout.addWidget(self.stop_button)


    def start(self):
        self.status_label.setText("Status: Running")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop(self):
        self.status_label.setText("Status: Stopped")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)