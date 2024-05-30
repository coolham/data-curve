import sys
import time
import random
import PyQt6
from PyQt6.QtCore import QTimer, QPoint
from PyQt6.QtGui import QPixmap, QColor, QPainter
from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QPushButton, QVBoxLayout
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph.exporters
from dao.data_model import DataModel



class RtCurveArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.max_data_points = 200
        self.init_ui()

        # Create data model
        self.data_model = DataModel()
        self.data_model.data_signal.connect(self.update_plot)

        # Start data generation
        self.data_model.start()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Create plot widget
        self.plot_widget = PlotWidget()
        self.plot_item = self.plot_widget.plotItem
        self.plot_item.showGrid(x=True, y=True)
        self.plot_item.setXRange(0, 10)
        self.plot_item.setYRange(0, 100)

        # Add plot widget to layout
        # self.setCentralWidget(self.plot_widget)
        self.layout.addWidget(self.plot_widget)
        self.setLayout(self.layout)

    def update_plot(self, data):
        # Get new data points
        x, y = data

        # Set or update maximum data points limit
        if not hasattr(self, 'max_data_points'):
            self.max_data_points = 1000  # Default value
        else:
            self.max_data_points = self.max_data_points

        # Limit data buffer size
        if len(x) > self.max_data_points:
            x = x[-self.max_data_points:]
            y = y[-self.max_data_points:]

        # Update curve data
        if not hasattr(self, 'curve'):
            self.curve = self.plot_item.plot(x, y)
        else:
            self.curve.setData(x, y)

        # Adjust x-axis range to show latest data
        self.plot_item.setXRange(min(x), max(x))