'''UDI Exceptions'''


class ValidationExeption(Exception):
    '''Invalid Date field Exception'''
    pass


class FixedSizeError(ValidationExeption):
    '''Exception when fixed size is mandatory'''
    def __init__(self, field, value, fixed_size):
        self.message = f'Bad value "{value}" for field <{field}>. It should have a fixed size of {fixed_size}'


class SizeOverflowError(ValidationExeption):
    '''Exception when size is higher then it should'''
    def __init__(self, field, value, max_size):
        self.message = f'Bad value "{value}" for field <{field}>. It should measure less then {max_size}'


class InvalidCharacterError(ValidationExeption):
    '''When Invalid character found on value'''
    def __init__(self, field, value):
        self.message = f'Bad value "{value}" for field <{field}>. Prohibited characters found'


class DateFieldError(ValidationExeption):
    '''Date field error'''

    def __init__(self, field, value):
        self.message = f'Bad value "{value}" for field <{field}>. Only "YYMMDD" dates are valid'


class RegexError(ValidationExeption):
    '''Regex compliance'''

    def __init__(self, field, value, regex):
        self.message = f'Bad value "{value}" for field <{field}>. Regex "{regex}" error'
