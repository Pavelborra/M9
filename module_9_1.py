def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов

    # Перебираем все функции из *functions
    for func in functions:
        # Вызываем функцию с переданным списком и сохраняем результат в словаре
        results[func.__name__] = func(int_list)

    return results  # Возвращаем словарь с результатами

# Примеры использования функции apply_all_func
print(apply_all_func([6, 20, 15, 9], max, min))  # Вывод: {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# Вывод: {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}