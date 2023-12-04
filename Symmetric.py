# Троичная симметричная система счисления

#& 10 -> 3
def decimal_to_symmetric_ternary(decimal_num):
    decimal_znach = int(str(decimal_num).split('.')[0])
    decimal_drob = float(f"0.{int(str(decimal_num).split('.')[1])}")

    result_znach = ""
    while decimal_znach != 0:
        remainder = decimal_znach % 3

        if remainder == 2:
            decimal_znach = decimal_znach // 3 + 1
            remainder = "-"
        elif remainder == 1:
            remainder = '+'
            decimal_znach //= 3
        else:
            decimal_znach //= 3

        result_znach = str(remainder) + result_znach


    result_drob = ''
    if decimal_drob == 0:
        return ""

    precision = 12  # Задайте желаемую точность дробной части

    # Обработка дробной части
    print(decimal_drob)
    while decimal_drob != 0 and len(result_drob) <= precision:
        decimal_drob *= 3
        digit = int(decimal_drob)
        decimal_drob -= digit

        if digit == 2:
            # digit = -1
            digit = "-"
        if digit == 1:
            digit = "+"

        result_drob += str(digit)
    
    summ = 0
    for index, i in enumerate(result_drob):
        if i == '+':
            summ += (3 ** -(index + 1))
            print((3 ** -(index + 1)), -(index + 1))
        elif i == '-':
            summ += -1 * (3 ** -(index + 1))
            print(-(3 ** -(index + 1)), -(index + 1))
        else:
            summ = summ
    
    print(summ)
    return result_znach + '.' + result_drob

# Пример использования
decimal_number = -999.9999
symmetric_ternary = decimal_to_symmetric_ternary(decimal_number)
print(f"Десятичное число {decimal_number} в троичной симметричной системе: {symmetric_ternary}")



#& 10 <- 3
def symmetric_ternary_to_decimal(symmetric_num):
    pass