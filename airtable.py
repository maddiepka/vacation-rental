"""
AirtableNavigator inserts data from AirBnB search to AirTable form
and shows results in a table.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class AirtableNavigator:

    def __init__(self, chrome_driver_path, search_results, tags):
        self.search_results = search_results
        self.tags = tags
        self.form_url = 'https://airtable.com/shrLPxfsJ0f7M1GQ6'
        self.results_url = 'https://airtable.com/shrANcvtjLTX7IAZZ/tbltobKnPyOfpWTLI'
        self.chrome_driver_path = chrome_driver_path
        self.driver = None

    def __enter__(self):

        service = Service(self.chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=service, options=options)
        return self

    def insert_search_results(self):
        self.driver.get(self.form_url)
        time.sleep(2)
        for result in self.search_results:
            form_cells = self.driver.find_elements(By.TAG_NAME, 'input')
            form_cells[0].send_keys(result.name)
            form_cells[1].send_keys(result.price)
            form_cells[2].send_keys(result.score)
            form_cells[3].send_keys(result.url)
            form_cells[4].send_keys(f"{self.tags[0].replace('-', ' ')},"
                                    f" {self.tags[1]}-{self.tags[2]}")
            form_cells[5].click()
            time.sleep(2)
            submit_next = self.driver.find_element(By.CLASS_NAME, 'refreshButton')
            submit_next.click()

    def show_results(self):
        print('Choose your vacation stay in table:')
        print(f'{self.results_url}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
