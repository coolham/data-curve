import sys
import time
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtGui import QPixmap


class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(":/images/resources/img-start.png").scaled(800, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if pixmap.isNull():  # 检查图片是否加载成功
            self.showMessage("Error: Failed to load splash image", Qt.AlignCenter, Qt.white)
            self.setFixedSize(800, 400)  # 设置错误信息窗口的大小
        else:
            self.setPixmap(pixmap)
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
            # self.showMessage("Loading...", Qt.AlignCenter, Qt.white)
            self.adjustWindowSize()

    def adjustWindowSize(self):
        # desktop = QDesktopWidget()
        # screen_rect = desktop.availableGeometry()
        # width = int(screen_rect.width() * 0.45)  # 根据屏幕宽度调整闪屏窗口的宽度
        # height = int(screen_rect.height() * 0.4)  # 根据屏幕高度调整闪屏窗口的高度
        # self.resize(width, height)

        # # 计算闪屏窗口的位置使其居中显示
        # x = screen_rect.x() + (screen_rect.width() - width) // 2
        # y = screen_rect.y() + (screen_rect.height() - height) // 2
        # self.move(x, y)
        return 
    
    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(3000, self.close)  # 设置3秒后自动关闭
        
        