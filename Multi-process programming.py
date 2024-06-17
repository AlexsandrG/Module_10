import threading

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        action, product, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
            print(f"Received {quantity} units of {product}")
        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity
                print(f"Shipped {quantity} units of {product}")
            else:
                print(f"Insufficient quantity of {product} for shipment")

    def run(self, requests):
        threads = []
        for request in requests:
            thread = threading.Thread(target=self.process_request, args=(request,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

# Пример использования
warehouse = WarehouseManager()
requests = [("receipt", "apples", 100), ("shipment", "apples", 50), ("receipt", "bananas", 200)]
warehouse.run(requests)

# Вывод текущего состояния склада
print(warehouse.data)