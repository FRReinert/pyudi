from abc import ABCMeta, abstractmethod

class IField(metaclass=ABCMeta):
    '''Interface for Field Classes'''

    data_delimiter: str
    data_size: int
    agency: str
    name: str

    @property
    @abstractmethod
    def regex(self):
        '''Regex Interface implementation'''


class GS1AlphanumericField(IField):
    '''Base GS1 Alphanumeric Field'''

    @property
    def regex(self):
        return fr'{self.data_delimiter}([\x21-\x22\x25-\x2F\x30-\x39\x3A-\x3F\x41-\x5A\x5F\x61-\x7A]{{0,{self.data_size}}})$'


class GS1DateField(IField):
    '''Base GS1 Date Field'''

    @property
    def regex(self):
        return fr'{self.data_delimiter}(\d{{{self.data_size}}})$'


class GS1NumericField(IField):
    '''Base GS1 Numeric Field'''

    @property
    def regex(self):
        return fr'{self.data_delimiter}(\d{{{self.data_size}}})$'