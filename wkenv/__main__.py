import asyncio
import sys
from qasync import QEventLoop, QApplication
from setproctitle import setproctitle

from aiohttp import web
from .engine import RenderWidget
from .api import ApiWidget


if __name__ == "__main__":
    setproctitle("wkenv")
    app = QApplication([])

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    widget = RenderWidget()
    widget.resize(800, 600)
    widget.show()

    with loop:
        loop.create_task(web._run_app(widget.api.app))
        loop.run_until_complete(app_close_event.wait())

    sys.exit(app.exec())
