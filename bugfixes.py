from random import *
#добавил a, b в скобки
def vahetus(a, b):
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n,loend,a,b):
    #добавил букву n в скобки и добавил один tab после 11 строчки и правильно написал loend.append
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend: list, p: list, n: list, nol: list):
    for el in loend:
        if el>0:
            p.append(el)  # исправил правильно append
        elif el<0:        #убрал лишнее двоеточие
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    #правильно поставил табы
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    #правильно написал функцию
    loend.append(el)
    loend.sort()

#создал списки которые не были defined
s = []
pos = []
neg = []
null = []
nol = []

#Põhifunktsioon
#правильно табы поставил
def arvud_loendis():
    print("Andmed:")
    n=abs(int(input("Mitu täisarvu genereerime loendisse? => ")))
    mini=int(input("Sisesta vahemiku minimaalne arv => "))
    maxi=int(input("Sisesta vahemiku maksimaalne arv => "))
    #убрал лишние двоеточия и поправил табы
    if mini>=maxi:
        mini, maxi = vahetus(mini, maxi)  # corrected to capture swapped values
    generaator(n,s,mini,maxi)  # исправлено generator на generaator
    print()
    print("Tulemused:")
    print("Saadud loend alates",mini,"kuni", s)
    s.sort()
    print("Sorteeritud loend", s)
    jagamine(s,pos,neg,nol)
    print("Positiivsete elementide loend",pos)
    print("Negatiivsete elementide loend",neg)
    print("Null-elementide loend",nol)
    kesk=keskmine(pos)  # only pass the list
    lisamine(s,kesk)
    print("Positiivsete keskmine:",kesk)
    kesk=keskmine(neg)  # only pass the list
    lisamine(s,kesk)
    print("Negatiivsete keskmine:",kesk)
    print("Lisame keskmised algsesse massiivi:")
    s.sort()
    print(s)

#Põhifunktsiooni käivitus
arvud_loendis()
