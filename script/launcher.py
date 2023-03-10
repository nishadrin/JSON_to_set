import json

import click

from utils.dict_to_set import DictionaryToSet

DEFAULT_PATH = './test.json'


@click.command()
@click.option('--path', default=DEFAULT_PATH, help='Path to JSON file')
def command_line(path):
    # Валидацию path не проводил, но она может быть уместна.
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    parser = DictionaryToSet()
    result = parser.add_to_set(data)

    # Для проверки используются эти значения, json лежит в файле test.json
    test_text = ['Users', 'id', '1', 'employee', 'department', 'tech', 'name',
                 'Mark',
                 'project', '2', 'Test', 'status', "ok", 'mistakes', 'Alex',
                 '3', 'parser',
                 'filed', '404', 'IO error']
    # Для возможности сортировать данные
    result = [str(i) for i in result]
    result = sorted(result)
    test_text = sorted(test_text)
    print(result)
    print(test_text)
    print(test_text == result)


if __name__ == '__main__':
    command_line()
