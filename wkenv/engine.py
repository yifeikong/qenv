
import random

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
from qasync import asyncClose, asyncSlot

from .api import ApiWidget


class RenderWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QtCore.QUrl("https://abrahamjuliot.github.io/creepjs/"))

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.api = ApiWidget()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.api)

        self.button.clicked.connect(self.magic)
        self.api.sig.connect(self.update_url)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    @QtCore.Slot()
    def update_url(self):
        self.view.load(QtCore.QUrl("https://www.zhihu.com"))
