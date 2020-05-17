import random

#konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo
        self.crke = []

    def pravilne_crke(self):
        return list(set(self.crke) - set(self.pravilne_crke()))

    def napacne_crke(self):
        return list((set(self.crke) - set(self.geslo)))

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return self.pravilni_del_gesla() == self.geslo

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self): #vrne niz z že uganjenim delom gesla, tako da neznane črke zamenja s podčrtajem
        geslo = self.geslo
        for x in self.geslo:
            if x.lower() not in str(self.crke).lower():
                geslo = geslo.replace(x, "_")
        return geslo

    def nepravilni_ugibi(self): #vrne niz, ki vsebuje s presledkom ločene nepravilne ugibe
        delni = ''
        geslo = self.geslo.lower()
        for crka in self.crke:
            if crka not in geslo:
                delni += crka
        return delni

    def ugibaj(self, crka): # sprejme črko, jo pretvori v veliko črko, in vrne ustrezno konstanto
        izbrana_crka = crka.upper()
        if izbrana_crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(izbrana_crka)
        if izbrana_crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            return NAPACNA_CRKA


#ustvari seznam možnih gesel
with open("besede.txt", encoding="utf-8") as dat:
    besede = []
    for vrstica in dat:
        besede.append(vrstica.strip().upper())

#zgradi in vrne novo igro
def nova_igra():
    beseda = random.choice(besede)
    return Igra(beseda)

a = nova_igra()