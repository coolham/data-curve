import sys
from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton


class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.status_label = QLabel("Status: Ready", self)
        # self.status_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        self.layout.addWidget(self.status_label)

        # # Control buttons
        self.start_button = QPushButton("Start", self)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop", self)
        self.layout.addWidget(self.stop_button)


        # self.label = QLabel("This is Tab 2")
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.label)
        # self.setLayout(self.layout)

        self.setLayout(self.layout)
