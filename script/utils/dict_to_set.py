from typing import List, Dict, Set


class DictionaryParser:
    """
    Convert dictionary to set.
    """
    def __init__(self) -> None:
        self.result = set()

    def add_to_set(self, data: Dict) -> Set:
        """
        Add dictionary to set and return it.
        :param data: Dict
        :return: self.result: List
        """
        self.add_or_next(data)
        return self.result

    def clear_result(self):
        self.result = set()

    def __add_item(self, item) -> None:
        self.result.add(item)

    def __add_dict(self, data: Dict) -> None:
        for key, value in data.items():
            self.__add_item(key)
            self.add_or_next(value)

    def __add_list(self, data: List) -> None:
        for key in data:
            self.add_or_next(key)

    def add_or_next(self, data: Dict) -> None:
        """
        Add dictionary to result.
        :param data:
        :return:
        """
        if isinstance(data, dict):
            self.__add_dict(data)
        elif isinstance(data, list):
            self.__add_list(data)
        else:
            self.__add_item(data)
