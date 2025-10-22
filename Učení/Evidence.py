#Evidence uživatelů
uzivatel = {
    "jmeno": "Ondřej", 
    "vek": 35, 
    "role": "tester"
    }
print ("Jméno:", uzivatel["jmeno"])
print("Věk:", uzivatel["vek"])

uzivatel.get("telefon", "Není zadáno")
print("Telefon:", uzivatel.get("telefon", "Není zadáno"))#neexistující klíč

uzivatel["telefon"] = "733542667" #přidání nového záznamu
print("Telefon:", uzivatel.get("telefon", "Není zadáno"))


# Využití slovníků v testování
#Ukládání test. dat
test_data = { 
    "scénář_1": {"vstup": "abc", "očekávaný_výstup": "ABC"}
    #"scénář_2": {"vstup": "123" "očekávaný_výstup": "123"}
}
print(test_data["scénář_1"]["očekávaný_výstup"])

#Porovnání očekávaných a skutečných výsledků
ocekavane = {"status": 200, "data": "OK"}
skutecne = {"status": 100, "data": "OK"}

print(ocekavane == skutecne)

#Sledování stavů během testování
vysledky = {}
vysledky["test_1"] = "Prošel"
vysledky["test_2"] = "Selhal"
print(vysledky)

#Vytváření dynamických parametrů pro API Testy
headers = {"Content-Type": "application/json", "Authorization": "Bearer"}
data = {"username": "tester", "password": "12345"}

#Cvičení
## Uživatelský vstup uložený v proměnné jmeno
jmeno = input("Zadejte své jméno: ")

#Výpis zprávy do konzole
print("Ahoj, " + jmeno + "! Vítej v našem programu.")

počet_znaků = len(jmeno)
print("Vaše jméno má: " + str(počet_znaků) + " znaků")

text = input("Dnes je venku hezky")
pocet_slov = len(text.split())
print("Vaše věta obsahuje: " + str(pocet_slov) + " slov")