#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Enzo Chimienti"

"""Funda quicksearch Selenium WebDriver test"""

import pytest
import time

from selenium.webdriver.common.keys import Keys
from test_funda_search import TestFundaSimpleSearch

class TestFundaSimpleSearchChromium(TestFundaSimpleSearch):
    """Selenium test for funda search"""
    def test_from_with_chromium(self, setup_browser):
        """Tests with various to and from price combinations selected"""
        setup_browser.start(url="https://www.funda.nl", browser="chrome", display="off", size=(800, 600), visible=0)
        setup_browser.wait_for_title('Zoek huizen en appartementen te koop in Nederland [funda]')
        setup_browser.select_from_price('€ 50.000' )

        submit_and_verify(setup_browser)

        setup_browser.verify_price_filter('€ 50.000', None)

