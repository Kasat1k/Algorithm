import random
import matplotlib.pyplot as plt
import networkx as nx

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def visualize(self):
        if not self.heap:
            print("Heap is empty")
            return
        G = nx.DiGraph()
        for i in range(len(self.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap):
                G.add_edge(self.heap[i], self.heap[left])
            if right < len(self.heap):
                G.add_edge(self.heap[i], self.heap[right])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color='lightblue')
        plt.show()

heap = BinaryHeap()
def input_number_of_elements():
    while True:
        try:
            n = int(input("Введіть кількість елементів (більше 10): "))
            if n > 10:
                return n
            else:
                print("Будь ласка, введіть число більше 10.")
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")

num_elements = input_number_of_elements()
random_keys = random.sample(range(101), num_elements)
print("Випадкові ключі:", random_keys)

for key in random_keys:
    heap.insert(key)

heap.visualize()

# Видалення мінімального 
min_key = heap.delete_min()
print("Видаляємо мінімальний ключ:", min_key)

heap.visualize()
