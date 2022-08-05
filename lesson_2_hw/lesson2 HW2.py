password = input()
if len(password) < 6:
    print('пароль короткий')
else:
    print('пароль соответствует нужной длинне')
if 'K' in password and 'F' in password and ('D' in password or 'C' in password):
    print('Ок')
else:
    print('нужные буквы не найдены')
if ('1'and '6') in password:
    print('недопустимые цифры')
else:
    print('Ok')
if '#' in password and not 'a' in password:
    print('Ошибка')
else:
    print('Ок')
