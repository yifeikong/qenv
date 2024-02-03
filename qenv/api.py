from aiohttp import web
from functools import cached_property

from PySide6 import QtCore, QtWidgets

routes = web.RouteTableDef()


class ApiWidget(QtWidgets.QWidget):
    sig = QtCore.Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_server()

    def setup_server(self):
        self.app.add_routes([web.get("/", self.hello)])

    @cached_property
    def app(self):
        return web.Application()

    async def hello(self, request):
        self.sig.emit("world")
        return web.Response(text="Hello, world")
