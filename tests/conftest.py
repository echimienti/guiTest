__author__ = "Enzo Chimienti"

import pytest

from fixture.browser import SeleniumBrowser


@pytest.fixture(scope='function')
def setup_browser():
    browser = SeleniumBrowser()

    yield browser

    browser.stop()


@pytest.fixture(scope='function')
def run_browser(setup_browser):
    """Sets up a browser for selenium session"""
    setup_browser.start(url="https://www.funda.nl", browser="firefox", display="off", size=(800, 600), visible=0)
    return setup_browser

