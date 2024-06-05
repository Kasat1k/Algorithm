import random
import time
from queue import Queue

class Customer:
    def __init__(self, id):
        self.id = id
        self.items = random.randint(1, 20)  
        self.service_time = self.items * random.uniform(0.1, 0.5)  

    def __repr__(self):
        return f"Customer {self.id} with {self.items} items"

class StoreQueue:
    def __init__(self, num_queues):
        self.queues = [Queue() for _ in range(num_queues)]

    def add_customer(self, customer):
        min_queue = min(self.queues, key=lambda q: q.qsize())
        min_queue.put(customer)
        print(f"{customer} added to queue {self.queues.index(min_queue) + 1}")

    def process_queues(self):
        for i, queue in enumerate(self.queues):
            if not queue.empty():
                customer = queue.queue[0]
                print(f"Processing {customer} in queue {i + 1}")
                time.sleep(customer.service_time) 
                queue.get()
                print(f"{customer} finished in queue {i + 1}")
            else:
                print(f"Queue {i + 1} is empty")

def main():
    num_queues = 3  # Кількість черг
    store_queue = StoreQueue(num_queues)
    customer_id = 1

    while True:
        print("\n--- Новий клієнт приходить до каси ---")
        customer = Customer(customer_id)
        store_queue.add_customer(customer)
        customer_id += 1

        print("\n--- Обробка черг ---")
        store_queue.process_queues()
        print("\n--- Кінець обробки ---")

        time.sleep(2)  # Затримка 
        if customer_id > 10:  # Вихід з циклу після обробки 10 покупців
            break

if __name__ == "__main__":
    main()
