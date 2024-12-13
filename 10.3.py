import threading
import random
import time

lock = threading.Lock()


class Bank(threading.Thread):

    def __init__(self, balance: int):
        threading.Thread.__init__(self)
        self.balance = balance
        self.lock = lock

    def deposit(self):
        n = 0

        while n < 3:
            num = random.randint(50, 500)
            self.balance = self.balance + num
            if self.balance >= 500 or lock.locked():
                lock.release()
            print(f"Пополнение: {num}. Баланс: {self.balance}")
            n += 1
        time.sleep(0.001)

    def take(self):
        n = 0
        while n < 3:
            num_ = random.randint(50, 500)
            print(f'Запрос на {num_}')
            if num_ <= self.balance:
                self.balance = self.balance - num_
                print(f"Снятие: {num_}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()
            n += 1


bk = Bank(0)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
