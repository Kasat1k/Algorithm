class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

def main():
    main_stack = Stack()
    even_stack = Stack()
    odd_stack = Stack()

    print("Введіть цілі числа. Для завершення введення введіть 'stop':")

    while True:
        user_input = input()
        if user_input.lower() == 'stop':
            break
        try:
            number = int(user_input)
            main_stack.push(number)
        except ValueError:
            print("Введіть коректне ціле число або 'stop' для завершення.")

    print("Основний стек:", main_stack.display())

    while not main_stack.is_empty():
        number = main_stack.pop()
        if number % 2 == 0:
            even_stack.push(number)
        else:
            odd_stack.push(number)

    print("Стек з парними числами:", even_stack.display())
    print("Стек з непарними числами:", odd_stack.display())

if __name__ == "__main__":
    main()
