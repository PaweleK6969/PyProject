print("Kolejnosc:" + " ")
# Dzialanie zgodnie z prawami matematyki
print(2 + 2 * 2)
# Dzialanie nie zgodne z prawami matematyki
print((2 + 2) * 2)

print("Dzielenie:" + " ")
# liczba + liczba po przecinku
print(5 / 2)
# Liczba calkowita bez liczby po przecinku
print(5 // 2)

print("Mnożenie:" + " ")
# Normalne mnozenie
print(2 * 3)
# Potegowanie
print(2 ** 3)

print("Skrocone: ")
# Zmienne (zwiekszenie o 1)
x = 5
x = x + 1
print(x)
# krotszy zapis
x += 1
print(x)

print("Konwersja:")
a = input("Podaj 1 liczbe: ")
b = input("Podaj 2 liczbe: ")
print(int(a) + int(b))
# Jesli chcemy dodawac liczby przecinkowe np 5.5 to zmieniamy int na float
print(" ")
# odwrotnosc
y = 2
z = 2
print(str(y) + str(z))
print(str(y) + str(z))
# jesli nie potrzebujemy juz zmiennej to uzywamy polecenia "del (zmienna)" np. (del y)
# pamietaj ze po uzyciu polecenia del zmienna nie bedzie istniec, jesli bedziesz chcial ja wywolac wyskoczy blad
