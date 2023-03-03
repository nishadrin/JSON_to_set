from typing import List, Dict


class DictionaryParser:
    def __init__(self) -> None:
        self.data = None
        self.result = list()

    def add_item(self, item) -> None:
        self.result.append(item)

    def add_dict(self, data: Dict) -> None:
        for key, value in data.items():
            self.add_item(key)
            self.add_or_next(value)

    def add_list(self, data: List) -> None:
        for key in data:
            self.add_or_next(key)

    def add_or_next(self, data: Dict) -> None:
        if isinstance(data, dict):
            self.add_dict(data)
        elif isinstance(data, list):
            self.add_list(data)
        else:
            self.add_item(data)

    def to_set(self, data: Dict) -> List:
        self.data = data
        self.add_or_next(self.data)
        return list(set(self.result))
