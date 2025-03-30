import itertools

def string_permutations(s, n):
    """Возвращает все перестановки длины n из символов строки s в лексикографическом порядке."""
    perms = itertools.permutations(s, n)
    return sorted([''.join(p) for p in perms])

# Пример использования
if __name__ == "__main__":
    s = input("Введите строку: ")
    n = int(input("Введите длину перестановок: "))
    print("Результат:", string_permutations(s, n))