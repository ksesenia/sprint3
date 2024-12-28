# Импортируйте необходимые модули.
from datetime import datetime

def validate_record(name: str, birthdate: str) -> bool:
    try:
        datetime.strptime(birthdate, '%d.%m.%Y')
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birthdate}')
        return False

def process_people(entries: list) -> dict:
    # Объявите счётчики.
    good_count: int = 0
    bad_coun: int = 0
    # Распакуйте кортежи из полученного списка entries.
    for name, birthdate in entries:
        correct = validate_record(name, birthdate)
        if correct:
            good_count += 1
        else:
            bad_coun += 1
    dict_good_bad = {'good': good_count, 'bad': bad_coun}
    # Верните словарь.
    return dict_good_bad


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')