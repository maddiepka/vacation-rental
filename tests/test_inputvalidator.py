"""
Tests for InputValidator
"""

import pytest

from  inputvalidator import OnlyLettersValidator, IsNumericValidator, \
    IsGoodDateFormatValidator, IsInFutureValidator, \
    IsAfterStartDateValidator, InputValidator

from exceptions import ValidationError


def test_only_letters_validator_positive():
    """
    Test of class OnlyLettersValidator - positive case
    """
    # given
    input = OnlyLettersValidator('isdfoljhjlsdefkjDHJSHSDJK')
    # when
    result = input.is_valid()
    # then
    assert result is True

    # given
    input = OnlyLettersValidator('Los Angeles')
    # when
    result = input.is_valid()
    # then
    assert result is True

    # given
    input = OnlyLettersValidator('Los Angeles, USA')
    # when
    result = input.is_valid()
    # then
    assert result is True


def test_only_letters_validator_negative():
    """
    Test of class OnlyLettersValidator - negative cases
    """
    # given
    input = OnlyLettersValidator('2sdfsdfsdf')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert 'Input doesn\'t contain only letters!' in str(error.value)

    # given
    input = OnlyLettersValidator('?sdfsdfsdf')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert 'Input doesn\'t contain only letters!' in str(error.value)


def test_is_numeric_validator_positive():
    """
    Test of class IsNumericValidator - positive case
    """
    # given
    input = IsNumericValidator('1212450')
    # when
    result = input.is_valid()
    # then
    assert result is True


def test_is_numeric_validator_negative():
    """
    Test of class IsNumericValidator - negative cases
    """
    # given
    input = IsNumericValidator('1sd212450')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert 'Input doesn\'t contain only digits!' in str(error.value)

    # given
    input = IsNumericValidator('1.5')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert 'Input doesn\'t contain only digits!' in str(error.value)


def test_is_good_date_format_validator_positive():
    """
    Test of class IsGoodDateFormatValidator - positive case
    """
    # given
    input = IsGoodDateFormatValidator('2022-05-02')
    # when
    result = input.is_valid()
    # then
    assert result is True


def test_is_good_date_format_validator_negative():
    """
    Test of class IsGoodDateFormatValidator - negative cases
    """
    # given
    input = IsGoodDateFormatValidator('02-02-2003')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert f"Time data  {input.input} incorrect or doesn\'t match format YYYY-MM-DD" \
               in str(error.value)

    # given
    input = IsGoodDateFormatValidator('2022-05-38')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert f"Time data  {input.input} incorrect or doesn\'t match format YYYY-MM-DD" \
               in str(error.value)


def test_is_in_future_validator_positive():
    """
    Test of class IsInFutureValidator - positive case
    """
    # given
    input = IsInFutureValidator('2040-05-02')
    # when
    result = input.is_valid()
    # then
    assert result is True


def test_is_in_future_validator_negative():
    """
    Test of class IsInFutureValidator - negative case
    """
    # given
    input = IsInFutureValidator('2022-05-02')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert 'Date not in the future!' in str(error.value)


def test_is_after_start_date_validator_positive():
    """
    Test of class IsAfterStartDateValidator - positive case
    """
    # given
    input = IsAfterStartDateValidator('2023-05-02', '2023-04-08')
    # when
    result = input.is_valid()
    # then
    assert result is True

def test_is_after_start_date_validator_negative():
    """
    Test of class IsAfterStartDateValidator - negative case
    """
    # given
    input = IsAfterStartDateValidator('2023-05-02', '2023-05-08')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert "End date can't be before start date!" in str(error.value)

def test_input_validator_positive():
    """
    Test of total class InputValidator - positive cases
    """
    # given
    # input = InputValidator('Malaga', validators=[OnlyLettersValidator, CityValidator])
    input = InputValidator('Malaga, Spain', validators=[OnlyLettersValidator])

    # when
    result = input.is_valid()
    # then
    assert result is True

    # given
    input = InputValidator('5', validators=[IsNumericValidator])
    # when
    result = input.is_valid()
    # then
    assert result is True

    # given
    input = InputValidator('2023-05-02', validators=[IsGoodDateFormatValidator,
                                                     IsInFutureValidator])
    # when
    result = input.is_valid()
    # then
    assert result is True

    # given
    input = InputValidator('2023-05-02',
                           validators=[IsGoodDateFormatValidator,
                                       IsInFutureValidator,
                                       IsAfterStartDateValidator],
                           start_date = '2023-05-01')
    # when
    result = input.is_valid()
    # then
    assert result is True


def test_input_validator_negative():
    """
    Test of total class InputValidator - negative cases
    """
    # given
    input = InputValidator('2023-05-02',
                           validators=[IsGoodDateFormatValidator,
                                       IsInFutureValidator,
                                       IsAfterStartDateValidator],
                           start_date = '2023-05-08')
    # when
    with pytest.raises(ValidationError) as error:
        input.is_valid()
        assert "End date can't be before start date!" in str(error.value)


    with pytest.raises(ValidationError) as error:
        InputValidator('2023-05-02',
                               validators=[IsGoodDateFormatValidator,
                                           IsInFutureValidator,
                                           IsAfterStartDateValidator])
        assert "No start date to compare!" in str(error.value)
