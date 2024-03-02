wkenv
======

WebKit based JavaScript environment for executing API-signing algorithms, such as jsvmp.

With `wkenv`, you do not need to create a patched environment to emulate the browser,
because it's indeed a real WebKit based browser. On the other hand, it's built for
crawling, not testing. It's much easier to manage a wkenv service than a Playwright or
Selenium service.

Features(to be implemented)
------

1. Execute JavaScript directly, like `pyexecjs`.
    - Pass a piece of script and execute directly.
    - Register a script to be called later via name or id.
    - Create virtual env with custom patches.
2. Use JS RPC to call the algorithm on host page.
    - Execute functions directly within the page context.
    - Register additional scripts to the page.
3. Docker image for one-click install as a service.
4. Call wkenv as a headless browser, without the `webdriver` attributes.
    - Integrate common anti-detect scripts from [Undetected chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
    - Generate random values for JS based fingerprints.

Acknowledgements
------

PySide6 tutorial: https://www.pythonguis.com/pyqt6/
