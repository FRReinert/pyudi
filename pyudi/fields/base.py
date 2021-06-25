'''
    This file contain the IField to Interface any agency fields.
    - Do not make attr, properties or methos for IField which only benefits a single agency
    - IField must be enough abstract to implement all possible agencies
'''

from abc import ABCMeta, abstractclassmethod

class IField(metaclass=ABCMeta):
    '''Base interface for any agency Field'''

    data_delimiter: str
    data_size: int
    agency: str
    value:str
    name: str

    @classmethod
    @abstractclassmethod
    def regex(self):
        '''Regex Interface implementation'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class GS1AlphanumericField(IField):
    '''Base GS1 Alphanumeric Field'''

    @classmethod
    def regex(cls):
        return r'%s([\x21-\x22\x25-\x2F\x30-\x39\x3A-\x3F\x41-\x5A\x5F\x61-\x7A]{0,%s})' % (cls.data_delimiter, cls.data_size)


class GS1DateField(IField):
    '''Base GS1 Date Field'''

    @classmethod
    def regex(cls):
        return r'%s(\d{%s})' % (cls.data_delimiter, cls.data_size)


class GS1NumericField(IField):
    '''Base GS1 Numeric Field'''

    @classmethod
    def regex(cls):
        return r'%s(\d{%s})' % (cls.data_delimiter, cls.data_size)
