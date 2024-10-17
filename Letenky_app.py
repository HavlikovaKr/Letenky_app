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


weights_input = input("ZADEJTE VÁHY ZAVAZADEL ODDĚLENO ČÁRKOU (např. 16.5, 17): ")

