def sub_str(str:str):
    mini = {'0':'\u2080', 
            '1':'\u2081', '2':'\u2082', '3':'\u2083', 
            '4':'\u2084', '5':'\u2085', '6':'\u2086', 
            '7':'\u2087', '8':'\u2088', '9':'\u2089'
    }

    res = ""
    for i in str:
        res += mini[i] 
    return res



class chislo:
    #! Первоначальное создание объекта    
    def __init__(self, znach=None, osnov=None, accuracy=9) -> None: 
        #^ Желаемая точность вычислений дробной части
        self.accuracy = accuracy

        self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if (znach == None or osnov == None):
            znach = (input('Znach = ')).upper()
            osnov = int(input('Osnov = '))

            if osnov > 36:
                raise Exception('Основание привышает максимально допустимое')
            if self.osnov < 2:
                raise Exception('Основание меньше минимально допустимого')
            
            alph_slice = self.alphabet[0:osnov]
            alph_slice += '.'
            for item in znach:
                if item not in alph_slice:
                    raise Exception('Недопустимые символы для данного алфавита')

            if '.' in znach:
                self.znach, self.drob = znach.split('.')
            else:
                self.znach = znach
                self.drob = '0'
            
            self.osnov = sub_str(osnov).upper()
        else:       
            self.accuracy = accuracy             
            self.osnov_int = int(osnov)
            if self.osnov_int > 36:
                raise Exception('Основание привышает максимально допустимое')
            if self.osnov_int < 2:
                raise Exception('Основание меньше минимально допустимого')
            
            alph_slice = self.alphabet[0:self.osnov_int]
            alph_slice += '.'

            znach = str(znach).upper()
            for item in znach:
                if item not in alph_slice:
                    raise Exception(f'{item} - Недопустимые символы для данного алфавита. максимальный символ алфавита - {alph_slice[-2]}')
                
            self.osnov = sub_str(str(osnov)).upper()

            if '.' in str(znach):
                self.znach, self.drob = str(znach).split('.')
            else:
                self.znach = znach
                self.drob = '0'

            if len(self.drob) > self.accuracy:
                self.drob = self.drob[0:self.accuracy]

    #! Принудительно уменьшить или увеличить количество знаком после запятой
    def set_zero_drob(self, new_zero_count):
        if (self.drob != '0'):
            if self.accuracy > new_zero_count:
                self.drob = self.drob[0:new_zero_count]
            else:
                self.drob += '0' * (new_zero_count - len(self.drob))

    #! Перевод в строку
    def __str__(self) -> str:
        if self.drob == None:
            return f'{self.znach}.0{self.osnov}'
        else:
            return f'{self.znach}.{self.drob}{self.osnov}'
    
    #! Перевод в 10-тичную систему счисления
    def to10(self):
        new_znach = 0
        count = 0

        for item in reversed(self.znach):
            new_znach += int(self.alphabet.find(item))*(int(self.osnov_int)**count)
            count += 1
        
        if self.drob != '':
            count = -1
            for item in self.drob:
                new_znach += int(self.alphabet.find(item))*(int(self.osnov_int)**count)
                count -= 1

        new_osnov = 10
        return chislo(znach=new_znach, osnov=new_osnov, accuracy=self.accuracy)
    
    #! ПЕревод в Р-ричную систему счисления
    def toP(self, new_osnov:int):
        if self.osnov_int != 10:
            self = self.to10()
        
        new_znach = ''
        new_drob = ''
        lencount = 0

        old_znach = int(self.znach)
        old_drob = float('0.' + self.drob)
        
        while old_znach > 0:
            new_znach += self.alphabet[old_znach % new_osnov]
            old_znach //= new_osnov
        
        while lencount < self.accuracy:
            new_drob += self.alphabet[int(old_drob * new_osnov)]
            old_drob = (old_drob * new_osnov) % 1
            lencount += 1

        for item in reversed(new_drob):
            if item != '0':
                break
            else:
                new_drob = new_drob[0:new_drob.rindex('0')]

        if new_drob == '':
            new_drob = '0'
            
        new_znach = new_znach[::-1] + '.' + new_drob
        return chislo(znach=new_znach, osnov=new_osnov)

    #! Сложение Self и Other
    def __add__(self, other):
        # Если СС разные то к одной
        if self.osnov != other.osnov:
            other = other.toP(self.osnov_int)

        # Self должен быть больше чем Other иначе меняем
        if int(self.to10().znach) < int(other.to10().znach):
            self, other = other, self
        
        # Указатели на конец числа
        pointer1 = len(self.znach) - 1
        pointer2 = len(other.znach) - 1
        
        new_znach = ''
    
        # Незначащие нули в конце числа для одинакового кол-ва разрядов
        if len(self.drob) > len(other.drob):
            other.drob += '0' * (len(self.drob) - len(other.drob))
        elif len(self.drob) < len(other.drob):
            self.drob += '0' * (len(other.drob) - len(self.drob))

        pointer_drob1 = len(self.drob) - 1
        pointer_drob2 = len(other.drob) - 1

        new_drob = ''

        # Поразрядное суммирование 
        carry = 0
        while pointer_drob2 >= 0:
            summ = self.alphabet.find(self.drob[pointer_drob1]) + self.alphabet.find(other.drob[pointer_drob2]) + carry
            addition_bit = self.alphabet[summ % self.osnov_int]
            new_drob += str(addition_bit)
            carry = summ // self.osnov_int

            pointer_drob1 -= 1
            pointer_drob2 -= 1


        # Бежим с конца в перед пока не закончится меньшее число, 
        # в процессе складываем значения и пишем их по модулю
        # carry = 0
        while pointer2 >= 0:
            summ = self.alphabet.find(self.znach[pointer1]) + self.alphabet.find(other.znach[pointer2]) + carry
            addition_bit = self.alphabet[summ % self.osnov_int]
            new_znach += str(addition_bit)
            carry = summ // self.osnov_int

            pointer1 -= 1
            pointer2 -= 1

        # Добегаем остальные позиции в числе
        while pointer1 >= 0:
            summ = self.alphabet.find(self.znach[pointer1]) + carry
            addition_bit = self.alphabet[summ % self.osnov_int]
            new_znach += str(addition_bit)
            carry = summ // self.osnov_int

            pointer1 -= 1

        # Записываем в конец остаток суммы
        if carry != 0:
            new_znach += str(carry)

        # Переворачиваем результат
        new_znach = new_znach[::-1]
        new_drob = new_drob[::-1]

        return chislo(znach=f'{new_znach}.{new_drob}', osnov=self.osnov_int)

    #!Вычитание Other из Self
    def __sub__(self, other):
        if (int(f'{self.znach}', self.osnov_int)) + (int(f'{self.drob}', self.osnov_int) / (self.osnov_int ** len(self.drob))) < \
            (int(f'{other.znach}', other.osnov_int)) + (int(f'{other.drob}', other.osnov_int) / (other.osnov_int ** len(other.drob))):
            raise ValueError('В результате должно получиться отрицательно значение, такие вычисления не вохможно произвести')


        if self.osnov_int != other.osnov_int:
            other = other.toP(self.osnov_int)
        
        base = self.osnov_int
        num1 = self.znach
        num1_drob = self.drob

        num2 = other.znach
        num2_drob = other.drob

        while len(num1) < len(num2):
            num1 = '0' + num1
        while len(num2) < len(num1):
            num2 = '0' + num2

        while len(num1_drob) < len(num2_drob):
            num1_drob = num1_drob + '0'
        while len(num2_drob) < len(num1_drob):
            num2_drob = num2_drob + '0'

        borrow = 0
        result_drob = ""
        
        for i in range(len(num1_drob) - 1, -1, -1):
            digit1 = int(num1_drob[i], base)
            digit2 = int(num2_drob[i], base)

            # Учитываем заем
            digit1 -= borrow

            # Если digit1 < digit2, занимаем у следующего разряда
            if digit1 < digit2:
                digit1 += base
                borrow = 1
            else:
                borrow = 0

            # Вычисляем текущий разряд результата
            result_digit = digit1 - digit2
            result_drob = self.alphabet[result_digit] + result_drob

        # Удаляем ведущие нули
        result_drob = result_drob.rstrip('0')

        if len(result_drob) == 0:
            result_drob = '0'

        # Выполняем вычитание над целой частью
        result = ""
        for i in range(len(num1) - 1, -1, -1):
            digit1 = int(num1[i], base)
            digit2 = int(num2[i], base)

            # Учитываем заем
            digit1 -= borrow

            # Если digit1 < digit2, занимаем у следующего разряда
            if digit1 < digit2:
                digit1 += base
                borrow = 1
            else:
                borrow = 0

            # Вычисляем текущий разряд результата
            result_digit = digit1 - digit2
            result = self.alphabet[result_digit] + result

        # Удаляем ведущие нули
        result = result.lstrip('0')

        if len(result) == 0:
            result = '0'

        return chislo(znach=f'{result}.{result_drob}', osnov=base)

    #! Умножает Self на Other
    def __mul__(self, other):
        base = self.osnov_int
        
        a = f"{self.znach}.{self.drob}"
        b = f"{other.znach}.{other.drob}"

        result_in_base = ""
        carry = 0
        shift_dot = 0

        if '.' in a:
            a = f"{a.split('.')[0]}.{a.split('.')[1]}"
            if '.' in b:
                b = f"{b.split('.')[0]}.{b.split('.')[1]}"
                if len(a.split('.')[1]) < len(b.split('.')[1]):
                    a += '0' * (len(b.split('.')[1]) - len(a.split('.')[1]))
                else:
                    b += '0' * (len(a.split('.')[1]) - len(b.split('.')[1]))
            else:
                b += '.'
                b += '0' * len(a.split('.')[1])
        else:
            a += '.'
            if '.' in b:
                b = f"{b.split('.')[0]}.{b.split('.')[1]}"
                if len(a.split('.')[1]) < len(b.split('.')[1]):
                    a += '0' * (len(b.split('.')[1]) - len(a.split('.')[1]))
                else:
                    b += '0' * (len(a.split('.')[1]) - len(b.split('.')[1]))
            else:
                b += '.'
                b += '0' * len(a.split('.')[1])

        shift_dot += len(a.split('.')[1]) + len(b.split('.')[1])

        a = a.replace('.', '')
        b = b.replace('.', '')

        for i in range(len(a) + len(b)):
            result_digit = carry
            for j in range(len(a)):
                if i - j >= 0 and i - j < len(b):
                    result_digit += int(a[len(a) - 1 - j], base) * int(b[len(b) - 1 - (i - j)], base)
            
            carry = result_digit // base
            result_digit %= base

            result_in_base = str(self.alphabet[result_digit]) + result_in_base

        while len(result_in_base) > 1 and result_in_base[0] == "0":
            result_in_base = result_in_base[1:]

        res = (result_in_base[0:-shift_dot] + '.' + result_in_base[-shift_dot:]).rstrip('0')
        if res[0] == '.':
            res = '0' + res
        
        if res[-1] == '.':
            res += '0'
        return chislo(res, base, self.accuracy)
    
    #! self == other
    def __eq__(self, other):
        self = self.toP(self.osnov_int)
        other = other.toP(self.osnov_int)
        max_count = max(len(self.drob), len(other.drob))
        self.set_zero_drob(max_count)
        other.set_zero_drob(max_count)

        return ((self.znach == other.znach) and (self.drob == other.drob))

    #! self != other
    def __ne__(self, other):
        self = self.toP(self.osnov_int)
        other = other.toP(self.osnov_int)
        max_count = max(len(self.drob), len(other.drob))
        self.set_zero_drob(max_count)
        other.set_zero_drob(max_count)

        return ((self.znach != other.znach) or (self.drob != other.drob))

    #! self < other
    def __lt__(self, other):
        max_count = max(len(self.drob), len(other.drob))
        self.set_zero_drob(max_count)
        other.set_zero_drob(max_count)

        self = self.to10()
        other = other.to10()
        return (int(self.znach) < int(other.znach)) or \
                ((int(self.znach) == int(other.znach)) and (float('0.' + self.drob) < float('0.' + other.drob)))

    #! self <= other
    def __le__(self, other):
        max_count = max(len(self.drob), len(other.drob))
        self.set_zero_drob(max_count)
        other.set_zero_drob(max_count)

        self = self.to10()
        other = other.to10()
        return (int(self.znach) <= int(other.znach)) or \
                ((int(self.znach) == int(other.znach)) and (float('0.' + self.drob) <= float('0.' + other.drob)))

    #! self > other
    def __gt__(self, other):
        max_count = max(len(self.drob), len(other.drob))
        self.set_zero_drob(max_count)
        other.set_zero_drob(max_count)

        self = self.to10()
        other = other.to10()
        return (int(self.znach) > int(other.znach)) or \
                ((int(self.znach) == int(other.znach)) and (float('0.' + self.drob) > float('0.' + other.drob)))

    #! self >= other
    def __ge__(self, other):
        max_count = max(len(self.drob), len(other.drob))
        self.set_zero_drob(max_count)
        other.set_zero_drob(max_count)

        self = self.to10()
        other = other.to10()
        return (int(self.znach) >= int(other.znach)) or \
                ((int(self.znach) == int(other.znach)) and (float('0.' + self.drob) >= float('0.' + other.drob)))

    #! Self делится на Other по обычным правилам
    def __truediv__(self, other):
        if (self.osnov_int != other.osnov_int):
            other = other.toP(self.osnov_int)

        new_znach = ""
        new_drob = ""

        count_znach = 0
        while self > other:
            self = self - other
            count_znach += 1

        ten = chislo(10, self.osnov_int)
        count = 0
        max_acc = max(self.accuracy, other.accuracy)

        while count < max_acc:
            count_drob = 0
            self = self * ten
            while self > other:
                self = self - other
                count_drob += 1

            new_drob += self.alphabet[count_drob]
            count += 1

        if (new_drob == (self.alphabet[self.osnov_int-1] * max_acc)):
            count_znach += 1
            new_drob = "0"


        while count_znach > 0:
            new_znach = self.alphabet[count_znach % self.osnov_int] + new_znach
            count_znach //= self.osnov_int


        if (new_znach == ""):
            new_znach = "0"
        if (new_drob == ""):
            new_drob = "0"

        return chislo(f"{new_znach}.{new_drob}", self.osnov_int, max_acc)
    
    #! Целочисленное деление Self на Other
    def __floordiv__(self, other):
        if (self.osnov_int != other.osnov_int):
            other = other.toP(self.osnov_int)

        new_znach = ""
        new_drob = "0"

        count_znach = 0
        while self > other:
            self = self - other
            count_znach += 1

        max_acc = max(self.accuracy, other.accuracy)

        while count_znach > 0:
            new_znach = self.alphabet[count_znach % self.osnov_int] + new_znach
            count_znach //= self.osnov_int

        if (new_znach == ""):
            new_znach = "0"

        return chislo(f"{new_znach}.{new_drob}", self.osnov_int, max_acc)
    
    #! Остаток от деление Self на Other
    def __mod__(self, other):
        return self - other * (self // other)