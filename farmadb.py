
'''
sa se faca o baza de date de gestionare a medicamentelor intro farmacie.
Datele se salveaza si se citesc dintr-un fisier.
Baza de date trebuie sa permita urmatoarele operatiuni

cauta <Nume>
va afisa cate bucati sunt din acel <Nume> si pretul/bucata

vinde <Nume> <cantitatea>
va elimina din baza de date <cantitatea> de <Nume>

adauga <Nume> <cant> <pret/bucata>
va adauga in baze de date

quit
Va salva totul intrun fisier de tipul farmacie.txt
'''

import sys
#poti crea cate variabile globale vrei

def CitireDinFisier(caleFisier):
    #aici trebuie sa scrii cod, sa incarci datele din fisierul txt
    #datele sunt de forma
    #medicament cantitate pret_per_bucata
    pass
    
def SalvareInFisier(storedb):
    #aici actualizezi fisierul txt cu noile date
    pass
    
def Cauta(med):
    #aici cauti dupa ceva, si returnezi acel ceva
    pass

def Vinde(med, quant):
    pass
    
def Vinde(med, quant, pret):
    pass    

def processInput(command):
    pass

if __name__=="__main__":
    pyver=sys.version_info[0]
    while(True):
        #print to console
        print("farmadb>")
        if pyver == 2:
            command = str(raw_input())
        else:
            command = str(input())
        if command == "quit":
            break
        #asta ii sa vezi ce comanda scrii    
        print(command)
        #aici procesesi comenzile
        processInput(command)
        
    #salveaza ce ai lucrat    
    print("bye")