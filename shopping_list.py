#program do zarządzania listą zakupów

zakupy = {
    "piekarnia": ["chleb", "pączek", "bułki", "drożdzówki"],
    "warzywniak": ["marchew", "seler", "rukola","jabłka"]
}

suma_produktów = 0

for sklep, produkty in zakupy.items():
    sklep_formatted = sklep.title()
    produkty_formatted = [produkt.title() for produkt in produkty]
    print(f"Idę do {sklep_formatted}, kupuję tam {produkty_formatted}.")

    suma_produktów += len(produkty_formatted)

print(f"W sumie kupuję {suma_produktów} produktów.")
print("Robienie listy zakupów jest dobrym nawykiem")




