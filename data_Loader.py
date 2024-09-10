import threading
import requests


class DataLoader:

    def __init__(self):
        self.__result = []

    @property
    def result(self):
        return self.__result

    def __fetch_and_save_data(self, api, lock):
        response = requests.get(api)
        if response.status_code == 200:
            with lock:
                self.__result.append(response.json())
        else:
            print("incorrect data")

    def load_data(self, base_api, start_id, end_id):
        lock = threading.Lock()
        threads = []
        for i in range(start_id, end_id):
            api = f"{base_api}{i}"
            thread = threading.Thread(target=self.__fetch_and_save_data, args=(api, lock,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
