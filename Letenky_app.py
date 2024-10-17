# Aplikace na letenky 
city = { "Londýn": 1000, "Berlín": 500, "Řím": 1200, "Madrid": 1500, "Budapešť": 900 } 

line = 35 * "_" 
double_line = 35 * "="
offers = """ 
(VÍTEJTE V APLIKACI EVROPA LETENKY!
***ODLET POUZE Z PRAHY***
-----------------------------------
          "DESTINACE"
1 - Londýn    |   1000,-Kč 
2 - Berlín    |   500,-Kč 
3 - Řím       |   1200,-Kč 
4 - Madrid    |   1500,-Kč 
5 - Budapešť  |   900,-Kč 
-----------------------------------
"SLEVA NA LETENKY"
DĚTI DO 10 LET - 50%
-----------------------------------
"CENA ZAVAZADEL"
DO 15KG CENA: 100,-Kč
NAD 15KG CENA: 200,-KČ
***MOŽNOST POUZE JEDNO ZAVAZADLO NA OSOBU NEBO DÍTĚ***  
"""
# print (double_line, offers, end='') 
# print(double_line) 

print("'INFORMACE'")

destinace_num = int(input("VYBERTE ČÍSLO DESTINACE: "))
destinace = list(city.keys())[destinace_num - 1]  # Výběr destinace podle čísla

children = int(input("POČET DĚTÍ DO 10 LET: "))
adult = int(input("POČET OSOB: "))
ticket_price = city[destinace] * adult

weights_input = input("ZADEJTE VÁHY ZAVAZADEL ODDĚLENO ČÁRKOU (např. 16.5, 17): ")

# Rozdělení vstupu na jednotlivé váhy podle čárky a převod na seznam čísel (float)
weights_list = [float(weight.strip()) for weight in weights_input.split(',')]

#  Výpočet ceny zavazadel podle váhy
luggage_prices = []
for weight in weights_list:
    if weight <= 15:
        luggage_prices.append(100)
    else:
        luggage_prices.append(200)

# KONTROLA VÝPOČTU FINÁLNÍ CENY BEZ DĚTÍ
# total_price = (city[destinace] * adult) + sum(luggage_prices)
# print("Celková cena:", total_price)

# SLEVA DÍTĚ
discount = 0
if children > 0:
    discount = 0.5 * city[destinace] * children

# CELKOVÁ CENA SE ZAVAZADLY A DĚTMI
total_price = (ticket_price - discount) + sum(luggage_prices)
print(total_price)