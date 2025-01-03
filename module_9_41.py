from random import choice  # Импортируем функцию choice из модуля random для случайного выбора

# Часть 1: Lambda-функция для сравнения строк
first = 'Мама мыла раму'  # Первая строка
second = 'Рамена мало было'  # Вторая строка

# Создаем lambda-функцию для сравнения символов двух строк
result = list(map(lambda x, y: x == y, first, second))  # Используем map для применения lambda-функции к парам символов
print(result)  # Выводим результат: список совпадений букв в одинаковых позициях

# Часть 2: Замыкание для записи в файл
def get_advanced_writer(file_name):
    # Определяем внутреннюю функцию для записи данных в файл
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:  # Открываем файл в режиме добавления с кодировкой UTF-8
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything  # Возвращаем внутреннюю функцию

# Пример использования замыкания
write = get_advanced_writer('example.txt')  # Создаем функцию записи в файл example.txt
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])  # Записываем данные в файл

# Часть 3: Класс MysticBall с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные слова в атрибуте words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из коллекции words

# Пример использования класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')  # Создаем объект класса MysticBall с тремя словами
print(first_ball())  # Вызываем объект как функцию для получения случайного слова
print(first_ball())  # Вызываем объект как функцию для получения случайного слова
print(first_ball())  # Вызываем объект как функцию для получения случайного слова