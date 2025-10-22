print("Procvičování")
print("V uvozovkách zobrazí přesně to co do nich napíšeš")
print(123)
print("123") 
print("funguje s i bez uvozovek")
print(56.2)
print("Desetinná čísla se píšou s tečkou")
print("Spotřeba vozidla je:", 6.28)
print("Spotřeba vozidla je:",6.28,"L")

#Více řádků
print("Výška:\nVáha:\nPohlaví:")
#Skládání textů
print("Pes " + "potřebuje " + "péči") #odstup uvozovek na konci slova udělá mezeru
#Opakování textů pomocí násobení
print("Pes! "* 3)
#Celá čísla
print(35)
#Desetinná čísla
print(35.9)

#Logické hodnoty
print(True)
print(False)
#Seznamy
test_výsledky = [True, False, True]
print(test_výsledky)
#Slovníky
uživatel = {"Jméno": "Ondra", "Věk": 35}
print(uživatel)

#Proměnné pomocí symbolu =
počet_psů = '5'
plemeno = 'bulík'
zdraví = True

#Textové řetězce (string)
jméno = 'Ondra'
prodej = 'špatný'
počet_koberců = '7'

print(jméno)
print(prodej)
print(počet_koberců)
#Spojování řetězců
výsledek = "prodej, " + jméno + "!"
print(výsledek)
print("jméno "  * 3)
#Zjištění délky řetězce len
zpráva = "Ahoj, jak se máš!"
print(len(zpráva)) #počítá od 0 a počítá i mezery
#Přístup k jednotlivým znakům 0 je první -1 poslední
print(jméno[0])
print(jméno[-1])
#Zpracování - Velká malá písmena pomocí upper() a lower()
print(zpráva.upper())
print(zpráva.lower())
#Najít část řetězce pomocí find()
print(zpráva.find("máš!")) #najde koláté číslo ve slově máš!, Kterým začíná v tom pořadí
#Nahrazení textu pomocí replace()
print(zpráva.replace("máš!", "máte!")) #první slovo je nahrazeno tím druhým

print("Vaše jméno má " + str(len(jméno)) + " znaků.")

#Celá čísla int
teplota_plus = 25
teplota_mínus = '-5'
nulová_hodnota = '0'
print(teplota_plus)
print(teplota_mínus)
print(nulová_hodnota)
#Desetinná čísla float
pi = 3.14
míra_hladiny = -1.5
cena = 100.0
print(pi)
print(míra_hladiny)
print(cena)
#Počítání
print(25 + 30)
print(25*30)
print(25/30)
print(25//30)
print(10%3)
print(2**3)
a = 10
b = 4
print(a+b)
print(a**b)
#příklad rozdělení masa na osobu
váha_prasete = 110.0
pocet_lidi = 4
vaha_na_osobu = váha_prasete / pocet_lidi
print(f"Každý dostane: {vaha_na_osobu:.2f} kg masa")

#Uživatelský vstup
#input(), str(řetězec), type()
věk = input("Kolik je vám let? ")
print("Zadal jste: " + věk)
print("Typ zadaného vstupu je: " + str(type(věk)))

#Seznamy(list) seznamy pomocí []
cisla = [1, 2, 3, 4, 5]
slova = [ "red", "blue", "black"]
kombinace = [1, "yellow", True, 3,14]
print(cisla)
print(slova)
print(kombinace)
#Seznam cisla obsahuje pět čísel (každé číslo je datového typu int).
#Seznam slova obsahuje tři texty (řetězce), což jsou hodnoty datového typu str.
#Seznam kombinace ukazuje, že seznam může obsahovat různé datové typy včetně čísel, textů a logických hodnot.
print(slova[-1])
print(kombinace[2])
# index zadá pořadí slov v proměnné

#Změna seznamu
ovoce = ["jablko", "banán", "broskev"]
ovoce[-1] = "meruňka"
print(ovoce)
slova[-1] = "silver"
print(slova)
#Operace ovoce[1] = "pomeranč" změní druhý prvek seznamu (s indexem 1) z "broskev" na "meruňka".
#Tato vlastnost seznamů je velmi užitečná, například při aktualizaci hodnot v dynamických aplikacích.

#Operace se seznamy
#Na konec seznamu
ovoce.append("pomeranč") #append přidá novou položku na konec seznamu
print(ovoce)
ovoce.insert(1,"mango") #insert + index vloží data na určitou pozici
print(ovoce)

#Mazání dat
#podle hodnoty pomocí remove(hodnota)
ovoce.remove("mango")
print(ovoce)
#podle indexu pop(index)
ovoce.pop(1)
print(ovoce)

#Vyhledávání v seznamu
#Index(hodnota): Vrátí první výskyt hodnoty v seznamu. Pokud hodnota neexistuje, vyvolá chybu.
print(cisla.index(3))
#Count(hodnota): Vrátí, kolikrát se hodnota v seznamu vyskytuje.
print(cisla.count(3))

poradi = [2, 5, 3, 1]
#poradi.sort()
#print(poradi)
poradi.reverse()
print(poradi)

#Slovníky - zápis pomocí složených závorek. Každý klíč je oddělen : a jednotlivé páry ,
profil = {
    "jmeno": "Petr",
    "věk": 35,
    "role": "Tester"
}    
print(profil["jmeno"])
print(profil["věk"])
#Přidání a úprava hodnot
uživatel["pozice"] = "Tester"
print(uživatel)
#Mazání hodnot
del uživatel["Jméno"] #odstraní konkrétní hodnotu
#věk = uživatel.pop["Věk"] #pomocé pop()
#uživatel.clear() #vyprázdní slovník
#print(uživatel)

#Kontrola existence klíče pomocí in
uzivatel = {"jmeno": "Ondřej", "vek": 30}
print("jmeno" in uzivatel)
print("role" in uzivatel)