def is_matching_pair(opening, closing):
    pairs = {')': '(', '}': '{', ']': '['}
    return pairs[closing] == opening

def check_brackets(expression):
    stack = []
    errors = []
    
    # Опрацьовуємо весь рядок
    for index, char in enumerate(expression):
        if char in "({[":
            stack.append((char, index))
        elif char in ")}]":
            if stack and is_matching_pair(stack[-1][0], char):
                stack.pop()
            else:
                errors.append(f"Помилка на позиції {index}: '{char}' не має відповідної відкриваючої дужки")
    
    # Перевіряємо залишкові елементи у стеці
    while stack:
        unclosed_char, unclosed_index = stack.pop()
        errors.append(f"Помилка на позиції {unclosed_index}: '{unclosed_char}' не має відповідної закриваючої дужки")

    return errors if errors else ["Розставлення дужок правильне"]

def main():
    expression = "[ { ( } ) { ] [ } ( [ ] ) { }"
    errors = check_brackets(expression)
    for error in errors:
        print(error)

if __name__ == "__main__":
    main()
