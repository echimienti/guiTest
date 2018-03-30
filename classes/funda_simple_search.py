__author__ = "Enzo Chimienti"


class FundaSimpleSearch():
    """Selenium class with methods for funda search"""

    expected_results = 0

    def submit_and_verify(self, browser):
        """submit the search and wait for the results"""
        browser.click_search_submit()
        searched_results = browser.wait_results()
        assert int(searched_results) >= self.expected_results

    def enter_national_location(self, browser, location):
        location_input = browser.get_national_location()

        # enter part of the location
        location_input.click()

        for char_l in list(location):
            location_input.send_keys(char_l)
            time.sleep(0.3)

        # click on the first match of autocomplete
        autocomplete_list0 = browser.wait_autocomplete('0')
        autocomplete_list0.click()

    def enter_european_location(self, browser, location):
        country_location = browser.europa_location(location)
        country_location.click()
