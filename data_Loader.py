import threading
import requests
import concurrent.futures


class DataLoader:

    def __init__(self):
        self.__result = []
        self.__lock=threading.Lock()

    @property
    def result(self):
        return self.__result

    def __fetch_and_save_data(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            with self.__lock:
                self.__result.append(response.json())
        else:
            print("incorrect data")

    def load_data(self, base_api, start_id, end_id):
        threads = []
        for i in range(start_id, end_id):
            api = f"{base_api}{i}"
            thread = threading.Thread(target=self.__fetch_and_save_data, args=(api,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    def load_data_2(self, base_api, start_id, end_id):
        with concurrent.futures.ThreadPoolExecutor() as TP:
            for i in range(start_id, end_id):
                api = f"{base_api}{i}"
                TP.submit(self.__fetch_and_save_data, api)
