#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Enzo Chimienti"

"""Funda quicksearch Selenium WebDriver test"""
from selenium.webdriver.common.keys import Keys
from classes.funda_simple_search import FundaSimpleSearch


class TestFundaSimpleSearchChromium(FundaSimpleSearch):
    """Selenium test for funda search"""
    def test_with_chromium(self, setup_browser):
        """Tests with various to and from price combinations selected"""
        setup_browser.start(url="https://www.funda.nl", browser="chrome", display="off", size=(800, 600), visible=0)
        setup_browser.wait_for_title('Zoek huizen en appartementen te koop in Nederland [funda]')
        setup_browser.select_from_price('€ 50.000' )

        self.submit_and_verify(setup_browser)

        setup_browser.verify_price_filter('€ 50.000', None)

