import math, datetime, random, modul_Engeto
#Pozdrav
#print("Ahojte pyton kurzu pokračování")

#chci do proměnné, která popisuje váhu vánočního stromečku uložit 5.98
#váha_stromčku = 5.98

#Je možné uložit novou váhu stromčku?v proměnné Nová váha 6.01
#váha_stromčku = 6.01

# Jestli má vůz pojištění
#je_vůz_pojištěn = True

#print(bool(["meloum","káva"]))
#print(51<51)
#print(10!=10)

# Cyklus = iterace
#Na dálnici chceme vypsat upozonění Pozor nehoda
#print("Pozor nehoda!!")

#Vypsat 5x
#print("Pozor nehoda!!")
#print("Pozor nehoda!!")
#print("Pozor nehoda!!")
#print("Pozor nehoda!!")
#print("Pozor nehoda!!")

#Vypsat 55x
for i in range(55):
    print("Pozor nehoda!!")
    print("Tělo cyklu")

# Cyklus While
#správné_heslo = "20"
#user_input = input("Zadejte heslo:")

#while user_input != správné_heslo:
    #print("Nesprávné heslo, zkuste to znovu.")
    #user_input = input("Zadejte heslo:")

#print("Přihlášení úspěšné")    

# Podmínky IF, elif, else
věk_uživatele = -15

if věk_uživatele >0 and věk_uživatele <18:
    print("kofola")   
elif věk_uživatele >=18 and věk_uživatele <64:
    print("Nazdraví")  
elif věk_uživatele >=64 and věk_uživatele <140:
    print("Pozor píjte s rozumem")
else:
    print("Chyba, špatně zadaný věk")

#Funkce - obvod trojúhelníku
def obvod_trojúhelníku(strana_a, strana_b, strana_c):
    obvod = strana_a+strana_b+strana_c
    return obvod

#Zadání: a=45 b´=56, c=150
print(obvod_trojúhelníku(45,56,150))

#Funkce Pozdrav Eng.Studenti
def pozdrav_Engeto_studfentu():
    print("Ahojte studenti")

#Volám funkci
pozdrav_Engeto_studfentu()   

#z modulu math poziji funkci odmocnina
#prnt(match.sqrt(16))

#z modulu datetime poziji funkci aktualni čas
aktualni_čas = datetime.datetime.now()
print(aktualni_čas)

#z modulu random pro náhodný výběr
print(random.choice(['voda','minerální voda','nic']))

#pizití funkce z vlastního modulu
print(modul_Engeto.součet(50,5))
print(modul_Engeto.rodíl(50,5))

#funkce, která pozdraví Studenti engetu zdar
#funkce, která se rozloučí Engeto konec
#speciální objem koule