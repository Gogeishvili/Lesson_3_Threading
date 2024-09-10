import threading
import requests


class DataLoader:

    def __init__(self):
        self.__result = []
        self.__locker = threading.Lock()

    @property
    def result(self):
        return self.__result

    def load_data(self, i):
        API = f'https://jsonplaceholder.typicode.com/posts/{i}'
        response = requests.get(API)
        if response.status_code == 200:
            with self.__locker:
                self.__result.append(response.json())
