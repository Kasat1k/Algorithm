import random
import matplotlib.pyplot as plt
import networkx as nx

class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.child = None
        self.sibling = None
        self.parent = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.degree <= h2.degree:
            h1.sibling = self.merge(h1.sibling, h2)
            return h1
        else:
            h2.sibling = self.merge(h1, h2.sibling)
            return h2

    def union(self, h1, h2):
        new_head = self.merge(h1, h2)
        if new_head is None:
            return None
        prev = None
        curr = new_head
        next = new_head.sibling
        while next is not None:
            if curr.degree != next.degree or (next.sibling is not None and next.sibling.degree == curr.degree):
                prev = curr
                curr = next
            else:
                if curr.key <= next.key:
                    curr.sibling = next.sibling
                    self.link(next, curr)
                else:
                    if prev is None:
                        new_head = next
                    else:
                        prev.sibling = next
                    self.link(curr, next)
                    curr = next
            next = curr.sibling
        return new_head

    def link(self, y, z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def insert(self, key):
        new_node = BinomialHeapNode(key)
        self.head = self.union(self.head, new_node)

    def get_min(self):
        if self.head is None:
            return None
        y = None
        x = self.head
        min_key = float('inf')
        while x is not None:
            if x.key < min_key:
                min_key = x.key
                y = x
            x = x.sibling
        return y

    def extract_min(self):
        if self.head is None:
            return None
        min_node = self.get_min()
        if min_node is None:
            return None
        min_node_parent = None
        x = self.head
        while x is not None:
            if x.sibling == min_node:
                min_node_parent = x
                break
            x = x.sibling
        if min_node_parent is None:
            self.head = min_node.sibling
        else:
            min_node_parent.sibling = min_node.sibling
        child = min_node.child
        new_head = None
        while child is not None:
            next = child.sibling
            child.sibling = new_head
            child.parent = None
            new_head = child
            child = next
        self.head = self.union(self.head, new_head)
        return min_node.key

    def visualize(self):
        if self.head is None:
            print("Heap is empty")
            return
        G = nx.DiGraph()
        self._add_edges(self.head, G)
        pos = nx.planar_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color='lightblue')
        plt.show()

    def _add_edges(self, node, G, parent=None):
        if node is not None:
            G.add_node(node.key)
            if parent is not None:
                G.add_edge(parent, node.key)
            self._add_edges(node.child, G, node.key)
            self._add_edges(node.sibling, G, parent)

def input_number_of_elements():
    while True:
        try:
            n = int(input("Введіть кількість елементів (більше 15): "))
            if n > 15:
                return n
            else:
                print("Будь ласка, введіть число більше 15.")
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")

binomial_heap = BinomialHeap()

num_elements = input_number_of_elements()

random_keys = random.sample(range(101), num_elements)
print("Випадкові ключі:", random_keys)

for key in random_keys:
    binomial_heap.insert(key)

binomial_heap.visualize()

min_key = binomial_heap.extract_min()
print("Видаляємо мінімальний ключ:", min_key)

binomial_heap.visualize()
