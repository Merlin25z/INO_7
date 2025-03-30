def check_length(city):
    return len(city) >= 3

# Ввод данных
cities_input = input("Введите названия городов через пробел: ")
cities_list = cities_input.split()

# Фильтрация
filtered_cities = [city for city in cities_list if check_length(city)]

# Вывод
print("Отфильтрованный список городов:", filtered_cities)
