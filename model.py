import random
import json

ZACETEK = 'Z'

PRAVILNI_UGIB = '+'
NAPACEN_UGIB = '-'

ZMAGA = 'W'
PORAZ = 'L'


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

    def __init__ (self, oseba):
        self.oseba = oseba

    def zmaga(self):
        if len(polje_oseb) == 1:
            return True
    
    def ugibaj(self, kriterij, vrednost):
        global polje_oseb
        pomozni = polje_oseb.copy()
        if vrednost == self.oseba[kriterij]:
            print('pravilno')
            for i in polje_oseb:
                druga_oseba = osebe[i]
                if vrednost != druga_oseba[kriterij]:
                    pomozni.remove(i)
                    print(pomozni)
            polje_oseb = pomozni.copy()
            if self.zmaga():
                print('ZMAGA')
                return ZMAGA
        else:
            print('napačno')
            for i in polje_oseb:
                druga_oseba = osebe[i]
                if vrednost == druga_oseba[kriterij]:
                    pomozni.remove(i)
                    print(pomozni)
            polje_oseb = pomozni.copy()        
            if self.zmaga():
                print('ZMAGA')
                return ZMAGA

    
def nova_igra():
    nakljucna_oseba = random.choice(osebe)
    print(nakljucna_oseba)
    return Igra(nakljucna_oseba)

