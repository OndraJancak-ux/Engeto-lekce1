seznam_cisel = [5, -3, 0, 12, -7]
for cislo in seznam_cisel:
    if cislo > 0:
        print(f"{cislo} je kladné číslo")
    elif cislo < 0:
        print(f"{cislo} je záporné číslo")
    else:
        print(f"{cislo} je nulové číslo")
        