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

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class chislo:    
    def __init__(self, znach=None, osnov=None, accuracy=9) -> None: 
        #^ Желаемая точность вычислений дробной части
        self.accuracy = accuracy

        if (znach == None or osnov == None):
            znach = (input('Znach = ')).upper()
            osnov = int(input('Osnov = '))

            if osnov > 36:
                raise Exception('Основание привышает максимально допустимое')
            if self.osnov < 2:
                raise Exception('Основание меньше минимально допустимого')
            
            alph_slice = alphabet[0:osnov]
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
            
            alph_slice = alphabet[0:self.osnov_int]
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

    #^ Перевод в строку
    def __str__(self) -> str:
        if self.drob == None:
            return f'{self.znach}.0{self.osnov}'
        else:
            return f'{self.znach}.{self.drob}{self.osnov}'
    
    def to10(self):
        new_znach = 0
        count = 0

        for item in reversed(self.znach):
            new_znach += int(alphabet.find(item))*(int(self.osnov_int)**count)
            count += 1
        
        if self.drob != '':
            count = -1
            for item in self.drob:
                new_znach += int(alphabet.find(item))*(int(self.osnov_int)**count)
                count -= 1

        new_osnov = 10
        return chislo(znach=new_znach, osnov=new_osnov, accuracy=self.accuracy)
    
    def toP(self, new_osnov:int):
        if self.osnov_int != 10:
            self = self.to10()
        
        new_znach = ''
        new_drob = ''
        lencount = 0

        old_znach = int(self.znach)
        old_drob = float('0.' + self.drob)
        
        while old_znach > 0:
            new_znach += alphabet[old_znach % new_osnov]
            old_znach //= new_osnov
        
        while lencount < self.accuracy:
            new_drob += alphabet[int(old_drob * new_osnov)]
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

    # Сложение Self и Other
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
            summ = alphabet.find(self.drob[pointer_drob1]) + alphabet.find(other.drob[pointer_drob2]) + carry
            addition_bit = alphabet[summ % self.osnov_int]
            new_drob += str(addition_bit)
            carry = summ // self.osnov_int

            pointer_drob1 -= 1
            pointer_drob2 -= 1


        # Бежим с конца в перед пока не закончится меньшее число, 
        # в процессе складываем значения и пишем их по модулю
        # carry = 0
        while pointer2 >= 0:
            summ = alphabet.find(self.znach[pointer1]) + alphabet.find(other.znach[pointer2]) + carry
            addition_bit = alphabet[summ % self.osnov_int]
            new_znach += str(addition_bit)
            carry = summ // self.osnov_int

            pointer1 -= 1
            pointer2 -= 1

        # Добегаем остальные позиции в числе
        while pointer1 >= 0:
            summ = alphabet.find(self.znach[pointer1]) + carry
            addition_bit = alphabet[summ % self.osnov_int]
            new_znach += str(addition_bit)
            carry = summ // self.osnov_int

            pointer1 -= 1

        # Записываем в конец остаток суммы
        if carry != 0:
            new_znach += str(carry)

        # Переворачиваем результат
        new_znach = new_znach[::-1]
        new_drob = new_drob[::-1]

        return chislo(znach=new_znach + '.' + new_drob, osnov=self.osnov_int)


    #Вычитание Other из Self
    def __sub__(self, other):
        print('MIN')
        pass

    #! Пока только целое
    def __mul__(self, other):
        osnov = self.osnov_int
        self = self.to10()
        other = other.to10()

        return chislo(str(float(self.znach + '.' + self.drob) * float(other.znach + '.' + other.drob)), '10').toP(osnov)