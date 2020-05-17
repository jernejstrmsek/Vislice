import model

def izpis_igre(igra):
    izpis = (
        "Preostali poskusi: {preostali_poskusi} \n"
        "Pravilni del gesla: {pravilni_del_gesla} \n"
        "Neuspešni poskusi: {nepravilni_poskusi}" 
    ).format(
        preostali_poskusi = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak(),
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        nepravilni_poskusi = igra.nepravilni_ugibi()
    )
    return izpis

def izpis_zmage(igra):
    izpis = (
        "Bravo, zmaga! Geslo je bilo: {geslo}"
        "Ostalo ti je še {st_poskusov} poskusov"
    ).format(
        geslo = igra.geslo,
        st_poskusov = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()
    )
    return izpis

def izpis_poraza(igra):
    izpis = (
        
        ":( Žal ste porabili vse poskuse. :("
        "Geslo je bilo {geslo}."
    ).format(
        geslo = igra.geslo
    )
    return izpis

def zahtevaj_vnos():
    return input("Prosim vnesite črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        rezultat_poskusa = igra.ugibaj(crka)
        #preveti ali je bila dosežena zmaga
        if rezultat_poskusa == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        #preveri ali je bil dosežen poraz
        elif rezultat_poskusa == model.PORAZ:
            print(izpis_poraza(igra))
            break
        #preveri ali je bila črka že uporabljena
        elif rezultat_poskusa == model.PONOVLJENA_CRKA:
            print("To črko ste že uporabili, poskusite ponovno.")
    #igralcu ponudi še eno igro
    ponovitev = input("Ali želite igrati ponovno? Vpisite DA ali NE:")
    while ponovitev.upper() not in ["DA", "NE"]:
        ponovitev = input("Prosim vensite DA ali NE")
    if ponovitev.upper() == "DA":
        pozeni_vmesnik()
    elif ponovitev.upper() == "NE":
        print("Hvala, da ste igrali!")

pozeni_vmesnik()

