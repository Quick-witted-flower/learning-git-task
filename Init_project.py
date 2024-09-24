zakupy = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
suma_produktow = 0

for sklep, produkty in zakupy.items():
    
    sklep_formatted = sklep.title()
    produkty_formatted = [produkt.title() for produkt in produkty]
    

    print(f"Idę do {sklep_formatted}, kupuję tam {produkty_formatted}.")

    suma_produktow += len(produkty)

print(f"W sumie kupuję {suma_produktow} produktów.")  




    

    