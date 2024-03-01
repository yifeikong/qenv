
import random

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QVBoxLayout, QPushButton
# from qasync import asyncClose, asyncSlot

from .api import ApiWidget


class RenderWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QUrl("https://abrahamjuliot.github.io/creepjs/"))

        self.goto_button = QPushButton("Go")
        self.address_bar = QLineEdit()
        self.api = ApiWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        header = QHBoxLayout()
        header.addWidget(self.address_bar)
        header.addWidget(self.goto_button)

        layout.addLayout(header)
        layout.addWidget(self.view)
        layout.addWidget(self.api)

        self.setLayout(layout)

        self.goto_button.clicked.connect(self.on_goto_clicked)
        self.address_bar.returnPressed.connect(self.on_goto_clicked)
        self.api.sig.connect(self.update_url)

    @QtCore.Slot()
    def on_goto_clicked(self):
        self.view.load(QUrl(self.address_bar.text()))

    @QtCore.Slot()
    def update_url(self):
        self.view.load(QUrl("https://www.zhihu.com"))
