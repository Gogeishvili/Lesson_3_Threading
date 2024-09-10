import threading
import time
from data_Loader import DataLoader
from json_Saver import initialize_json_file, save_to_json, finalize_json_file


def main():
    API = "https://jsonplaceholder.typicode.com/posts/"

    start_time = time.time()

    data_loader = DataLoader()
    data_loader.load_data(API,1,78)

    initialize_json_file()
    save_to_json(data_loader.result)
    finalize_json_file()

    print("Time taken:", time.time() - start_time)


if __name__ == "__main__":
    main()
