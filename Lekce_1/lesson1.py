# funkce
print("ahoj")
print("40 000")
print("Pozor náledí")
print("Výsledek je:",100)

print("První řádek\nDruhý řádek\nTřetí řádek")
print("Spotřeba vozidla je:", 6.28)
# datový typ bool
print(True)
# datový typ seznam
akciové_zboží = {"káva","Meloun","banány"}
print(akciové_zboží)

#datový typ slovník
uživatel = {
    "jméno": "Honza",
    "věk": "28"
}
print(uživatel)

#Proměnné
věk_uživatele = 17
print(věk_uživatele)
věk_uživatele = 18
print(věk_uživatele)
věk_uživatele = 25
print(věk_uživatele)

uživatelské_jméno = "Viktor007"
spotřeba_jízda = 6.3
je_pojištěn_CZ = False

#Funkce pro retezce
#pokud ma sms > 100 -> 2SMS uctujeme
SMS = "Dobrou  noc"
print (len(SMS))

#Jaký znak je první v SMS?
print(SMS[0])
print(SMS[-1])

#Další funkce - lowerCase
user_name = "StEeeFAn007"
print(user_name. lower())

print(11//5) #celé dělení
print(11/5)
print(11%5)#zbytek po dělení
print(2**80)#mocnění
print(2+80)#spoučet čísel

#Uživatelský vstup
#funkce input()

print("Vítejte\nKolik je Vám let?")
věk_návštěvníka_hospody = input()
print("Váš věk je:" + věk_návštěvníka_hospody)

#Funkce pro seznam datový typ
#Došly nám banány, musíme tento produkt stáhnout z prodeje
akciové_zboží.remove("banány")
print(akciové_zboží)

#přidat nové zboží, cukr
akciové_zboží.add("cukr")
print(akciové_zboží) # zkusit opravit append

#které je zboží na prvním místě našeho letáku
#print(akciové_zboží[0]) #kontrola

#Funkce pro datový typ slovník
print(uživatel["jméno"])
uživatel["je_pojištěn_EU"] = True
print(uživatel)
