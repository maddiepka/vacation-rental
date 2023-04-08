"""
UserInterface for AirBnB scrapper
"""
from inputvalidator import InputValidator, \
    OnlyLettersValidator, IsGoodDateFormatValidator, \
    IsInFutureValidator, IsAfterStartDateValidator, IsNumericValidator
from forms import AirBnbSearch
from exceptions import ValidationError


class ApartmentUI:

    def __init__(self):
        self.is_on = True
        self.ui_brain = {
            'location': {
                'question': 'Where you want to go? [city] or [city, country] ',
                'answer': None,
                'validators': [OnlyLettersValidator],
            },
            'check_in': {
                'question': 'Check in date (YYYY-MM-DD): ',
                'answer': None,
                'validators': [IsGoodDateFormatValidator,
                               IsInFutureValidator]
            },
            'check_out': {
                'question': 'Check out date (YYYY-MM-DD): ',
                'answer': None,
                'validators': [IsGoodDateFormatValidator,
                               IsInFutureValidator,
                               IsAfterStartDateValidator]
            },
            'n_of_rooms': {
                'question': 'How many rooms do you need?: ',
                'answer': None,
                'validators': [IsNumericValidator]
            },
            'n_of_adults': {
                'question': 'How many adults?: ',
                'answer': None,
                'validators': [IsNumericValidator]
            },
            'max_price': {
                'question': 'Max nightly price (base price without taxes and extra fees, '
                            'in your currency)?: ',
                'answer': None,
                'validators': [IsNumericValidator]
            },
        }


    def validate_answers(self, value, start_date=None):

        while True:
            answer = input(value['question'])
            if start_date:
                validator = InputValidator(answer, validators=value['validators'],
                                           start_date=start_date)
            else:
                validator = InputValidator(answer, validators=value['validators'])
            try:
                validator.is_valid()
            except ValidationError as error:
                print(error)
            else:
                return answer

    def ask_questions(self):
        for key, value in self.ui_brain.items():
            if key == 'check_out':
                check_in = self.ui_brain['check_in']['answer']
                answer = self.validate_answers(value, start_date=check_in)
            else:
                answer = self.validate_answers(value)
            value['answer'] = answer


    def create_answers(self):
        answers = {key: value['answer'] for key, value in self.ui_brain.items()}
        return answers

    def create_form(self):
        answers = self.create_answers()
        search_form = AirBnbSearch(**answers)
        return search_form

    def no_data_info(self):
        print('No results found. Increase your budget or try other dates/place')

    def close(self):
        self.is_on = False
