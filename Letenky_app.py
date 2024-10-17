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
DĚTI DO 10 LET - 50% sleva
-----------------------------------
"CENA ZAVAZADEL NA LETENKU"
DO 20KG CENA: 200,- Kč
NAD 20KG CENA: 300,-KČ  
"""
print (double_line, offers, end='') 
print(double_line) 

print("'VYPLNĚNÍ FORMULÁŘE'")

# Ošetření špatného formátu
while True:
    try:
        destinace_num = int(input("VYBERTE ČÍSLO DESTINACE: "))
        destinace = list(city.keys())[destinace_num - 1]  # Výběr destinace podle čísla
        break 
    except (ValueError, IndexError):
        print("Špatný formát nebo číslo destinace. Vyplňte znovu.")

while True:
    try:
        adult = int(input("POČET DOSPĚLÝCH: "))
        break
    except ValueError:
        print("Špatný formát. Vyplňte znovu číslo dospělých.")

while True:
    try:
        children = int(input("POČET DĚTÍ DO 10 LET: "))
        break
    except ValueError:
        print("Špatný formát. Vyplňte znovu počet dětí.")

while True:
    try:
        weights = float(input("ZADEJTE VÁHU ZAVAZADEL DOHROMADY v Kg: "))
        break
    except ValueError:
        print("Špatný formát. Zadejte znovu váhu zavazadel jako číslo.")

# Zavazadla
if weights <= 20:
    total_luggage = 200
else:
    weights > 20
    total_luggage = 300

# Cena za dospělé
ticket_price = city[destinace] * adult

# Sleva pro děti 50% a cena bez dětí
if children > 0:
    discount = 0.5 * city[destinace] * children
    ticket_price = ticket_price + discount 
else:
    # Pokud nejsou děti, cena je jen za dospělé
    ticket_price = city[destinace] * adult

# Celková cena (letenky + zavazadla)
price = ticket_price + total_luggage

print(double_line)
print("     *** LETENKA *** ")
print(double_line)
print(f"DESTINACE: {destinace}")
print(f"POČET DOSPĚLÝCH: {adult}")
print(f"POČET DĚTÍ DO 10 LET: {children}")
print(f"CENA ZAVAZADEL: {total_luggage} Kč")
print(double_line)
print(f"CELKOVÁ CENA: {price:.2f} Kč")
print(double_line)

