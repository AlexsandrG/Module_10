import threading
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(threading.Thread):
    def __init__(self, number, table, cafe):
        threading.Thread.__init__(self)
        self.number = number
        self.table = table
        self.cafe = cafe

    def run(self):
        print(f"Посетитель номер {self.number} прибыл.")
        if self.table.is_busy:
            print(f"Посетитель номер {self.number} ожидает свободный стол.")
            self.cafe.queue.put(self)
        else:
            self.table.is_busy = True
            print(f"Посетитель номер {self.number} сел за стол {self.table.number}. (начало обслуживания)")
            time.sleep(5)
            self.table.is_busy = False
            print(f"Посетитель номер {self.number} покушал и ушёл. (конец обслуживания)")

class Cafe:
    def __init__(self, tables):
        self.tables = [Table(number)for number in tables]
        self.queue = Queue()

    def customer_arrival(self):
        for i in range(20):
            table = None
            for t in self.tables:
                if not t.is_busy:
                    table = t
                    break
            if table:
                customer = Customer(i, table, self)
                customer.start()
            else:
                customer = Customer(i, None, self)
                customer.start()
            time.sleep(1)

    def serve_customer(self, customer):
        if customer.table is None:
            while customer.table is None:
                if not self.queue.empty():
                    customer.table = self.queue.get()
            customer.run()

# Создаем сеть кафе
cafe = Cafe([1, 2, 3])

# Моделируем приход посетителей
cafe.customer_arrival()

# В этом коде класс `Table` представляет стол в кафе, с атрибутами
# номера стола и информацией о занятости. Класс `Customer` представляет
# посетителя-поток, который при приходе оценивает доступность столов
# и либо занимает свободный стол, либо становится в очередь.
#
# Класс `Cafe` управляет процессами кафе, инициализируя столы
# и очередь, а также запуская потоки посетителей.
# Метод `customer_arrival` моделирует появление новых посетителей,
# а метод `serve_customer` обслуживает посетителей в зависимости
# от доступных столов и условий очереди.
#
# Этот код создаст симуляцию работы кафе с несколькими
# столами и посетителями, отображая соответствующие сообщения о событиях