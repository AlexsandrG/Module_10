import threading
from queue import Queue
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.customer_arrival = None
        self.tables = tables
        self.queue = Queue()


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe
        self.table = None


    def run(self):
        print(f"Посетитель номер {self.number} прибыл.")
        if self.table is None:
            if not any([t.is_busy for t in self.cafe.tables]):
                self.table = self.cafe.tables.pop(0)
                self.table.is_busy = True
                print(f"Посетитель номер {self.number} сел за стол {self.table.number}. (начало обслуживания)")
                time.sleep(5)
                self.table.is_busy = False
                print(f"Посетитель номер {self.number} покушал и ушёл. (конец обслуживания)")
            else:
                print(f"Посетитель номер {self.number} ожидает свободный стол. (помещение в очередь)")
                self.cafe.queue.put(self)
        else:
            time.sleep(5)
            print(f"Посетитель номер {self.number} покушал и ушёл. (конец обслуживания)")


def customer_arrival(self):
    for i in range(20):
        time.sleep(1)
        customer = Customer(i + 1, self)
        customer.start()

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запустим поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы потока прибытия посетителей
customer_arrival_thread.join()
