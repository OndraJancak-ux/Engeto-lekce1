import math, datetime, random
#Boolean
# True and False
pravda = True
nepravda = False
print(pravda)

print(bool(0))
print(bool(123))
print(bool(""))

#Seznam porovnávacích operátorů
#Rovnost
print(10 == 10)
print(5 == 10)
#Nerovnost
print(10!=10)
print(10 != 5)
#Menší<než - Větší než>
print(5 < 10)
print(5 > 10)
#Menší nebo rovno <= a Větší nebo rovno>=
print(5 <= 5)
print(4 <= 5)
print(10>=10)

#Příklad
vek = int(input("Zadejte svůj věk: "))
je_plnoletý = vek >= 18
print("Je Vám alespoň 18 let:", je_plnoletý)

#Příklad 2
heslo = "tajneheslo"
#zadané_heslo = input("Zadejte své heslo: ")
#print("Vaše heslo je: ", heslo)
#print("Heslo je správné: ", zadané_heslo == heslo)

#Příklad 3
cislo = int(input("Zadejte číslo: "))
je_ve_stupnici = cislo >0 and cislo <100
print("Čislo je mezi 0 a 100:", je_ve_stupnici)

#Cyklus pomocí for - položka in sekvence
#Položka – proměnná, která při každé iteraci obsahuje hodnotu aktuálního prvku sekvence.
#sekvence – kolekce dat, které chceme iterovat, například seznam (list) nebo rozsah čísel (range).
test_cases = ["Přihlášení", "Registrace", "Zapomenuté heslo"]

for case in test_cases:
    print(f"Spouštím testovací scénář: {case}")
#Přes rozsah čísel range
for i in range(5):
    print(f"Spouštím testovací scénář:{i + 1}")

#Iterace přes řetězec
text = "Test"
for char in text:
    print(f"Znak: {char}")

#While cyklus
#cislo = 0

#while cislo <5:
    #print(f"Iterace číslo: {cislo + 1}")
    #cislo += 1


#Čekání na načtení stránky
nacitani = True
cas = 0

while nacitani and cas <4:
    print("Načítání stránky...")
    cas += 1
    nacitani = cas != 5

print("Test dokončen: stránka načtena" if not nacitani else "Test selhal: stránka se nenačetla včas.")

#Hledání první chyby v testovacích výsledcích
testovací_výsledky = ["PASS", "PASS", "FALS", "PASS"]
index = 0

while index < len(testovací_výsledky) and testovací_výsledky[index] != "FAIL":
    index += 1

print(f"Chyba nalezena v testu č.{index + 1}." if index < len(testovací_výsledky) else "Všechny testy prošly")    

#Opakované zadávání hesla
spravne_heslo = "tajneheslo"
uzivatel_input = input("Zadejte své heslo: ")

while uzivatel_input != spravne_heslo:
    print("Nesprávné heslo, zkuste to znovu.")
    uzivatel_input = input("Zadejte heslo: ")

print("Přihlášení úspěšné.")    

#Podmínky
# if, elif, else
#if podmínka:
    # Kód, který se vykoná, pokud je podmínka pravdivá
#elif jiná_podmínka:
    # Kód, který se vykoná, pokud je splněna jiná podmínka
#else:
    # Kód, který se vykoná, pokud žádná podmínka není splněna
number = 5
if number > 0:
    print("Čislo je kladné")

elif number < 0:
    print("Číslo je záporné") 

else:
    print("Číslo je nulové")    

# Logické operátory v podmínkách
# and  Podmínka je pravdivá, pokud jsou pravdivé všechny části.
# or     Podmínka je pravdivá, pokud je pravdivá alespoň jedna část.
# not    Otočí pravdivost podmínky (např. z True na False)

age = 17
ma_opravněni = True
if age >= 18 and ma_opravněni:
    print("Vstup povolen")
else:
    print("Vstup zakázán")    


#Ověření výsledků
skutecny_vysledek = 10
aktualni_vysledek = 5

if aktualni_vysledek == skutecny_vysledek:
    print("Test prošel.")

else:
    print("Test neprošel")   

#Rozlišení tyou testu
if aktualni_vysledek < 10:
    print("Test selhal: Výsledek je nizky")
elif aktualni_vysledek > 10:
    print("Test selhal: Výsledek je vysoky")
else:
    print("Test prošel")        

#Funkce
#Funkce je blok kódu, který provádí určitou činnost. Může přijímat vstupní hodnoty (parametry) a 
# vracet výstupní hodnotu.
# pomocí def
#Návratová hodnota: Pomocí return funkce vrací výsledek. Pokud není return uvedeno, 
# funkce vrací hodnotu None
def pozdrav():
    print("Ahoj, vítej")

pozdrav()    

#Vestavěné funkce
#len(): Vrací délku objektu (např. řetězce nebo seznamu).
#max(): Vrací největší hodnotu ze zadaných argumentů.
#round(): Zaokrouhluje číslo na zadaný počet desetinných míst.
#print(): Slouží k výpisu hodnot do výstupního zařízení (obvykle konzole)

print(len("Python"))
print(max(2, 8, 5))
print(round(3.14159, 2))

#Vlastní funkce
def scitani(a, b):
    return a + b
vysledek = scitani(3, 5)
print(vysledek)

#Parametry
def pozdrav_jmenem(jmeno):
    print(f"Ahoj, {jmeno}!")

pozdrav_jmenem("Ondra")

#Moduly math
#odmocnina


print(math.sqrt(16))
print(math.pi)

#Modul dateline
now = datetime.datetime.now()
print(now)

#Modul random
print(random.randint(1, 10))
print(random.choice(['jablko', 'Hruška', 'Banán']))