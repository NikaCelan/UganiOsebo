import random
import json

ZACETEK = 'Z'

ZMAGA = 'W'
PORAZ = 'L'


osebe=[]
with open('UganiOsebo/osebe.txt', encoding='UTF-8') as datoteka_osebe:
    for vrstica in datoteka_osebe:
        osebe.append(vrstica[])

vprasanja=[]
with open('UganiOsebo/vprasanja.txt', encoding='UTF-8') as datoteka_vprasanja:
    for vprasanje in datoteka_vprasanja:
        vprasanja.append(vprasanje)

class Igra:

    def __init__ (self, oseba, vprasanje):
        self.oseba = osebe[x]

    def ugibi(self):
        for lastnost in osebe[]

    
def nova_igra():
    nakljucna_oseba = random.choice(osebe)
    return Igra(nakljucna_oseba)


class UgibajOsebo:
    '''
    Skrbi za trenutno stanje več iger (imel bo več objektov tipa igra)
    '''

    def __init__(self):
        #slovar, ki ID-ju priredi objektt njegove igre
        self.igre = {}      #int -> (Igra, stanje)
    
    def prost_id_igre(self):
        '''Vrne nek id za novo igro, ki ga ne uporablja se nobena igra '''
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        # dobimo novi ID

        id_igre = self.prost_id_igre()

        # naredimo novo igre

        igra = nova_igra()

        # vse to shranimo v self.igre

        self.igre[id_igre] = (igra, ZACETEK)
        
        # vrnemo nov ID

        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ =self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)