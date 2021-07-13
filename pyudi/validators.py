from abc import ABC, abstractmethod


__all__ = ['DateValidator', 'AllowedCharactersValidator', 'SizeOverflowValidator', 'FixedSizeValidator', 'RegexValidator',]


class IValidator(ABC):

    @abstractmethod
    def validate(self, field: str, value: str, *args, **kwargs) -> bool:
        '''Execute validations'''
        pass


class DateValidator(IValidator):
    '''Date Field validation'''

    def validate(field, value) -> bool:
        pass


class AllowedCharactersValidator(IValidator):
    '''Validate if only allowed characters are used'''

    def validate(field, value) -> bool:
        pass


class SizeOverflowValidator(IValidator):
    '''Validate size overflow'''

    def validate(field, value) -> bool:
        pass


class FixedSizeValidator(IValidator):
    '''Validate fixed size fields'''

    def validate(field, value) -> bool:
        pass


class RegexValidator(IValidator):
    '''Validate regex'''

    def validate(field, value, regex) -> bool:
        pass