import threading
from threading import Thread
import time
import random
from queue import Queue


class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        random_time = random.randint(3,10)
        time.sleep(random_time)

class Cafe:
    list_thr = []
    def __init__(self,*tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        # Преобразуем переданных гостей в список для удобства работы с ними
        list_guests = list(guests)
        # Получаем список доступных столов из атрибута класса
        list_tables = self.tables
        # Определяем количество гостей
        len_list_guests = len(list_guests)
        # Определяем минимальное количество гостей и столов, чтобы избежать выхода за границы
        min_guests_tables = min(len_list_guests, len(self.tables))
        # Распределяем гостей по столам
        for i in range(min_guests_tables):
            # Назначаем гостя на стол
            list_tables[i].guest = guests[i]
            # Запускаем поток для обработки гостя
            thr1 = guests[i]
            thr1.start()
            # Добавляем поток в общий список потоков кафе
            Cafe.list_thr.append(thr1)
            # Выводим сообщение о том, что гость сел за стол
            print(f'{list_guests[i].name} сел(-а) за стол номер {list_tables[i].number}')
        # Если гостей больше, чем доступных столов, добавляем оставшихся в очередь
        if len_list_guests > min_guests_tables:
            for i in range(min_guests_tables, len_list_guests):
                # Добавляем гостя в очередь
                self.queue.put(guests[i])
                # Выводим сообщение о том, что гость в очереди
                print(f'{list_guests[i].name} в очереди')

    def discuss_guests(self):
        # Продолжаем обсуждение гостей, пока очередь не пуста или есть свободные столы
        while not (self.queue.empty()) or Cafe.check_table(self):
            # Проходим по всем столам в кафе
            for table in self.tables:
                # Проверяем, есть ли гость за столом и жив ли он
                if not (table.guest is None) and not (table.guest.is_alive()):
                    # Если гость покинул стол, выводим сообщение об этом
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    # Освобождаем стол, устанавливая значение guest в None
                    table.guest = None
                # Проверяем, есть ли гости в очереди и свободен ли стол
                if (not (self.queue.empty())) and table.guest is None:
                    # Берём следующего гостя из очереди и сажаем его за стол
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    # Запускаем поток для нового гостя
                    thr1 = table.guest
                    thr1.start()
                    # Добавляем поток в общий список потоков кафе для отслеживания
                    Cafe.list_thr.append(thr1)
    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
