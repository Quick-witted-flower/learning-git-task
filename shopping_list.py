#program do zarządzania listą zakupów

zakupy = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for sklep, produkty in zakupy.items():
    sklep_formatted = sklep.title()
    produkty_formatted = [produkt.title() for produkt in produkty]
    print(f"Idę do {sklep_formatted}, kupuję tam {produkty_formatted}.")


    