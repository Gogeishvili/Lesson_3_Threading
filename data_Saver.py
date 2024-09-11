import json


class DataSaver:

    def __init__(self, file_name="data.json"):
        self.__file_name = file_name

    def save_data(self, items):
        with open(self.__file_name, 'w') as json_file:
            json.dump(items, json_file, indent=4)
