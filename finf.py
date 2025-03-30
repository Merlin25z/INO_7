def get_list(numbers_str):
    """Преобразует строку чисел в список целых чисел."""
    return [int(num) for num in numbers_str.split()]

def sort_func(func, input_str):
    """Сортирует результат переданной функции."""
    numbers = func(input_str)
    return sorted(numbers)

# Ввод данных
input_str = input("Введите целые числа через пробел: ")

# Обработка и вывод
result = sort_func(get_list, input_str)
print("Отсортированный список:", result)