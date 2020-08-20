import random
import json

ZACETEK = 'Z'

ZMAGA = 'W'

DATOTEKA_STANJE = 'stanje.json'

osebe = []
izdelava_menija = []
#naredimo seznam oseb v katerem bodo slovarji z lastnostmi oseb
datoteka_osebe = open("osebe.txt", "r", encoding='utf-8')
for line in datoteka_osebe: 
    oseba = {}
    lined = line.split(",")
    for i in range(len(lined)):
        (key, val) = lined[i].split(":")
        key = key.strip()
        val = val.strip()
        oseba[key] = val
        zapis_v_meni = key + ":" + val
        if zapis_v_meni not in izdelava_menija:
            izdelava_menija.append(zapis_v_meni)
    osebe.append(oseba)

#stevila od 0 do 13 (vsaka za eno osebo), ki se bodo brisala iz polja,
#  ko bo oseba izpadla iz ugibanja
polje_oseb = []
izdelava_menija.sort()
for i in range(len(osebe)):   
    polje_oseb.append(i)

#izdelava menija za prikaz spustnega seznama

class Igra:

    def __init__ (self, oseba, kriterij = None, vrednost = None, stevilo_poskusov = 0, napaka = None):
        self.oseba = oseba
        self.kriterij = kriterij
        self.vrednost = vrednost
        self.stevilo_poskusov = stevilo_poskusov
        self.napaka = napaka

    def zmaga(self):
        if len(polje_oseb) == 1:
            return True

    def povecaj_stevilo_poskusov(self):
        self.stevilo_poskusov += 1
    
    def vrni_stevilo_poskusov(self):
        return self.stevilo_poskusov

    def vrni_pravilnost(self):
        if self.pravilnost:
            return "Pravilno!" 
        else:
            return "Nepravilno!"
    
    #napake veljajo le za delo v tekstovnem vmesniku 
    # kjer uporabnik sam napiše kriterij in vrednost
    def napaka_pri_vnosu(self, napaka):
        self.napaka = napaka

    def vrni_napako(self):
        if self.napaka:
            return "Vnesel si neobstoječ kriterij!"
        else:
            return ""
    
    def ugibaj(self, kriterij, vrednost):
        global polje_oseb
        pomozni = polje_oseb.copy()
        if kriterij in self.oseba:
            self.povecaj_stevilo_poskusov()
            if vrednost == self.oseba[kriterij]:
                self.pravilnost = True
                for i in polje_oseb:
                    druga_oseba = osebe[i]
                    if vrednost != druga_oseba[kriterij]:
                        pomozni.remove(i)
                polje_oseb = pomozni.copy()
                if self.zmaga():
                    return ZMAGA
            else:
                self.pravilnost = False
                for i in polje_oseb:
                    druga_oseba = osebe[i]
                    if vrednost == druga_oseba[kriterij]:
                        pomozni.remove(i)
                polje_oseb = pomozni.copy()        
                if self.zmaga():
                    return ZMAGA
        else:
            self.napaka_pri_vnosu(True)

nakljucna_oseba = random.choice(osebe)   
def nova_igra():
    return Igra(nakljucna_oseba)
class UganiOsebo:
    def __init__(self, datoteka_s_stanjem):
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.nalozi_igre_iz_datoteke()

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

    def ugibaj(self, id_igre, kriterij, vrednost):
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(kriterij, vrednost)
        self.igre[id_igre] = (igra, stanje) 
        self.zapisi_igre_v_datoteko() 

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f) 
            self.igre = {int(id_igre): (Igra(oseba, kriterij, vrednost), stanje) 
            for id_igre, (oseba, kriterij, vrednost, stanje) in igre.items()}

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f: 
            igre = {id_igre: (igra.oseba, igra.kriterij, igra.vrednost, stanje) for id_igre, (igra, stanje) in self.igre.items()}
            json.dump(igre, f, ensure_ascii=False)

