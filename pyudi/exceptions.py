'''UDI Exceptions'''


class InvalidAlphanumericException(Exception):
    '''Invalid Date field Exception'''
    pass


class InvalidDateException(Exception):
    '''Invalid Date field Exception'''
    pass


class SerializingException(Exception):
    '''Bad instance fields'''
    pass


class ParsingExecption(Exception):
    '''Bad UDI code'''
    pass
