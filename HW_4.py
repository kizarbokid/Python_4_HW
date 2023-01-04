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


def toWriteSomeStrInTXT(value: str, filename):
    with open(filename, "w") as file:
        file.write(value)
    return print(f'Запись файла {filename} завершена')


def toReadSomeStrFromTXT(filename):
    with open(filename, "r") as file:
        content = file.read()
    print(f'Импорт из файла {filename} завершен')
    return content


def toGetValuesFromString(string):
    values_dict = dict()
    string = string.replace('-', '+-')
    values_list = [string for string in string.split('+')]
    if values_list[0] == '':  # если первый многочлен <0 то первый элемент пустая строка, уберем его
        del values_list[0]
    # определить степень многочлена
    length = int(values_list[0][values_list[0].find('^')+1:])
    for i in range(length, 0, -1):
        values_dict[i] = 0
    # записать свободный член
    if '*' not in values_list[-1] and ('x' not in values_list[-1]):
        values_dict[0] = int(values_list[-1])
        values_list.pop()
    else:
        values_dict[0] = 0
    # записать член в степени 1, если такой существует
    for value in values_list:
        if ('x' in value) and ('^' not in value):
            if len(value) > 1:
                values_dict[1] = int(value[:value.find('*')])
                values_list.pop()
            else:
                values_dict[1] = 1
    # записать в словарь все остальные члены
    for value in values_list:
        if '*' in value:
            values_dict[int(value[value.find('^')+1:])
                        ] = int(value[:value.find('*')])
        else:  # если нет знака умножения, значит коэффициент=1
            values_dict[int(value[value.find('^')+1:])] = 1

    return values_dict


def toSumPolynom(dict_1: dict, dict_2: dict):
    sum_dict = dict()
    for i in range(len(dict_1)-1,-1,-1):
        sum_dict[i]=dict_1[i]+dict_2[i]
    return sum_dict 


low = -100
high = 100 + 1
k = int(input('Введите степень многочлена k: '))
my_dict = toCreateKoefForPolynomial(k, low, high)
my_str = toCreatePolynomialStr(my_dict)
toWriteSomeStrInTXT(my_str, 'polynomial1.txt')
my_dict = toCreateKoefForPolynomial(k, low, high)
my_str = toCreatePolynomialStr(my_dict)
toWriteSomeStrInTXT(my_str, 'polynomial2.txt')
import_str1 = toReadSomeStrFromTXT('polynomial1.txt')
import_str2 = toReadSomeStrFromTXT('polynomial2.txt')
import_dict1 = toGetValuesFromString(import_str1)
import_dict2 = toGetValuesFromString(import_str2)
sum_polinom_dict=toSumPolynom(import_dict1,import_dict2)
my_str = toCreatePolynomialStr(sum_polinom_dict)
toWriteSomeStrInTXT(my_str, 'sum_polinom.txt')