#Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
#Найти самого успешного и самого отстающего по среднему баллу.

class_list = {'Ivanov Ivan': [6, 8, 10, 7, 6], 'Petrov Petia': [5, 9, 7, 10, 11], 'Sidorov Semen': [4, 6, 5, 9, 9]}


def fun(grade):
    return sum(grade) / len(grade)


new_class_list = sorted(class_list.keys(), key=lambda students: fun(class_list[students]))

print('best:', new_class_list[0])
print('loser:', new_class_list[-1])
