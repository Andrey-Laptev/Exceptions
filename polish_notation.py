s = input('Введите выражение, разделив его части пробелом: ').split()

try:
    x = s.pop(0)
    g = int(s.pop(0))
    z = int(s.pop(0))

    assert x in ['+', '-', '*', '/'], 'Ошибка! Ввод необходимо начинать с арифметического оператора (+, -, *, /)'

    if s:
        print('Ошибка! Введено слишком много данных!')
    elif x == '+':
        print(g + z)
    elif x == '-':
        print(g - z)
    elif x == '*':
        print(g * z)
    elif x == '/':
        print(g / z)
except ZeroDivisionError:
    print('Ошибка! На ноль делить нельзя!')
except IndexError:
    print('Ошибка! Недостаточно корректных данных!')
except ValueError:
    print('Ошибка! Введены буквы вместо цифр!')
except Exception:
    print('Ошибка! Некорректно введены данные!')

