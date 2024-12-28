class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28
    def __init__(self, first_name_value,second_name_value,gender_value):
        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value

# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name_value = 'Роберт',second_name_value = 'Крузо',gender_value = 'м')
employee2 = Employee(first_name_value = 'Роб',second_name_value = 'Кру',gender_value = 'ж')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, Фамилия:{employee1.second_name}, Пол:{employee1.gender}, Отпускных дней в году:{employee1.vacation_days}.')