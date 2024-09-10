import threading
import time
from data_Loader import DataLoader
from json_Saver import initialize_json_file, save_to_json, finalize_json_file


def main():
    start_time = time.time()
    data_loader = DataLoader()

    threads = []
    for i in range(1, 178):
        thread = threading.Thread(target=data_loader.load_data, args=(i,))
        threads.append(thread)
        thread.start()

    #
    for thread in threads:
        thread.join()

    initialize_json_file()
    save_to_json(data_loader.result)
    finalize_json_file()

    print("Time taken:", time.time() - start_time)


if __name__ == "__main__":
    main()
