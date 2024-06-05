def union(set1, set2):
    return list(set(set1) | set(set2))

def intersection(set1, set2):
    return list(set(set1) & set(set2))

def difference(set1, set2):
    return list(set(set1) - set(set2))

def symmetric_difference(set1, set2):
    return list(set(set1) ^ set(set2))

def complement(universal_set, subset):
    return list(set(universal_set) - set(subset))

def main():
    set1 = [1, 2, 3, 4, 5]
    set2 = [4, 5, 6, 7, 8]
    universal_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Універсальна множина

    print("Множина 1:", set1)
    print("Множина 2:", set2)
    print("Універсальна множина:", universal_set)
    
    print("Об'єднання:", union(set1, set2))
    print("Перетин:", intersection(set1, set2))
    print("Різниця (Множина 1 - Множина 2):", difference(set1, set2))
    print("Різниця (Множина 2 - Множина 1):", difference(set2, set1))
    print("Симетрична різниця:", symmetric_difference(set1, set2))
    print("Доповнення (Універсальна множина - Множина 1):", complement(universal_set, set1))
    print("Доповнення (Універсальна множина - Множина 2):", complement(universal_set, set2))

if __name__ == "__main__":
    main()
