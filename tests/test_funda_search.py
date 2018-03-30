#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Enzo Chimienti"

"""Funda quicksearch Selenium WebDriver test"""

import pytest
import time

from selenium.webdriver.common.keys import Keys
from classes.funda_simple_search import FundaSimpleSearch


class TestFundaSimpleSearch(FundaSimpleSearch):
    """Selenium test for funda search"""

    @pytest.mark.parametrize('block_navigation, xpath_extension, location, title',
        [('koop', 'li[1]/a', 'Hui', 'huizen en appartementen te koop in Nederland'),
        ('huur', 'li[2]/a', 'Hilvers', 'huizen en appartementen te huur in Nederland'),
        ('nieuwbouw', 'li[3]/ul/li[1]/a', 'Alme', 'nieuwbouwprojecten en -woningen in Nederland'),
        ('recreatie', 'li[3]/ul/li[2]/a', 'Den ', 'recreatiewoningen in Nederland'), # test 0 results
        ('europa', 'li[3]/ul/li[3]/a', 'duitsland', 'huizen en appartementen in Europa')
    ])
    def test_location_input(self, run_browser, block_navigation, xpath_extension, location, title):
        """Tests the location input for the various navigation blocks"""
        title = "Zoek %s [funda]" % title
        if run_browser.driver.title != title:
            run_browser.click_block_navigation(xpath_extension)
            run_browser.wait_for_title(title)

        if block_navigation != 'europa':
            self.enter_national_location(run_browser, location)
        else:
            self.enter_european_location(run_browser, location)

        self.submit_and_verify(run_browser)

    @pytest.mark.parametrize('price_from, price_to', [
        ('€ 50.000' , None),
        (None, '€ 75.000'),
        ('€ 50.000', '€ 2.000.000'),
        ('€ 1.000.000', '€ 50.000'),
        ('Anders 100000', 'Anders 200000')
    ])
    def test_from_with_to_price(self, run_browser, price_from, price_to):
        """Tests with various to and from price combinations selected"""
        run_browser.wait_for_title('Zoek huizen en appartementen te koop in Nederland [funda]')
        if price_from:
            run_browser.select_from_price(price_from)

        if price_to:
            run_browser.select_to_price(price_to)

        self.submit_and_verify(run_browser)

        if price_from == '€ 1.000.000':
            run_browser.wait_no_results_warning()
        else:
            run_browser.verify_price_filter(price_from, price_to)

    @pytest.mark.parametrize('straal', ['+ 0 km', '+ 1 km', '+ 2 km',
        '+ 5 km','+ 10 km', '+ 15 km'])
    def test_distance(self, run_browser, straal):
        self.enter_national_location(run_browser, 'Huiz')
        run_browser.select_distance(straal)
        self.submit_and_verify(run_browser)
