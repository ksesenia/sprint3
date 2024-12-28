# Импортируйте нужную библиотеку.
from datetime import datetime

class Store:
    def __init__(self, address):
        self.address: str = address

    def __is_open(self, date) -> bool:
        return False

    def get_info(self, text_date) -> str:
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(text_date, '%d.%m.%Y')
        # Передайте в метод __is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.__is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {text_date} {info}'


class MiniStore(Store):
    # Переопределите метод __is_open().
    def __is_open(self, date: datetime) -> bool:
        date_object = date.weekday()
        if date_object > 5:
            return False
        return True



class WeekendStore(Store):
    # Переопределите метод __is_open().
    def __is_open(self, date: datetime) -> bool:
        date_object = date.weekday()
        if date_object > 5:
            return True
        return False


class NonStopStore(Store):

    # Переопределите метод __is_open().
    def __is_open(self, date: datetime) -> bool:
        return True

mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))