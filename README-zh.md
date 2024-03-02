wkenv
======

基于 WebKit 的 JavaScript 环境，用来执行 jsvmp 等 API 加密代码。

有了 `wkenv`，就不需要再补环境模拟浏览器了，因为这个本身就是基于 WebKit 的一个浏览器。
另一方面，`wkenv` 本身就是为了爬虫而生的，而不是测试工具。用 wkenv 搭建一个服务，比用
Playwright 或者 Selenium 要简单得多。

功能(to be implemented)
------

1. 直接执行 js 代码，就像 `pyexecjs` 一样，但是通过 API.
    - Pass a piece of script and execute directly.
    - Register a script to be called later via name or id.
    - Create virtual env with custom patches.
2. Use JS RPC to call the algorithm on host page.
    - Execute functions directly within the page context.
    - Register additional scripts to the page.
3. Docker image for one-click install as a service.
4. Call wkenv as a headless browser, without the `webdriver` attributes.

Acknowledgements
------

PySide6 tutorial: https://www.pythonguis.com/pyqt6/
