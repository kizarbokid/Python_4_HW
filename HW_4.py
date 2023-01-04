from random import randrange


def toCreateKoefForPolynomial(value, low_v, high_v):
    polynomial_dict = dict()
    for i in range(k, -1, -1):  # от К до 0
        polynomial_dict[i] = randrange(low_v, high_v)
        if i == k:  # чтобы 1ый элемент не был равен 0
            while polynomial_dict[i] == 0:
                polynomial_dict[i] = randrange(low_v, high_v)
    return polynomial_dict


def toCreatePolynomialStr(polynomial_dict):
    polynomial_str = ''
    for key, value in polynomial_dict.items():
        if value == 0 and key != 0:  # если значение 0 то не добавляем в строку, переходим к следующему
            continue
        elif value == 1 and key != 0 and key != 1:  # если значение 1, то незачем записывать коэффициент перед Х
            polynomial_str += 'x^'+str(key)+'+'
        elif key == 1 and value != 1:  # если ключ =1 и значение <>1 то не писать показатель степени
            polynomial_str += str(value)+'*x'+'+'
        elif key == 1 and value == 1:  # перед элементом с со степенью 1 и кэффиц 1 незачем ставить возведение в степень
            polynomial_str += 'x'+'+'
        elif key == 0:  # если последний свободный член, то закончить
            if value != 0:
                polynomial_str += str(value)+'+'
            polynomial_str = polynomial_str.replace('+-', '-')
            # последний символ минуса- некарсиво
            polynomial_str = polynomial_str[::-1].replace('+', '', 1)
            polynomial_str = polynomial_str[::-1]
            return polynomial_str
        else:
            polynomial_str += str(value)+'*x^'+str(key)+'+'


def toWriteSomePolyInTXT(value: str, filename):
    with open(filename, "w") as file:
        file.write(value)
    return print(f'Запись файла {filename} завершена')


low = -100
high = 101
k = int(input('Введите степень многочлена k: '))
my_dict = toCreateKoefForPolynomial(k, low, high)
my_str = toCreatePolynomialStr(my_dict)
toWriteSomePolyInTXT(my_str, 'polynomial1.txt')
my_dict = toCreateKoefForPolynomial(k, low, high)
my_str = toCreatePolynomialStr(my_dict)
toWriteSomePolyInTXT(my_str, 'polynomial2.txt')
