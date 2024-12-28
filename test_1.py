import datetime
from decimal import Decimal
DATE_FORMAT = '%Y-%m-%d'
goods = {'Фабрика №2: яйца': [{'amount': Decimal('2'),
                       'expiration_date': datetime.date(2024, 12, 3)},
                      {'amount': Decimal('3'),
                       'expiration_date': datetime.date(2024, 12, 5)}],
 'Яйца Фабрики №1': [{'amount': Decimal('1'),
                      'expiration_date': datetime.date(2024, 12, 7)}],
 'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]}



def add(items, title, amount, expiration_date=None):
    if expiration_date == None:
        new_food = {'amount': amount, 'expiration_date': None}
    else:
        new_food = {'amount': amount, 'expiration_date': datetime.date.fromisoformat(expiration_date)}
    if title in items.keys():
        items[title].append(new_food)
    else:
        items[title] = list()
        items[title].append(new_food)


def add_by_note(items, note):
    string_1 = str.split(note,' ')
    date = string_1[len(string_1)-1]
    try:
        datetime.datetime.strptime(date, DATE_FORMAT)
        delta_date = 2
    except Exception:
        date = None
        delta_date = 1
    amount = Decimal(string_1[len(string_1) - delta_date])
    title = [date for date in string_1[0:len(string_1) - delta_date]]
    title = ' '.join(title)
    add(items, title, amount, date)

add_by_note(goods,'Макароны 1.5')

def find(items, needle):
    string_2 = []
    for string in items.keys():
        if needle.lower() in string.lower():
           list.append(string_2, string)
    return string_2
print(find(goods,'яйца'))

def amount(items, needle):
    mass = 0
    food_list = find(items, needle)
    for key_dict in food_list:
        dict_food = items[key_dict]
        for food in dict_food:
            mass += food['amount']
    return mass

amount(goods, 'яйца')
def expire(items, in_advance_days=0):
    list_expire = []
    today = datetime.date.today()
    date_food_fresh = today + datetime.timedelta(in_advance_days)
    for key_dict in items:
        dict_food = items[key_dict]
        quantity = 0
        for date_food in dict_food:
            date = date_food['expiration_date']
            if date != None:
                if date <= date_food_fresh:
                    quantity += float(date_food['amount'])
        if quantity > 0:
            list_expire.append((key_dict, Decimal(str(quantity))))
    print(tuple(list_expire))


expire(goods)