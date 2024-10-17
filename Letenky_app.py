# Aplikace na letenky 

city = { 

    "Londýn": 1000, 
    "Berlín": 500, 
    "Řím": 1200, 
    "Madrid": 1500, 
    "Budapešť:": 900 

} 

line = 35 * "=" 
offers = """ 
Londýn     |   1000,-Kč 
Berlín     |   500,-Kč 
Řím        |   1200,-Kč 
Madrid     |   1500,-Kč 
Budapešť   |   900,-Kč 
""" 

# print("VÍTEJTE V APLIKACI EVROPA LETENKY! 'ODLET PRAHA'") 
# print (line, offers, end='') 
# print(line) 
print(" 'OSOBNÍ ÚDAJE' ")
destinace = input("VYBERTE CÍLOVÉ MĚSTO: "). lower()
people = int(input("POČET DOSPĚLÝCH: "))
children = int(input("POČET DĚTÍ DO 10 LET: "))
luggage = int(input("POČET ZAVAZADEL DO 15KG: "))
# NAD 15 KG PŘÍPLATEK 200KČ
# print(f"Vaše cílové město: {destinace}\nPočet dospělých osob: {people}\nPočet dětí: {children}\nPočet zavazadel do 15KG: {luggage}")