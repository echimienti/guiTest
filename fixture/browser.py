# -*- coding: utf-8 -*-

__author__ = "Enzo Chimienti"

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from fixture.locator import FundaXpathLocatator


class SeleniumBrowser(object):

    def __init__(self, url="https://www.funda.nl", browser="firefox", display="off", size=(800, 600), visible=0):
        if display == "on":
            display = Display(visible=visible, size=size)
            display.start()

        self.browser = browser
        self.url = url
        self.driver = None
        self.locator = FundaXpathLocatator()

    def start(self):
        """Start browser"""
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def stop(self):
        """Stop and close browser"""
        self.driver.close()

    def click_block_navigation(self, xpath_extension):
        self.driver.find_element_by_xpath(self.locator.block_navigation + xpath_extension).click()

    def click_search_submit(self):
        self.driver.find_element_by_xpath(self.locator.search_submit).click()

    def select_from_price(self, price):
        price_select = Select(self.driver.find_element_by_id(self.locator.price_select_from))
        if price.find('Anders') < 0:
            price_select.select_by_visible_text(price)
        else:
            price_select.select_by_visible_text(price.split(' ')[0])
            enter_element = self.driver.find_element_by_xpath(self.locator.price_anders)
            enter_element.send_keys(price.split(' ')[1])

    def select_distance(self, distance):
        distance_select = Select(self.driver.find_element_by_id(self.locator.distance_range))
        distance_select.select_by_visible_text(distance)

    def select_to_price(self, price):
        price_select = Select(self.driver.find_element_by_id(self.locator.price_select_to))
        if price.find('Anders') < 0:
            price_select.select_by_visible_text(price)
        else:
            price_select.select_by_visible_text(price.split(' ')[0])
            enter_element = self.driver.find_element_by_xpath(self.locator.price_select_anders)
            enter_element.send_keys(price.split(' ')[1])

    def verify_price_filter(self, price_from, price_to):
        if price_from:
            # remove \xe2\x82\xac and punctuation
           
            price_from = self.remove_punctuation(price_from.split(' ')[1])
        if price_to:
            # remove \xe2\x82\xac and punctuation
            price_to = self.remove_punctuation(price_to.split(' ')[1]) 

        wait = WebDriverWait(self.driver, 15)
        filter_button  = wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/main/form/div[2]/div[3]/div[1]/div[2]/div/button')))

        button_price = self.remove_punctuation(filter_button.text.split('\n')[1])

        if price_to and price_to.find('Anders') < 0:
            assert button_price.find(price_to) >= 0

        if price_from and price_from.find('Anders') < 0:
            assert button_price.find(price_from) >= 0
        if price_from and price_from.find('Anders') >= 0:
            if price_to:
                assert button_price.find(price_to.split(' ')[1]) >= 0
            if price_from:
                assert button_price.find(price_from.split(' ')[1]) >= 0

    def get_national_location(self):
        return self.driver.find_element_by_xpath(self.locator.national_location)

    def europa_location(self, country):
        self.driver.find_element_by_xpath(self.locator.europa_location).click()

        return self.driver.find_element_by_xpath(self.locator.get_element_country(country))

    def wait_for_title(self, title):
        """Function that waits for a page title"""
        WebDriverWait(self.driver, 15).until(ec.title_contains(title))
        time.sleep(10)

    def wait_autocomplete(self, option_nr):
        wait = WebDriverWait(self.driver, 15)
        autocomplete_list  = wait.until(
            ec.presence_of_element_located((By.XPATH, self.locator.get_autocomplete_list_option(option_nr))))
        return autocomplete_list;

    def wait_results(self):
        "Function wait and return found results"
        wait = WebDriverWait(self.driver, 15)
        searched_results = wait.until(
            ec.presence_of_element_located((By.XPATH, self.locator.search_results_1 or self.locator.search_results_2)))
        
        result = self.remove_punctuation(searched_results.text.split(' ')[0])
        return int(result)

    def remove_punctuation(self, a_string):
        """if there is punctuation remove it"""        
        if a_string.find('.') >= 0:
            result_s = a_string.split('.')
            a_string = "".join(result_s)

        return a_string

    def wait_no_results_warning(self):
        "Function wait no results and warning"
        wait = WebDriverWait(self.driver, 15)
        no_results = wait.until(
            ec.presence_of_element_located((By.XPATH, self.locator.warning)))
       
        result = no_results.text
        assert result == '0 resultaten'
 
        wait = WebDriverWait(self.driver, 15)
        warning_mesg = wait.until(
            ec.presence_of_element_located((By.XPATH, self.locator.warning_mesg)))

        warning_msg = warning_mesg.text
        assert warning_msg.find("Kies een groter gebied of verwijder") >= 0
        assert warning_msg.find("of meerdere filters. Sommige filters of combinaties van filters leverden 0 resultaten op.") >= 0

