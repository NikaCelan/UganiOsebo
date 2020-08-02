import random
import json

ZACETEK = 'Z'

ZMAGA = 'W'


DATOTEKA_STANJE = 'stanje.json'

osebe = []
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
    osebe.append(oseba)


polje_oseb = []
#stevila od 0 do 13 (vsaka za eno osebo), ki se bodo brisala iz polja,
#  ko bo oseba izpadla iz ugibanja
for i in range(len(osebe)):   
    polje_oseb.append(i)


class Igra:

    def __init__ (self, oseba, kriterij = None, vrednost = None):
        self.oseba = oseba
        self.kriterij = kriterij
        self.vrednost = vrednost

    def zmaga(self):
        if len(polje_oseb) == 1:
            return True

    # def izberi_kriterij(kriterij):
    #     if kriterij == spol:
    #         return {kriterij: moški, ženska}
    #     elif kriterij == barva las:
    #         return {barva las: blond, črna, rdeča, rjava, nima las}
    #     elif kriterij == dolžina las:
    #         return {kriterij: kratki, dolgi}
    #     elif kriterij == barva majice:
    #         return {kriterij: rdeča, črna, siva, zelena, bela, modra}
    #     elif kriterij == usta:
    #         return {kriterij: odprta, zaprta}
        
    
    def ugibaj(self, kriterij, vrednost):
        global polje_oseb
        pomozni = polje_oseb.copy()
        if vrednost == self.oseba[kriterij]:
            print('pravilno')
            for i in polje_oseb:
                druga_oseba = osebe[i]
                if vrednost != druga_oseba[kriterij]:
                    pomozni.remove(i)
            polje_oseb = pomozni.copy()
            if self.zmaga():
                return ZMAGA
        else:
            print('napačno')
            for i in polje_oseb:
                druga_oseba = osebe[i]
                if vrednost == druga_oseba[kriterij]:
                    pomozni.remove(i)
            polje_oseb = pomozni.copy()        
            if self.zmaga():
                return ZMAGA

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

