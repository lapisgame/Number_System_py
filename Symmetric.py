from ChisloLib import chislo

# Троичная симметричная система счисления

#& 10 -> 3
def decimal_to_symmetric_ternary(decimal_num):
    decimal_znach = int(str(abs(decimal_num)).split('.')[0])
    decimal_drob = float(f"0.{int(str(abs(decimal_num)).split('.')[1])}")

    result_znach = ""
    while decimal_znach > 0:
        remainder = decimal_znach % 3
        result_znach += str(remainder)
        decimal_znach //= 3
    
    result_znach = result_znach[::-1]

    result_drob = ''
    if decimal_drob == 0:
        return ""

    precision = len(str(decimal_num).split('.')[1]) * 4  # Задайте желаемую точность дробной части

    # Обработка дробной части
    while decimal_drob != 0 and len(result_drob) < precision:
        decimal_drob *= 3
        digit = int(decimal_drob)
        decimal_drob -= digit

        result_drob += str(digit)
    
    a = chislo(f'{result_znach}.{result_drob}', 3, precision)
    b = chislo(f"{'1' * (len(result_znach) + 2)}.{'1' * len(result_drob)}", 3, precision)

    c = (a + b)
    res = ''
    to_minus_znach = c.znach
    to_minus_drob = c.drob

    for i in to_minus_znach:
        if i == '0':
            res += '-'
        elif i == '1':
            res += '0'
        else:
            res += '+'
    
    res += '.'

    for i in to_minus_drob:
        if i == '0':
            res += '-'
        elif i == '1':
            res += '0'
        else:
            res += '+'

    if decimal_num < 0:
        res_c = res
        res = ''
        for i in res_c:
            if i == '-':
                res += '+'
            elif i == '+':
                res += '-'
            elif i == '0':
                res += '0'
            else:
                res += '.'

    return res


#& 10 <- 3
def symmetric_ternary_to_decimal(symmetric_num):
    res = 0
    znach, drob = symmetric_num.split('.')
    znach = znach[::-1]

    for index, i in enumerate(znach):
        if i == '+':
            res += 3**index
        elif i == '-':
            res -= 3**index
        else:
            res += 0

    for index, i in enumerate(drob):
        if i == '+':
            res += 3**-(index + 1)
        elif i == '-':
            res -= 3**-(index + 1)
        else:
            res += 0

    return res

# Пример использования
decimal_number = -5.25
symmetric_ternary = decimal_to_symmetric_ternary(decimal_number)
print(f"Десятичное число {decimal_number} в троичной симметричной системе: {symmetric_ternary}")
decimal_number_2 = symmetric_ternary_to_decimal(symmetric_ternary)
print(decimal_number_2)