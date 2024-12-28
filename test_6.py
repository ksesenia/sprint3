people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(lambda name: print(f'Здравствуй, {name}!') if ('С' in name) else print(f'Привет, {name}!'), people)
