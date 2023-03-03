a = { "Users": [ { "id": 1, "employee": { "department": "tech", "name": "Mark", "project": [ { "id": 2, "name": "Test", "status": "ok", "mistakes": [] } ] } }, { "id": 2, "employee": { "department": "tech", "name": "Alex", "project": [ { "id": 3, "name": "parser", "status": "filed", "mistakes": [ 404, "IO error" ] } ] } } ] }
b = ['Users', 'id', 1, 'employee', 'department', 'tech', 'name', 'Mark', 'project', 2, 'Test', 'status', "ok", 'mistakes', 'Alex', 3, 'parser', 'filed', 404, 'IO error']


class DictionaryParser:
    stop = False

    def __init__(self, data):
        self.data = data
        self.result = list()

    def add_item(self, item):
        self.result.append(item)

    def add_dict(self, data):
        for key, value in data.items():
            self.add_item(key)
            self.add_or_next(value)

    def add_list(self, data):
        for key in data:
            self.add_or_next(key)

    def add_or_next(self, data):
        if isinstance(data, dict):
            self.add_dict(data)
        elif isinstance(data, list):
            self.add_list(data)
        else:
            self.add_item(data)

    def parse(self):
        self.add_or_next(self.data)
        return list(set(self.result))


parser = DictionaryParser(a)
result = parser.parse()
print(result)
print(len(result))
print(len(b))
result = sorted(result)
b = sorted(b)
print(result==b)
