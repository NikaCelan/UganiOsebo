import model

def izpis_igre(igra):
    return (
        "izbrana oseba: {}\n".format(nova_igra()) +
        "odgovor: {}\n".format(igra.ugibaj())
    )

def izpis_zmage(igra):
    return (
        "Čestitam, uganil si geslo {}\n".format(igra.geslo) +
        "Uspelo ti je v {} poskusih\n".format(len(igra.crke))
    )

def izpis_poraza(igra):
    return (
        "Porabil si vse poskuse.\n" +
        "Pravilno geslo je bilo {}\n".format(igra.geslo)
    )

def zahtevaj_kriterij():
    return input('Kriterij: ')

def zahtevaj_vrednost():
    return input('Vrednost: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        poskus_k = zahtevaj_kriterij()
        poskus_v = zahtevaj_vrednost()
        stanje = igra.ugibaj(poskus_k, poskus_v)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break

pozeni_vmesnik()