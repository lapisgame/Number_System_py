def replace(old_string, new_string, index):
    if index not in range(len(old_string)):
        raise ValueError('Index outside given string')
    
    if index < 0:
        return new_string + old_string
    
    if index == len(old_string):
        return old_string + new_string

    return old_string[:index] + new_string + old_string[index+1:]

def int10_to_dop(x_inp):
    if x_inp >= 0:
        raise ValueError('Дополнительный код возможно рассчитать только для отрицательных чисел, введите число < 0')

    x = abs(x_inp)
    y = ''

    #& Переводим в двоичную из десятичной
    while x>0:
        y = str(x%2) + y
        x = x // 2

    #& Дописываем нули впереди до нужного размера (8, 16, 32, 64)
    if len(y) < 8:
        y = '0' * (8 - len(y)) + y
    else:
        if len(y) < 16:
            y = '0' * (16 - len(y)) + y
        else:
            if len(y) < 32:
                y = '0' * (32 - len(y)) + y
            else:
                if len(y) < 64:
                    y = '0' * (64 - len(y)) + y

    #& Инвертируем
    y_inv = ''
    for i in y:
        if i == '0':
            y_inv += '1'
        else:
            y_inv += '0'

    #& Прибавляем 1
    z = y_inv
    point = len(z) - 1
    bit = 1

    while (point>=0) and (bit>0):
        if z[point] == '0':
            z = replace(z, '1', point)
            bit -= 1
        else:
            z = replace(z, '0', point)
        point -= 1

    return [y,y_inv,z]


def dop_to_int10(z):

    #& Вычитаем 1
    point = len(z) - 1
    bit = 1
    while (point>=0) and (bit>0):
        if z[point] == '1':
            z = replace(z, '0', point)
            bit -= 1
        else:
            z = replace(z, '1', point)
        point -= 1
    

    #& Инвертируем
    y = ''
    y_inv = z
    for i in y_inv:
        if i == '0':
            y += '1'
        else:
            y += '0'
    y = y[y.find('1')::]


    #& Из двоичного в десятичное представление
    x = 0
    count = 0
    for i in y[::-1]:
        digit = int(i)
        x += 2**count * digit
        count += 1
    x = -x

    return [y_inv, y, x]

x = int(input('x = '))
y,y_inv,z = int10_to_dop(x)
print(f'x_2 = {y}', f'x_2 inv = {y_inv}', f'x_2 inv + 1 = {z}', sep='\n', end='\n\n')

y_inv, y, x = dop_to_int10(z)
print(f'x_2 inv + 1 = {z}', f'x_2 inv = {y_inv}', f'x_2 = {y}', f'x = {x}', sep='\n')