class Label:
    '''Base Label Class'''
    def __init__(self):
        raise NotImplementedError('Do not use this Class directly')


class MatrixLabel(Label):
    '''Data Matrix Label'''
    pass


class LinearLabel(Label):
    '''Linear Label'''
    pass
