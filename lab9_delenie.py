def V_10(k,p):
    Numer=[i for i in range (0,10)]
    Alfa = [chr(i) for i in range (65, 91)]
    Alfavit=Numer+Alfa
    k1_p='' #целая часть pго числа
    k2_p='' #дробная часть pго числа
    i=0
    drob=0
    S=0
    f=0
    while i!=len(k):
        if k[i]==',' or k[i]=='.' or drob==1:
            if drob==0:
                drob=1
                i+=1
            else:
                k2_p+=k[i]
                i+=1   
        elif drob==0:
            k1_p+=k[i]
            i+=1
    n=len(k1_p)
    r=0
    for i in range(n-1,-1,-1):
        for j in range(0,36):
            if k1_p[i]==str(Alfavit[j]):
                f=j
        S+=f*p**r
        r+=1
    n=len(k2_p)
    i=0
    r=-1
    for i in range (0,n):
        for j in range(0,36):
            if k2_p[i]==str(Alfavit[j]):
                f=j
        S+=f*p**r
        r-=1
    return S


def Minus_p(a1,a2,p):
    Numer=[i for i in range (0,10)]
    Alfa = [chr(i) for i in range (65, 91)]
    Alfavit=Numer+Alfa
#Переводим числа в 10 сс для дальнейшего сравнения
    w1=V_10(a1,p)
    w2=V_10(a2,p)
#перевели
    modul1=''
    modul2=''
    modul1_d=''
    modul2_d=''
    i=0
    drob=0
    s=''
    znrez=''
    while i!=len(a1):
        if a1[i]==',' or a1[i]=='.' or drob==1:
            if drob==0:
                drob=1
                i+=1
            else:
                modul1_d+=a1[i]
                i+=1  
        elif drob==0:
            modul1+=a1[i]
            i+=1
    i=0
    drob=0
    while i!=len(a2):
        if a2[i]==',' or a2[i]=='.' or drob==1:
            if drob==0:
                drob=1
                i+=1
            else:
                modul2_d+=a2[i]
                i+=1  
        elif drob==0:
            modul2+=a2[i]
            i+=1
    if len(modul1_d)!=len(modul2_d):
        #уравниваем количество цифр
        n1=len(modul1_d)
        n2=len(modul2_d)
        r=abs(n1-n2)
        if n1>n2:
            for i in range(r):
                modul2_d+='0'
        else:
            for i in range(r):
                modul1_d+='0'
    n1=len(modul1_d)
    n2=len(modul2_d)
    zap=max(n1,n2)
    if len(modul1)!=len(modul2):
        n1=len(modul1)
        n2=len(modul2)
        r=abs(n1-n2)
        if n1>n2:
            for i in range(r):
                modul2='0'+modul2
        else:
            for i in range(r):
                modul1='0'+modul1
    maxi=''
    mini=''
    if w1>=w2:
        maxi+=modul1+modul1_d
        mini+=modul2+modul2_d
    if w1<w2:
        maxi+=modul2+modul2_d
        mini+=modul1+modul1_d
        znrez='-'
    n=len(maxi)
    nol=0
    zaim=0
    for i in range (n-1,-1,-1):
        if maxi[i]!='.':
            for j in range(0,36):
                if maxi[i]==str(Alfavit[j]):
                    sl1=j
                if mini[i]==str(Alfavit[j]):
                    sl2=j
        if maxi[i]=='.':
            s='.'+s
        elif sl1>sl2:
            s=str(Alfavit[sl1-sl2])+s
        elif sl1==sl2:
            s='0'+s
        elif sl1<sl2:
            if maxi[i-1]!='0':
                position=i-1
                sl1=p+sl1
                s=str(Alfavit[sl1-sl2])+s
                new=V_10(maxi[i-1],p)-1
                maxi=maxi[:position]+str(Alfavit[new])+maxi[position+1:]
            else:
                k=i-1
                sl1=p+sl1
                s=str(Alfavit[sl1-sl2])+s
                while maxi[k]=='0':
                    new=p-1
                    maxi=maxi[:k]+str(Alfavit[new])+maxi[k+1:]
                    k-=1
                for j in range(0,36):
                    if maxi[k]==str(Alfavit[j]):
                        zai=j
                zai-=1
                maxi=maxi[:k]+str(Alfavit[zai])+maxi[k+1:]
    n=len(s)
    if modul2_d!='' and modul1_d!='':
        s=s[:n-zap]+'.'+s[n-zap:]
    if s[0]=='0':
        s=s[1:]
    return s

def Del(a1,a2,p,n):
    Numer=[i for i in range (0,10)]
    Alfa = [chr(i) for i in range (65, 91)]
    Alfavit=Numer+Alfa
    k1_d='' #дробная часть1го числа
    k2_d='' #дробная часть 2го числа
    k1=''   #целая часть1го числа
    k2=''   #целая часть2го числа
    i=0
    drob=0
    s=''
    znak=n
    zap=0
    while i!=len(a1):
        if a1[i]==',' or a1[i]=='.' or drob==1:
            if a1[i]==',':
                a1=a1.replace(',','.',1)
                i+=1
            if drob==0:
                drob=1
                i+=1
            else:
                k1_d+=a1[i]
                i+=1  
        else:
            k1+=a1[i]
            i+=1
    i=0
    drob=0
    while i!=len(a2):
        if a2[i]==',' or a2[i]=='.' or drob==1:
            if a2[i]==',':
                a2=a2.replace(',','.',1)
                i+=1
            if drob==0:
                drob=1
                i+=1
            else:
                k2_d+=a2[i]
                i+=1
        else:
            k2+=a2[i]
            i+=1
    if k2_d!='':
        n1=len(k1_d)
        n2=len(k2_d)
    if k2_d!='':
        if n1>n2:
            k1=k1+k1_d[:n2]+'.'+k1_d[n2:]
            k2=k2+k2_d
        elif n1==n2:
            k1=k1+k1_d
            k2=k2+k2_d
        else:
            k2=k2+k2_d
            k1=k1+k1_d
            r=n2-n1
            d=0
            while d!=r:
                k1+='0'
                d+=1
    elif k1_d!='':
        k1=k1+'.'+k1_d
        k2=k2
    else:
        k1=k1+k1_d
        k2=k2+k2_d
    if len(k1_d)>len(k2_d):
        zap=abs(len(k1_d)-len(k2_d))
    k1=k1.replace('.','',1)
    f=1
    i=0
    dl=''
    men=0
    if V_10(k1,p)<V_10(k2,p):
        men=1
        k1+='0'
        s='0.'
    while f==1:
        dl=dl+k1[i]
        if V_10(dl,p)>=V_10(k2,p):
            f=0
        else:
            i+=1
    t=len(k1)-1
    #r1=0
    #r=0
    #while r1==0:
       # if k1[t]=='0':
            #r+=1
       # elif k1[t]!='0':
         #   r1=1
       # t-=1
    j=len(k1)-len(dl)+1
    t=k2[:]
    #print(k1,k2,dl,zap)
    h=0
    q=0
    #print(dl)
    q=int(input('Сколько чисел вывести в дробной части? '))
    while h!=j:
        h+=1
        i+=1
        kol=0
        while V_10(t,p)>=V_10(k2,p):
            t=Minus_p(dl,k2,p)
            dl=Minus_p(dl,k2,p)
            kol+=1
        if t!=0 and h<j:
            dl=str(t)+k1[i]
        elif t==0 and h<j:
            dl=k1[i]
        s+=str(Alfavit[kol])
        #print(s)
        prov=0
        while prov==0 and h<j-1:
            if V_10(dl,p)<V_10(k2,p):
                i+=1
                dl+=k1[i]
                s+='0'
                h+=1
            if V_10(dl,p)>=V_10(k2,p):
                prov=1
        t=str(dl)
    #if r!=0:
        #for i in range(r):
           #s+='0'
    #print(s)
    if zap!=0 and q!=0 and men==0:
        if len(s)>zap:
            s=s[:len(s)-zap]+'.'+s[len(s)-zap:]
        if len(s)<zap:
            k=0
            y=len(s)
            while k!=zap-y:
                s='0'+s
                k+=1
        if len(s)==zap:
                s='0.'+s
    if zap==0 and q!=0 and men==0:
        s=s+'.'
    #print(s)
    if q!=0 and zap<q:
        j=q-zap
        u=0
        dl=t+'0'
        t=dl[:]
        #print(dl)
        while u!=j:
            i+=1
            kol=0
            u+=1
            while V_10(t,p)>=V_10(k2,p):
                t=Minus_p(dl,k2,p)
                dl=Minus_p(dl,k2,p)
                kol+=1
            #print(kol)
            s+=str(Alfavit[kol])
            dl+='0'
            prov=0
            while prov==0 and u<j:
                if V_10(dl,p)<V_10(k2,p):
                    i+=1
                    dl+='0'
                    s+='0'
                    u+=1
                if V_10(dl,p)>=V_10(k2,p):
                    prov=1
            t=str(dl)
    elif q!=0 and zap>=q:
        s=s[:len(s)-(zap-q)]
    if n==1:
        print('-',s)
    elif q==0 and t!=0 and t!='':
        print(s,' ост (', t,')')
    else:
        print(s)
    
      
        
Numer=[i for i in range (0,10)]
Alfa = [chr(i) for i in range (65, 91)]
Alfavit=Numer+Alfa    
a1=str(input('Введите делимое: '))
a2=str(input('Введите делитель: '))
if a2=='0':
    a2=str(input('На 0 не делим, Введите делитель: '))
p=str(input('В какой сс производить деление? '))
f=1
while f==1:
    try:
        int(p)
        if (int(p)>=2 and int(p)<=36):
            f=0
        else:
            p=p+'*'
    except ValueError:
        print('Неверно введено основание сс')
        p=input('Введите основание сс еще раз')
p=int(p)
n=0 #оба числа положительные
if a1[0]=='-' and a2[0]=='-':
    n=2 #оба числа отрицательные
    a1=a1.replace('-','',1)
    a2=a2.replace ('-','',1)
if a1[0]=='-' and a2[0]!='-' or a2[0]=='-' and a1[0]!='-':
    n=1 #одно из чисел отрицательное
    a1=a1.replace('-','',1)
    a2=a2.replace ('-','',1)
z=0
count1=0
for i in range(len(a1)):
    for j in range(0,36):
        if a1[i]==str(Alfavit[j]):
            d=j
    if d<p:
        count1+=1
    elif a1[i]=='.':
        count1+=1
count2=0
for i in range(len(a2)):
    for j in range(0,36):
        if a2[i]==str(Alfavit[j]):
            d=j
    if d<p:
        count2+=1
    elif a2[i]=='.':
        count2+=1
if count1!=len(a1) or count2!=len(a2):
    print('Введено число, которое не содержится в данной системе счисления!')
    z=1
if z==0:
    Del(a1,a2,p,n)


