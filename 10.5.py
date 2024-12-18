from datetime import datetime
import multiprocessing
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            content = file.readline()
            all_data.append(content)
            if not content:
                break

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
on_ = datetime.now()

for i in files:
    print(i)
    read_info(i)
off_ = datetime.now()
time_line = off_ - on_
print(f'Время работы линейного вызова : {time_line}')

if __name__ == '__main__':
    on_2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    off_2 = datetime.now()
    time_of_multiprocessing = off_2 - on_2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')
