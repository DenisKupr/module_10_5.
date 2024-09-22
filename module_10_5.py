import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == "__main__":
    # Список файлов
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print("Линейный вызов:")
    print(time.time() - start_time)

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print("Многопроцессорный вызов:")
    print(time.time() - start_time)
