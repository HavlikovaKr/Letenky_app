# Aplikace na letenky 
city = { "Londýn": 1000, "Berlín": 500, "Řím": 1200, "Madrid": 1500, "Budapešť": 900 } 
city["Riga"] = 600

line = 35 * "_" 
double_line = 35 * "="
offers = """ 
(VÍTEJTE V APLIKACI EVROPA LETENKY!
***ODLET POUZE Z PRAHY***
-----------------------------------
          "DESTINACE"
1 - Londýn    |   1000,-Kč 
2 - Berlín    |   500,- Kč 
3 - Řím       |   1200,-Kč 
4 - Madrid    |   1500,-Kč 
5 - Budapešť  |   900,- Kč 
6 - Riga      |   700,- Kč
-----------------------------------
"SLEVA NA LETENKY"
DĚTI DO 10 LET - 50%
-----------------------------------
"CENA ZAVAZADEL"
DO 15KG CENA: 100,- Kč
NAD 15KG CENA: 200,-KČ
***MOŽNOST POUZE JEDNO ZAVAZADLO NA OSOBU NEBO DÍTĚ***  
"""
print (double_line, offers, end='') 
print(double_line) 

print("'VYPLNĚNÍ FORMULÁŘE'")

destinace_num = int(input("VYBERTE ČÍSLO DESTINACE: "))
destinace = list(city.keys())[destinace_num - 1]  # Výběr destinace podle čísla

children = int(input("POČET DĚTÍ DO 10 LET: "))
adult = int(input("POČET DALŠÍCH OSOB: "))

# Kontrola, zda počet zavazadel odpovídá počtu osob a dětí
while True:
    weights_input = input("ZADEJTE VÁHY ZAVAZADEL ODDĚLENO ČÁRKOU (např. 16.5, 17): ")
    
    # Rozdělení vstupu na jednotlivé váhy podle čárky a převod na seznam čísel (float)
    weights_list = [float(weight.strip()) for weight in weights_input.split(',')]

    if len(weights_list) > (adult + children):
        print("Počet zavazadel je větší než počet osob a dětí dohromady! Zadejte znovu.")
    else:
        break  # Pokud je počet zavazadel v pořádku, ukončíme cyklus

# Výpočet ceny zavazadel podle váhy
luggage_prices = []
for weight in weights_list:
    if weight <= 15:
        luggage_prices.append(100)
    else:
        luggage_prices.append(200)
    

# KONTROLA VÝPOČTU FINÁLNÍ CENY BEZ DĚTÍ
# total_price = (city[destinace] * adult) + sum(luggage_prices)
# print("Celková cena:", total_price)

# Výpočet ceny letenek
ticket_price_adult = city[destinace] * adult  # Cena pro dospělé
ticket_price_children = 0.5 * city[destinace] * children  # 50% sleva na dětské letenky

# Výpočet celkové ceny
total_price = ticket_price_adult + ticket_price_children + sum(luggage_prices)


print(double_line)
print("     ***LETENKA*** ")
print(double_line)
print(f"DESTINACE: {destinace}")
print(f"POČET DOSPĚLÝCH: {adult}")
print(f"POČET DĚTÍ DO 10 LET: {children}")
print(f"CENA ZAVAZADEL: {', '.join(map(str, luggage_prices))} Kč")
print(double_line)
print(f"CELKOVÁ CENA: {total_price:.2f} Kč")
print(double_line)

