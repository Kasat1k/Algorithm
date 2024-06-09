import random
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color='black')
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert_node(new_node)
        self._fix_insert(new_node)

    def _insert_node(self, node):
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        node.color = 'red'

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, data):
        node = self._search(self.root, data)
        if node is self.NIL:
            return
        self._delete_node(node)

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _search(self, node, data):
        while node != self.NIL and data != node.data:
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return node

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def visualize(self):
        if self.root == self.NIL:
            print("Tree is empty")
            return
        G = nx.DiGraph()
        self._add_edges(self.root, G)
        pos = nx.planar_layout(G)
        colors = [G[u][v]['color'] for u, v in G.edges]
        nx.draw(G, pos, with_labels=True, edge_color=colors, node_size=500, font_size=10, node_color='lightblue')
        plt.show()

    def _add_edges(self, node, G):
        if node != self.NIL:
            if node.left != self.NIL:
                G.add_edge(node.data, node.left.data, color='black' if node.left.color == 'black' else 'red')
                self._add_edges(node.left, G)
            if node.right != self.NIL:
                G.add_edge(node.data, node.right.data, color='black' if node.right.color == 'black' else 'red')
                self._add_edges(node.right, G)

rbt = RedBlackTree()
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
    rbt.insert(key)

rbt.visualize()

key_to_delete = random.choice(random_keys)
print("Видаляємо ключ:", key_to_delete)
rbt.delete(key_to_delete)

rbt.visualize()