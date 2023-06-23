# Pętle

# i to zmienna potrzebna do petli zeby nie byly nieskonczone

i = 0

while i < 5:   # 5 = ilosc loopa
    print(i)
    i += 1     # bez tego pentla bedzie nieskonczona

# inny sposob
 # Przerwanie pentli

while True:
    print(i)
    i += 1
    if i <= 5:     # 5 = ilosc loopa
        break

# Wyswietlanie tylko pazystych liczb
# continue = pomija 

while True:
    i += 1:
    if i % 2 == 1:
        continue
    print(i)
    if i > 10:
        break