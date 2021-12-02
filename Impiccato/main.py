import os
from random import choice
from parole import lista, caratteri_consentiti
from disegni import stato_impiccato, logo, vinto, perso

def mostraImpiccato(vite,txt_precedente):
    os.system('cls||clear')
    print(intro_string)
    print("============================================")
    print(stringa_output)
    print(stato_impiccato[vite])
    print("\n"+txt_precedente)

vite = len(stato_impiccato)-1
continua_gioco = True
suggerimento = "Possibili scelte: lettere da 'a' a 'z' e accentate (à-è-ì-ò-ù)"
intro_string = logo + suggerimento

parola_da_indovinare = choice(lista).upper()

stringa_output = [];
for _ in range(len(parola_da_indovinare)):
    stringa_output += "_"

txt_precedente = ''

while continua_gioco:

    mostraImpiccato(vite,txt_precedente)

    ## input lettera e verifica carattere se consentito
    scelta_ok = False
    while not scelta_ok:
        print("============================================")
        scelta = input("Digita una lettera: ").upper()
        print("============================================")
        
        if scelta.upper() in caratteri_consentiti:
            scelta_ok = True
        else:
            print(suggerimento)
            
            
    if scelta in parola_da_indovinare:
        txt_precedente = f"CORRETTO!! - La lettera '{scelta}' è all'interno della parola da indovinare"
        for index in range(len(parola_da_indovinare)):
            if scelta == parola_da_indovinare[index]:
                stringa_output[index] = scelta
    else:
        txt_precedente = f"ERRATO!! - La lettera '{scelta}' NON è all'interno della parola da indovinare"
        vite -= 1

    if vite == 0 or "_" not in stringa_output:
        continua_gioco = False


mostraImpiccato(vite,txt_precedente)
print("============================================")
if vite == 0:
    print(perso)
else:
    print(vinto)
    
print(f"La parola da indovinare era '{parola_da_indovinare}'")
print("============================================")