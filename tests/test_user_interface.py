"""
Tests for User Interface
"""

import pytest
from user_interface import ApartmentUI
from inputvalidator import *


def test_create_answers():
    # given
    ui = ApartmentUI()
    ui.ui_brain = {
            'location': {
                'question': 'Where you want to go? ',
                'answer': 'Malaga',
                'validators': [OnlyLettersValidator],
            },
            'check_in': {
                'question': 'Check in date (YYYY-MM-DD): ',
                'answer': '2024-04-01',
                'validators': [IsGoodDateFormatValidator, IsInFutureValidator]
            },
            'check_out': {
                'question': 'Check out date (YYYY-MM-DD): ',
                'answer': '2024-04-07',
                'validators': [IsGoodDateFormatValidator, IsInFutureValidator, IsAfterStartDateValidator]
            },
            'n_of_rooms': {
                'question': 'How many rooms do you need?: ',
                'answer': '2',
                'validators': [IsNumericValidator]
            },
            'n_of_adults': {
                'question': 'How many adults?: ',
                'answer': '2',
                'validators': [IsNumericValidator]
            },
            'max_price': {
                'question': 'Your max budget for total stay? (in $): ',
                'answer': '1000',
                'validators': [IsNumericValidator]
            },
        }
    # when
    answers = ui.create_answers()
    # then
    assert answers == {
            'location':  'Malaga',
            'check_in': '2024-04-01',
            'check_out': '2024-04-07',
            'n_of_rooms': '2',
            'n_of_adults': '2',
            'max_price': '1000',
            }

def test_create_form():
    # given
    ui = ApartmentUI()
    ui.ui_brain = {
            'location': {
                'question': 'Where you want to go? ',
                'answer': 'Malaga',
                'validators': [OnlyLettersValidator],
            },
            'check_in': {
                'question': 'Check in date (YYYY-MM-DD): ',
                'answer': '2024-04-01',
                'validators': [IsGoodDateFormatValidator, IsInFutureValidator]
            },
            'check_out': {
                'question': 'Check out date (YYYY-MM-DD): ',
                'answer': '2024-04-07',
                'validators': [IsGoodDateFormatValidator, IsInFutureValidator, IsAfterStartDateValidator]
            },
            'n_of_rooms': {
                'question': 'How many rooms do you need?: ',
                'answer': '2',
                'validators': [IsNumericValidator]
            },
            'n_of_adults': {
                'question': 'How many adults?: ',
                'answer': '2',
                'validators': [IsNumericValidator]
            },
            'max_price': {
                'question': 'Your max budget for total stay? (in $): ',
                'answer': '1000',
                'validators': [IsNumericValidator]
            },
        }
    # when
    form = ui.create_form()
    # then
    assert vars(form) == {
            'location':  'Malaga',
            'check_in': '2024-04-01',
            'check_out': '2024-04-07',
            'n_of_rooms': '2',
            'n_of_adults': '2',
            'max_price': '1000',
            'url': None,
            'results': []
            }

