import sys
import time
import random
import PyQt6
from PyQt6.QtCore import QTimer, QPoint
from PyQt6.QtGui import QPixmap, QColor, QPainter
from PyQt6.QtWidgets import QTabWidget, QWidget, QLabel, QPushButton


class RtCurveArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Canvas
        self.canvas = QPainter(self)

        # Data
        self.data = []

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_curve)
        self.timer.start(100)

    def update_curve(self):
        # Generate new data
        new_data = [random.randint(0, 100) for _ in range(10)]
        self.data.extend(new_data)

        # Repaint the canvas
        self.update()

    def paintEvent(self, event):
        # Draw the curve
        self.canvas.begin(self)

        for i in range(len(self.data) - 1):
            start_point = QPoint(i * 10, self.height() - self.data[i])
            end_point = QPoint((i + 1) * 10, self.height() - self.data[i + 1])
            # self.canvas.setPen(QColor(Qt.red))
            self.canvas.drawLine(start_point, end_point)

        self.canvas.end()
