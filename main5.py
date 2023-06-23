wiek = 18
kasa = 35

if wiek >= 18:
    if kasa >= 35:
        print("1) 👍")

if wiek >= 18 and kasa >= 35:
    print("2) 👍")
# or = albo
# dzieci wchodza za darmo
# jesli jeden warunek jest spelniony to kod sie aktywuje
wiek2 = 0
kasa2 = 0
if wiek2 <= 12 or kasa2 >= 30:
    print("3) 👍")
else:
    print("3) 👎")

# operator not odwraca wartosc logiczna np z false na true

if not wiek > 12 or kasa >= 30:
    print("4) 👍")
else:
    print("4) 👎")

#
if True or False and False:
    print("Prawda")
else:
    print("Fałsz")