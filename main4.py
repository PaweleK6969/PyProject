# True/False TYP LOGICZNY NIE MOZNA ZMIENIAC NA INNE TYLKO TRUE/FALSE
# W Pythonie musi byc pierwsza duza litera np True.
x = True
y = False
# Czy są sobie rowne?
print(5 == 5)
# Czy są rózne?
print(5 != 1)
#Czy x jest wiekszy od x?
print(5 > 5)
# Czy x jest mniejszy od x?
print(5 < 5)
# Mniejsze lub rowne
print(8 <= 9)
# Wiekszy lub rowny
print(8 >= 9)

# Instrukcje warunkowe IF

print(" ")
print("IF")
print(" ")
# Wszystko co pod if w tabulatorze nalezy do tej funkcji
# Jezeli jest prawda to kod sie wykona, jesli nie to nic pod ifem nie wykona sie
if 5 > 5:
    print("Większe")
if 5 <= 10:
    print("Mniejsze")
if 5 > 10:
    print("True")
else:
    print("False")
