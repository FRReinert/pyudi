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
    value: str
    name: str

    @classmethod
    @abstractclassmethod
    def regex(self):
        '''Regex Interface implementation'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
