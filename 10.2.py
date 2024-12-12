import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали')
        wargs = 100
        x = 0
        while wargs > 0:
            x += 1
            time.sleep(1)
            wargs -= self.power
            print(f'{self.name} сражается {x} день, осталось {wargs} врагов')


            if wargs <= 0:
                print(f'{self.name} одержал победу на {x} день')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

