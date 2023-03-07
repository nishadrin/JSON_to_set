import sys
from typing import List, Dict, Set, Union


class DictionaryToSet:
    """
    Convert dictionary to set.
    :param recursion_limit: Optional[int]
    :return
    """
    __slots__ = ['data', 'recursion_limit']

    def __init__(self, recursion_limit: int = None) -> None:
        self.data = set()
        self.recursion_limit = recursion_limit
        self.__set_recursion_limit()

    def add_to_set(self, dictionary: Dict) -> Set:
        """
        Add dictionary to set and return it.
        :param dictionary: Dict
        :return: self.data: Set
        """
        self.add_or_next(dictionary)
        return self.data

    def clear_data(self) -> None:
        self.data = set()

    def add_or_next(self, dictionary: Dict) -> None:
        """
        Add dictionary to self.data.
        :param dictionary: Dict
        :return:
        """
        if isinstance(dictionary, dict):
            self.__add_dict(dictionary)
        elif isinstance(dictionary, list):
            self.__add_list(dictionary)
        elif isinstance(dictionary, int) or isinstance(dictionary, str):
            self.__add_item(dictionary)
        else:
            raise Exception(
                f'Wrong input data type. Awaited: dict, list, str or int. Get - '
                f'{type(dictionary)}')

    def __set_recursion_limit(self):
        if self.recursion_limit is not None:
            sys.setrecursionlimit(self.recursion_limit)

    def __add_item(self, item: Union[str, int]) -> None:
        self.data.add(item)

    def __add_dict(self, dictionary: Dict) -> None:
        for key, value in dictionary.items():
            self.__add_item(key)
            self.add_or_next(value)

    def __add_list(self, data: List) -> None:
        for key in data:
            self.add_or_next(key)
