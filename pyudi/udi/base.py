from abc import abstractmethod


'''
    This file contain the base abstract class to implement all agencies UDI
    - Do not implement anything that is intrinsict of a single Agency such as GS1
    - If there is a property, attr or method that any agency can make use, make it mandatory using the ABS lib  
'''


class IStructureUDI:
    '''UDI Structure interface'''
    pass


class StructureUDI:
    '''Base class for UDI implementation instance'''

    __iter_collection: list = []
    __iter_pos: int = 0

    def __iter__(self):
        self.__iter_collection = [field for field in self.get_fields()]
        return self

    def __next__(self):
        pos: int = self.__iter_pos
        if self.__iter_pos < len(self.__iter_collection):
            self.__iter_pos += 1
            return self.__iter_collection[pos]
        else:
            self.__iter_pos = 0
            raise StopIteration

    def __len__(self) -> int:
        '''Return UDI characters sum'''
        length: int = 0
        for field in self.get_fields():
            length += len(field.value)
        return length

    def __str__(self) -> str:
        '''Return printable UDI characters'''
        fields = []
        for field in self.get_fields():
            fields.append(f"{field.name}: {field.value}")
        return ", ".join(fields)
