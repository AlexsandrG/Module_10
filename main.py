import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
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
                print("Insufficient funds")

    def get_balance(self):
        with self.lock:
            return self.balance


def perform_transactions(account):
    for _ in range(10):
        account.deposit(100)
        account.withdraw(50)


if __name__ == "__main__":
    account = BankAccount()
    threads = []


for _ in range(5):
    thread = threading.Thread(target=perform_transactions, args=(account,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(f"Final balance: {account.get_balance()}")