
import random

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
from PySide6.QtCore import QUrl, Slot
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QVBoxLayout, QPushButton
# from qasync import asyncClose, asyncSlot

from .api import ApiWidget


class RenderWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.load(QUrl("https://abrahamjuliot.github.io/creepjs/"))

        self.goto_button = QPushButton("Go")
        self.address_bar = QLineEdit()
        self.api = ApiWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        header = QHBoxLayout()
        header.addWidget(self.address_bar)
        header.addWidget(self.goto_button)

        layout.addLayout(header)
        layout.addWidget(self.webview)
        layout.addWidget(self.api)

        self.setLayout(layout)

        # User action signals
        self.goto_button.clicked.connect(self.on_goto_clicked)
        self.address_bar.returnPressed.connect(self.on_goto_clicked)

        # Page events
        self.webview.urlChanged.connect(self.on_url_changed)

        self.api.sig.connect(self.update_url)


    @Slot()
    def on_goto_clicked(self):
        self.webview.load(QUrl(self.address_bar.text()))

    @Slot()
    def on_url_changed(self):
        self.address_bar.setText(self.webview.url().toString())

    @Slot()
    def update_url(self):
        self.webview.load(QUrl("https://www.zhihu.com"))
