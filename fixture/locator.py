
__author__ = "Enzo Chimienti"


class FundaXpathLocatator(object):

    def __init__(self):
        self.national_location = '//*[@id="autocomplete-input"]'
        self.block_navigation = '//*[@id="content"]/div[1]/div[4]/form/nav/ul/'
        self.search_submit = '//*[@id="content"]/div[1]/div[4]/form/div[1]/div/div/button'
        self.search_results_1 = '//*[@id="content"]/form/div[2]/div[1]/span'
        self.search_results_2 = '//*[@id="content"]/form/div[2]/div[3]/div[3]/div[1]'
        self.price_select_from = 'range-filter-selector-select-filter_koopprijsvan'
        self.price_anders = '/html/body/main/div[1]/div[4]/form/div[1]/div/fieldset[2]/div[1]/div/div[2]/div/input'
        self.distance_range = 'Straal'
        self.price_select_to = 'range-filter-selector-select-filter_koopprijstot'
        self.price_select_anders = '/html/body/main/div[1]/div[4]/form/div[1]/div/fieldset[2]/div[2]/div/div[2]/div/input'
        self.price_filter_button_by_xpath = '/html/body/main/form/div[2]/div[3]/div[1]/div[2]/div/button'
        self.europa_location = '//*[@id="content"]/div[1]/div[4]/form/div[1]/div/fieldset/div/div/div[1]'
        self.warning = '//*[@id="content"]/form/div[2]/div[3]/div[3]/div/h1'
        self.warning_mesg = '//*[@id="content"]/form/div[2]/div[3]/div[3]/div/p'

    def get_autocomplete_list_option(self, option):
        return '//*[@id="autocomplete-list-option%s"]' % option

    def get_element_country(self, country):
        return '//*[@id="Land-%s"]' % country
