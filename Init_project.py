
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