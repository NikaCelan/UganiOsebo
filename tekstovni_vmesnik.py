import model

def izpis_igre(igra):
    return (
        "izbrana oseba: {}\n".format(model.nakljucna_oseba) +
        "odgovor: {}\n".format(igra.ugibaj())
    )

def izpis_zmage(igra):
    return (
        "Čestitam, uganil si osebo. Ime ji je {}\n".format(model.nakljucna_oseba['ime'])
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