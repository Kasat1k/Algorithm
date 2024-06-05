import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

# Генерація ключів
keys = random.sample(range(101), 15)

# Побудова дерева
root = None
for key in keys:
    root = insert(root, key)

# Виведення 
print("BST з випадковими ключами:", keys)
print("\nПрямий обхід:")
preorder_traversal(root)
print("\n\nСиметричний обхід:")
inorder_traversal(root)
print("\n\nОбернений обхід:")
postorder_traversal(root)
