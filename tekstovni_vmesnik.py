import model

def izpis_osebe(oseba):
    return (
        " {}".format(oseba) 
    )

def izpis_igre(igra):
    return ( 
        "Odgovor: {}\n".format(igra.vrni_pravilnost()) +
        "Tvoje število ugibanj je {}\n".format(igra.vrni_stevilo_poskusov())
    )
def izpis_napake(igra):
    return (
        "{}\n".format(igra.vrni_napako())
    )

def izpis_zmage(igra):
    return (
        "Čestitam, uganil/a si osebo. Ime ji je {}\n".format(model.nakljucna_oseba['ime'])+
        "Ugotovil/a si v {}. poskusu.\n".format(igra.vrni_stevilo_poskusov())
    )

def izpis_poraza(igra):
    return (
        "Izgubil si! Izbrana oseba je bila {}\n".format(model.nakljucna_oseba['ime'])
    )

#def izpis_poskusov(igra):
 #   return (
  #      "Tvoje število ugibanj je {}\n".format(igra.vrni_stevilo_poskusov())
   # )

def zahtevaj_kriterij():
    return input('\nKriterij: ')

def zahtevaj_vrednost():
    return input('Vrednost: ')


def pozeni_vmesnik():
    igra = model.nova_igra()
    print("\nUGANI OSEBO\n")
    print("Med naštetimi osebami ugani tisto, ki jo je naključno izbral računalnik. Na voljo imaš neomejeno poskusov.\n")
    for i in range(len(model.osebe)):
        print(izpis_osebe(model.osebe[i]))
    while True:  
        poskus_k = zahtevaj_kriterij()
        poskus_v = zahtevaj_vrednost()
        stanje = igra.ugibaj(poskus_k, poskus_v)
        if igra.vrni_napako() == "":
            if stanje == model.ZMAGA:
                print(izpis_zmage(igra))
                break
            else:
                print(izpis_igre(igra))
        else:
            print(izpis_napake(igra))

pozeni_vmesnik()
