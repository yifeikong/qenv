"""
This file starts the main application.

"""
import asyncio
import sys
from PySide6.QtWidgets import QMainWindow

from aiohttp import web
from qasync import QApplication, QEventLoop
from setproctitle import setproctitle

from .engine import RenderWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("wkenv")
        self.widget = RenderWidget()
        self.setCentralWidget(self.widget)


def main():
    setproctitle("wkenv")
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    with loop:
        loop.create_task(web._run_app(window.widget.api.app))
        loop.run_until_complete(app_close_event.wait())

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
