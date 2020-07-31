import bottle
import model

SKRIVNOST = 'moja skrivnost'
PISKOTEK = 'idigre'

uganiosebo = model.UganiOsebo(model.DATOTEKA_STANJE)

@bottle.get('/')
def index():
    return bottle.template('views/index.tpl')

@bottle.post('/nova-igra/')
def nova_igra():
    id_igre = uganiosebo.nova_igra()
    bottle.response.set_cookie(PISKOTEK, str(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, stanje = uganiosebo.igre[id_igre]
    return bottle.template('views/igra.tpl', igra=igra, stanje=stanje)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    kriterij = bottle.request.forms.getunicode('kriterij')
    
    uganiosebo.ugibaj(id_igre, kriterij, vrednost)
    bottle.redirect('/igra/')

# @bottle.get('/img/<slika>')
# def pokazi_sliko(slika):
#     return bottle.static_file(slika, root='img')

bottle.run(reloader=True, debug=True)