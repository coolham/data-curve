import sys
from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout

from forms.rt_curve_area import RtCurveArea
from forms.rt_control_area import RtCurveControl


class RtCurveForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # Curve area
        self.curve_area = RtCurveArea(self)
        self.layout.addWidget(self.curve_area, 5)

        # Status and control area
        self.status_control_area = RtCurveControl(self)
        self.layout.addWidget(self.status_control_area, 1)


