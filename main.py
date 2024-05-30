import os
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from utils.config import MasterConfig
from utils.logger_factory import create_logger
from forms.main_form import MainWindow
from forms.splash import SplashScreen


def handle_exception(exc_type, exc_value, exc_traceback):
    """ 处理未捕获的异常 """
    if issubclass(exc_type, KeyboardInterrupt):
        # 对于 KeyboardInterrupt，直接调用默认处理
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("未处理异常", exc_info=(exc_type, exc_value, exc_traceback))
    
    
if __name__ == "__main__":

    cur_dir = os.getcwd()
    conf_file = os.path.join(cur_dir, 'conf', 'config.yaml')
    if not os.path.exists(conf_file):
        print(f'config file {conf_file} not exists')
        sys.exit(-1)

    config = MasterConfig(config_file=conf_file)
    log_level = config.get_config('log', 'level', default='info')
    logger = create_logger(log_level=log_level)

    logger.info("main start...")
    logger.info(f'config file: {conf_file}')

    try:
        app = QApplication(sys.argv)
        sys.excepthook = handle_exception  # 设置自定义异常处理

        main_window = MainWindow()

        # 初始化
        splash_enabled = config.get_config('windows', 'splash', default=False)
        if splash_enabled:
            # Show the splash screen
            splash = SplashScreen()
            # Wait for the splash screen to finish hiding
            splash.exec_()
            QTimer.singleShot(500, main_window.show)
        else:
            main_window.show()

        # 程序运行，sys.exit方法确保程序完整退出。
        sys.exit(app.exec())
    except Exception as e:
        import traceback

        logger.error(traceback.format_exc())
