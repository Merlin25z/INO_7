import itertools

def get_combinations(s, k):
    """Возвращает все комбинации символов строки s с длинами от 1 до k."""
    result = []
    for r in range(1, k + 1):
        comb = itertools.combinations(s, r)
        result.extend([''.join(c) for c in comb])
    return result

# Пример использования
if __name__ == "__main__":
    s = input("Введите строку: ")
    k = int(input("Введите максимальную длину комбинаций (k): "))
    print("Результат:", get_combinations(s, k))