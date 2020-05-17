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

    def pravilni_del_gesla(self):
        geslo = self.geslo
        for x in self.geslo:
            if x.lower() not in str(self.crke).lower():
                geslo = geslo.replace(x, "_")
        return geslo

    def nepravilni_ugibi(self):
        delni = ''
        geslo = self.geslo.lower()
        for crka in self.crke:
            if crka not in geslo:
                delni += crka
        return delni

    def ugibaj(self, crka): #
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

def nova_igra():
    beseda = random.choice(besede)
    return Igra(beseda)

a = nova_igra()