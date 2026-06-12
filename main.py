import time


#Komunikaty
HASLO_BARDZO_MOCNE='Podane hasło jest bardzo mocne ponieważ jest długie, zawiera duże, małe litery, cyfry'
HASLO_MOCNE='Podane hasło jest mocne ponieważ jest dość długie, zawiera duże litery lub małe litery lub cyfry'
HASLO_SLABE='Podane hasło jest słabe ponieważ jest za krótkie'
HASLO_POPULARNE='Wygląda na to że twoje hasło to popularna sekwencja, hasło jest mało unikatowe, zmień je!'
haslo=input("Podaj swoje hasło: ")
duze=0
malo=0
znakispc=0
cyfry=0
dl=0
for i in hasło:
    if i.isupper():
        duze+=1
        dl+=1
    elif i.islower():
        male+=1
        dl+=1
    elif i.isdigit():
        cyfry+=1
        dl+=1
    else:
        znakispc+=1
        dl+=1
print("Analiza hasła: ")
print(f"Długo)
