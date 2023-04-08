"""
AirBnB-scrapper - application gets from the user info about his future vacation stay,
validates it, and searches the AirBnB database to find vacation rentals.
Then the results are collected in an Airtable table so users can pick the best choice for them.
"""

from os import getenv
from dotenv import load_dotenv
from user_interface import ApartmentUI
from airtable import AirtableNavigator

load_dotenv()
chrome_driver_path =getenv('CHROME_DRIVER_PATH')

if __name__ == '__main__':
    ui = ApartmentUI()
    while ui.is_on:
        ui.ask_questions()
        user_form = ui.create_form()
        user_form.create_url()
        user_form.collect_search_data()
        if user_form.results:
            with AirtableNavigator(chrome_driver_path=chrome_driver_path,
                                   search_results=user_form.results,
                                   tags=[user_form.location, user_form.check_in,
                                         user_form.check_out]) as bot:
                bot.insert_search_results()
                bot.show_results()
            ui.close()
        else:
            ui.no_data_info()
