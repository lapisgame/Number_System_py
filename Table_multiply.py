from ChisloLib import chislo

p = 16
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print('', end='\t')
for i in range(p):
    x = chislo(alphabet[i], str(p))
    print(x, end='\t')
print()
print((8 * '-') * (p + 1))

for i in range(p):
    x = chislo(alphabet[i], str(p))
    print(x,'|', end='\t')
    for j in range(p):
        y = chislo(alphabet[j], str(p))
        print(x*y, end='\t')

    print()