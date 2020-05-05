import math

def je_prastevilo(stevilo):
    #Vrne "True", če je število praštevilo in "Fale", če število ni preštevilo
    if stevilo == 1:
        return False

    #Če je število sodo ne more biti praštevilo razen 2
    if stevilo == 2:
        return True
    if stevilo % 2 == 0:
        return False

    najvecji_delitelj = math.floor(math.sqrt(stevilo))
    for d in range(3, najvecji_delitelj + 1, 2):
        if stevilo % d == 0:
            return False
    return True

def prastevila_do(n):
    prastevila = []
    for x in range(n):
        if je_prastevilo(x):
            prastevila.append(x)
    return prastevila

print(prastevila_do(200))