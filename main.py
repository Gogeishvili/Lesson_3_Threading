import time
from data_Loader import DataLoader
from data_Saver import DataSaver


def main():
    API = "https://jsonplaceholder.typicode.com/posts/"

    start_time = time.time()

    data_loader = DataLoader()
    data_loader.load_data(API, 1, 78)

    data_saver = DataSaver()
    data_saver.save_data(data_loader.result)

    print("Time taken:", time.time() - start_time)


if __name__ == "__main__":
    main()
