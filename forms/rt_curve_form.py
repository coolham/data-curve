import sys
from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout


class RtCurveForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("This is Tab 1")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


        