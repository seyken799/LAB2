#zad1
lista_filmow = ['Harry Potter', 'LOTR', 'PZK', 'GOL','Nietykalni','Spider man','Kevin sam w domu','Bracia Grimsby']
print(lista_filmow)
lista_filmow.reverse()
print(lista_filmow)
lista_filmow.insert(5, "Wikingowie")
lista_filmow.insert(5, "SUITS")
print(lista_filmow)

#zad2
slownik_filmow = {'tytul': lista_filmow}
print(slownik_filmow)

#zad3
przedmioty = {"WD": "Wizualizacja danych","MD":"Matematyka Dyskretna", "AMDI":"Analiza matematyczna dla informatykow","JA": "Jezyk angielski","PS":"Programowanie strukturalne",
              "WOT":"Wiedza o teatrze", "CAD":"CAD komputerowe wspomaganie projektowania"}
print(przedmioty)
print(len(przedmioty))

#zad4
liczba =input("Podaj liczbe: ")
liczba = int(liczba)
print(liczba * liczba)

#zad5
import sys as system

system.stdout.write("Wpisz dowolny ciąg znaków: ")
ciag = system.stdin.readline()
print(ciag.count("a"))

#zad6
a = input("Wprowadz liczbe a: ")
b = input("Wprowadz liczbe b: ")
c = input("Wprowadz liczbe c: ")
a = int(a)
b = int(b)
c = int(c)
if (a % 2 == 0) & (b > c):
    print("prawda")
else:
    print("falsz")

#zad7
lista = [3, 5, 9, 2, 2.1, 3.6, 1.9, 4.4]
for i in

#zad8
lista2 = []
i = 0
while i < 10:
    i += 1
    liczby = int(input("Podaj liczbe: "))
    if liczby % 2 == 0:
        lista2.append(liczby)
print(lista2)

#zad9
lista4 = [1, 2, 3, 4, 5, 6]
i = 1
for i in range(6):
    if lista4[i] % 5 == 1:
        print("000000")
    else:
        print("O    O")



#zad10

licz = input("Podaj liczbe: ")
try:
    licz = float(licz)
    print("Twoja liczba to: ", licz)
except:
    print("Blad, podales litere")



