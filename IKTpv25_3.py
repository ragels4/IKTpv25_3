# Ex1
import random

P=random.randint(2,10)
print(f"Sõprade arv: {P}")

hind = 12.90
jootrahaga = 1.1 * hind
maksmus = jootrahaga/P
print(f"Iga sõber peab maksma: {maksmus:.2f} eurot")
print(f"Iga sõber peab maksma: {round(maksmus,2)} eurot")

print()

while True :
    try:
        a = int(input("Siseta A: "))
        break
    except:
        print("Palun siseta täisarv")

print()

while True :
    try:
        b = int(input("Siseta B: "))
        break
    except:
        print("Palun siseta täisarv")

    print()

while True :
    try:
        c = int(input("Siseta C: "))
        break
    except:
        print("Palun siseta täisarv")

print()


#Ex2

if a>0 and b>0 and c>0:
    print("Kõik küljed on positiivsed")
    
    if a+b>c and a+c>b and b+c>a:
        perimetr = a + b + c
        print(f"Kolmnurga ümbermoot on: {perimetr}")
    else:
        print("Ei, sellist kolmnurka ei saa olemas olla")
else:
    print("Arv positivsed")

#Moodle ex
#t_arvud = 0
#count = 0
#while True:                            
#    arv = input("Siseta arv: ")
#    try:
#        int_arv = int(arv)
#        print(f"{arv} on täisarv.")
#        t_arvud+=1
#    except ValueError:
#        print(f"{arv} ei ole täisarv")
#    count+=1
#
#    if count == 15: break
#print(f"{t_arvud} on täisarv.")


#MaksimVariant
#t_arvud = 0
#count = 0
#while count <= 15:                            
#    arv = input("Siseta arv: ")
#    try:
#        int_arv = int(arv)
#        print(f"{arv} on täisarv.")
#        t_arvud+=1
#    except ValueError:
#        print(f"{arv} ei ole täisarv")
#    count+=12
#print(f"{t_arvud} on täisarv.")

#summa = 0
#while True:
#    try:
#        a = int(input("Siseta arv: "))
#        if a > 0:
#            print("Arv on naturaalne")
#            break
#    except ValueError:
#        print("Arv ei ole naturaalne")
#
#for i in range (1,a + 1):
##  summa = i + summa
##   or
#    summa += i
#print(f"Summa on {summa}")

#ex5

import random
summa = 0

n = random.randint(2, 10)
for i in range(n):
    while True:
        try:
            arv = int(input("Sisesta suvaline arv"))
            break
        except:
            print("Palun sisesta korrektne arv!")
    if arv < 0:
        summa+=arv
print("Negatiivside arvude summa on:", summa)







