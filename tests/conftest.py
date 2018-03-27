__author__ = "Enzo Chimienti"

import pytest

from fixture.browser import SeleniumBrowser

@pytest.fixture(scope='function')
def run_browser(url="https://www.funda.nl", browser="firefox", display="off", size=(800, 600), visible=0):
    """Sets up a browser for selenium session"""
    browser = SeleniumBrowser(url, browser, display, size, visible)

    browser.start()

    yield browser

    browser.stop()
