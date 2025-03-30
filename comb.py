from functools import partial

def _sort_users_by_age(users, reverse=False):
    """Сортирует список пользователей по возрасту."""
    return sorted(users, key=lambda user: user['age'], reverse=reverse)

# Создание частичных функций
sort_ascending = partial(_sort_users_by_age, reverse=False)
sort_descending = partial(_sort_users_by_age, reverse=True)

# Пример использования
if __name__ == "__main__":
    users = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]

    print("По возрастанию:", sort_ascending(users))
    print("По убыванию:", sort_descending(users))