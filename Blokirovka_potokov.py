# Реализуйте программу, которая имитирует доступ к общему
# ресурсу с использованием механизма блокировки потоков.
# Класс BankAccount должен отражать банковский счет с балансом и методами
# для пополнения и снятия денег. Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
# Пример работы
import threading


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print("Недостаточно средств на счету")


account = BankAccount(balance=1000)
threads = []

for i in range(5):
    deposit_thread = threading.Thread(target=account.deposit, args=(100,))
    withdraw_thread = threading.Thread(target=account.withdraw, args=(150,))
    threads.extend([deposit_thread, withdraw_thread])

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
