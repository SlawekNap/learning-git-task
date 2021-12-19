
print("Zadanie 1")
print("Lista zakupów")

słownik = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"], 
    "Warzywniak": ["Marchew", "Seler", "Rukola"]
    }
for sklep in słownik:
print(f'Idę do {sklep}, kupuję tu następujące {słownik.get(sklep)}'),