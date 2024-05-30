import time
import random
from PyQt6.QtCore import QObject, QTimer, pyqtSignal


class DataSource(QObject):
    data_signal = pyqtSignal(list)  # Signal to emit new data points

    def __init__(self):
        super().__init__()

        self.x_data = []
        self.y_data = []

    def start(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.generate_data)
        self.timer.start(100)  # Update data every 100 milliseconds

    def generate_data(self):
        # Generate random data points
        x = self.x_data[-1] + 1 if self.x_data else 0
        y = random.randint(0, 100)

        # Append new data points
        self.x_data.append(x)
        self.y_data.append(y)

        # Emit new data signal
        self.data_signal.emit([self.x_data, self.y_data])