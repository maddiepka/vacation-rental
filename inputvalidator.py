"""
InputValidator collects input from the user and check
if it's valid for search.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from exceptions import ValidationError


class Validator(ABC):
    """
    Interface for Input validator
    """

    @abstractmethod
    def __init__(self, input):
        """
        Force to implement __init__
        :param input: user's input
        """
        self.input = input

    @abstractmethod
    def is_valid(self):
        """
        Force to implement is_valid method
        """

class OnlyLettersValidator(Validator):
    """
    Validator cheks if input contains only letters
    """
    def __init__(self, input):
        self.input = input

    def is_valid(self):
        """Checks if input is valid

        :return:
            bool: city has only letters
        :raises:
            ValidationError: city doesn't have only letters

        """
        stripped = self.input.replace(',','').replace(' ', '')
        if stripped.isalpha():
            return True
        raise ValidationError('Input doesn\'t contain only letters!')


class IsNumericValidator(Validator):
    """
    Validator cheks if input is a Numeric and >0
    """
    def __init__(self, input):
        self.input = input

    def is_valid(self):
        """Checks if input is valid

        :return:
            bool: is numeric
        :raises:
            ValidationError: input contains other signs

        """
        if self.input.isnumeric():
            if int(self.input) > 0:
                return True
            raise ValidationError('Input should be bigger than 0!')
        raise ValidationError('Input doesn\'t contain only digits!')


class IsGoodDateFormatValidator(Validator):
    """
    Validator cheks if input is a date in format YYYY-MM-DD
    """

    def __init__(self, input):
        self.input = input

    def is_valid(self):
        """Checks if input is valid

        :return:
            bool: date exists and is in good format YYYY-MM-DD
        :raises:
            ValidationError: wrong date or wrong dateformat
        """
        try:
            datetime.strptime(self.input, '%Y-%m-%d')
        except ValueError as exc:
            raise ValidationError(f"Time data  {self.input} incorrect "
                                  f"or doesn\'t match format YYYY-MM-DD") from exc
        return True

class IsInFutureValidator(Validator):
    """
    Validator cheks if input is a date in the future
    """

    def __init__(self, input):
        self.input = input

    def is_valid(self):
        """Checks if input is valid

        :return:
            bool: date in the future
        :raises:
            ValidationError: date from past
        """
        if self.input >= datetime.today().strftime('%Y-%m-%d'):
            return True
        raise ValidationError('Date not in the future!')

class IsAfterStartDateValidator(Validator):
    """
    Validator cheks if given date is after start date
    """

    def __init__(self, input, start_date):
        self.input = input
        self.start_date = start_date

    def is_valid(self):
        """Checks if input is valid

        :return:
            bool: End date is after start date
        :raises:
            ValidationError: end date is before start date
        """
        if self.input > self.start_date:
            return True
        raise ValidationError("End date can't be before start date!")


class InputValidator(Validator):
    """
    Total Input Validator - contains other Input Validators, all optional
    """

    def __init__(self, input, validators:list,  start_date=None):

        self.input = input
        self.validators = validators
        for validator in self.validators:
            if validator == IsAfterStartDateValidator:
                if start_date:
                    self.start_date=start_date
                else:
                    raise ValidationError("No start date to compare!")

    def is_valid(self):
        """Checks if input is valid

        :returns:
            bool: returns true if input passed all requirements.
        """
        for class_name in self.validators:
            if  class_name == IsAfterStartDateValidator:
                validator = class_name(self.input, self.start_date)
            else:
                validator = class_name(self.input)
            if validator.is_valid() is False:
                return False
        return True
