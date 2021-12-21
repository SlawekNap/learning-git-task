
print("Zadanie 1")
print("Lista zakupów")

słownik = {
    "Piekarnia": ["Chleb".upper(), "Pączek".upper(), "Bułki".upper()], 
    "Warzywniak": ["Marchew".upper(), "Seler".upper(), "Rukola".upper()]
    }
for sklep in słownik:
    print(f'Idę do {sklep.upper()}, kupuję tu następujące {słownik.get(sklep)}'),
Ilość_zakupów_w_sklepie = (len(słownik.get("Piekarnia")))+(len(słownik.get("Warzywniak")))
print(f"W sumie kupuję {Ilość_zakupów_w_sklepie} produktów.")

print("")
print("commit nr 1 na Git Hub")
for x in range(1,100):
    if x >= 80:
        print(x)
print("")
print("2 komit do zadnia")
list = {1:100}
for x in list:
    print(x)

