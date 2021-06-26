import os
import kerntranslate as kern
import agnostictranslate as agnostic

def init(i, path, typeagnostic):
    nombrearchivokern = 'k' + str(i) +'.kern'
    global fKern 
    fKern = open(os.path.join(path, nombrearchivokern), "w")
    fKern.write('**kern\n')

    nombrearchivoagnostico = 'a' + str(i) +'.txt'
    global fAgnostic 
    fAgnostic = open(os.path.join(path, nombrearchivoagnostico), "w")
    agnostic.valueSeparator(typeagnostic)

    global hayAcorde
    hayAcorde = False

    global escribirAcorde
    escribirAcorde = []

def polyinit(i, path, typeagnostic):
    nombrearchivokern = 'k' + str(i) +'.kern'
    global fKern 
    fKern = open(os.path.join(path, nombrearchivokern), "w")
    fKern.write('**kern\t**kern\n')

    global nombrearchivoagnostico1
    nombrearchivoagnostico1 = 'a_' + str(i) +'.txt'
    nombrearchivoagnostico2 = 'a' + str(i) +'.txt'

    global fAgnostic 
    global fAgnostic2
    fAgnostic = open(os.path.join(path, nombrearchivoagnostico1), "w")
    fAgnostic2 = open(os.path.join(path, nombrearchivoagnostico2), "w")

    agnostic.valueSeparator(typeagnostic)

    global hayAcorde1
    hayAcorde1 = False
    global hayAcorde2
    hayAcorde2 = False

    global escribirAcorde
    escribirAcorde = []

def clef(c):
    global clave
    clave = c
    fKern.write(kern.clefs[clave] + '\n')

    fAgnostic.write(agnostic.clefs(clave))
    fAgnostic.write(agnostic.advance)

def polyclef(c, c2):
    global clave
    global clave2
    clave = c
    clave2 = c2
    fKern.write(kern.clefs[clave] + "\t" + kern.clefs[clave2] + "\n")

    fAgnostic.write(agnostic.clefs(clave))
    fAgnostic.write(agnostic.advance)
    fAgnostic2.write(agnostic.clefs(clave2))
    fAgnostic2.write(agnostic.advance)

def key(k):
    global tonalidad
    tonalidad = k
    fKern.write(kern.accidentals[tonalidad] + '\n')

    fAgnostic.write(agnostic.accidentals(tonalidad, clave))

def polykey(k):
    global tonalidad
    tonalidad = k
    fKern.write(kern.accidentals[tonalidad] + '\t' + kern.accidentals[tonalidad] + '\n')

    fAgnostic.write(agnostic.accidentals(tonalidad, clave))
    fAgnostic2.write(agnostic.accidentals(tonalidad, clave2))

def metric(c):
    fKern.write(kern.compasses[c[0]] + '\n')

    fAgnostic.write(agnostic.compass(c[0]))
    fAgnostic.write(agnostic.advance)

def polymetric(c):
    fKern.write(kern.compasses[c[0]] + '\t' + kern.compasses[c[0]] + '\n')

    fAgnostic.write(agnostic.compass(c[0]))
    fAgnostic.write(agnostic.advance)
    fAgnostic2.write(agnostic.compass(c[0]))
    fAgnostic2.write(agnostic.advance)

def compas(i):
    fKern.write(kern.compas(i) + '\n')

    fAgnostic.write(agnostic.compas(i))

def polycompas(i):
    fKern.write(kern.compas(i) + '\t' + kern.compas(i) + '\n')
    
    fAgnostic.write(agnostic.compas(i))
    fAgnostic2.write(agnostic.compas(i))

def simbolo(s, compass_accidentals, chord):
    global hayAcorde
    global escribirAcorde
    if chord:
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + ' ')
    else:
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\n')

    if not hayAcorde and not chord: #es una nota normal
        fAgnostic.write(agnostic.simbolo(s, clave))
        fAgnostic.write(agnostic.advance)

    elif hayAcorde and chord: #estamos dentro de un acorde
        escribirAcorde.append(s)
    
    elif not hayAcorde and chord: #es la primera nota del acorde
        hayAcorde=True
        escribirAcorde.append(s)

    elif hayAcorde and not chord: #es la ultima nota del acorde
        hayAcorde=False
        escribirAcorde.append(s)
        fAgnostic.write(agnostic.acorde(escribirAcorde, clave))
        escribirAcorde = []

def polysimbolo(s, s2, compass_accidentals, compass_accidentals2, chord1, chord2):
    global hayAcorde1
    global hayAcorde2
    global escribirAcorde

    if not hayAcorde1 and not hayAcorde2 and not chord1 and not chord2: #son dos notas normales
        hayAcorde1 = False
        hayAcorde2 = False
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\t' + kern.simbolo(s2, clave2, tonalidad, compass_accidentals2) + '\n')

        res = agnostic.simbolo(s, clave)
        fAgnostic.write(res)
        if res!= '':
            fAgnostic.write(agnostic.advance)
        res = agnostic.simbolo(s2, clave2)
        fAgnostic2.write(res)
        if res!= '':
            fAgnostic2.write(agnostic.advance)
    
    elif hayAcorde1 and chord1: #estamos dentro de un acorde en el compás1
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + ' ')
        escribirAcorde.append(s)
    
    elif not hayAcorde1 and chord1: #es la primera nota del acorde en el compás1
        print('es la primera nota del acorde en el compás1')
        hayAcorde1=True
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + ' ')
        escribirAcorde.append(s)

    elif hayAcorde1 and not chord1 and not chord2: #es la ultima nota del acorde en el compás1 y no hay acorde en el compas2
        print('es la ultima nota del acorde en el compás1 y no hay acorde en el compas2')
        hayAcorde1=False
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\t' + kern.simbolo(s2, clave2, tonalidad, compass_accidentals2) + '\n')       
        escribirAcorde.append(s)
        fAgnostic.write(agnostic.acorde(escribirAcorde, clave))
        escribirAcorde = []
        res = agnostic.simbolo(s2, clave2)
        fAgnostic2.write(res)
        if res!= '':
            fAgnostic2.write(agnostic.advance)
    
    elif hayAcorde1 and not chord1 and chord2: #es la ultima nota del acorde en el compás1 pero empieza un acorde en el compas2
        hayAcorde1 = False
        hayAcorde2 = True
        print('es la ultima nota del acorde en el compás1 pero empieza un acorde en el compas2')
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\t' + kern.simbolo(s2, clave2, tonalidad, compass_accidentals2) + ' ')
        escribirAcorde.append(s)
        fAgnostic.write(agnostic.acorde(escribirAcorde, clave))
        escribirAcorde = []
        escribirAcorde.append(s2)

    elif not hayAcorde2 and chord2: #es la primera nota del acorde en el compás2 y no habia acorde en el compas1
        print('es la primera nota del acorde en el compás2 y no habia acorde en el compas1')
        hayAcorde2=True
        fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\t' + kern.simbolo(s2, clave2, tonalidad, compass_accidentals2) + ' ')
        res = agnostic.simbolo(s, clave)
        fAgnostic.write(res)
        if res!= '':
            fAgnostic.write(agnostic.advance)
        escribirAcorde.append(s2)
    
    elif hayAcorde2 and chord2: #estamos dentro de un acorde en el compás2
        print('estamos dentro de un acorde en el compás2')
        fKern.write(kern.simbolo(s2, clave2, tonalidad, compass_accidentals2) + ' ')
        escribirAcorde.append(s2)

    elif hayAcorde2 and not chord2: #es la ultima nota del acorde en el compás2
        print('es la ultima nota del acorde en el compás2')
        hayAcorde2=False
        fKern.write(kern.simbolo(s2, clave2, tonalidad, compass_accidentals2) + '\n')
        escribirAcorde.append(s2)
        fAgnostic.write(agnostic.acorde(escribirAcorde, clave2))
        escribirAcorde = []


def end(i):
    fKern.write('=' + str(i) + '\n' + '*-')

    fAgnostic.write(agnostic.end())

def polyend(i, path):
    fKern.write('=' + str(i) + '\t' + '=' + str(i) + '\n' + '*-' + '\t' + '*-')

    fAgnostic.write(agnostic.end())
    fAgnostic2.write(agnostic.end())
    #Combinamos los dos archivos en uno
    fAgnostic2.write('\n')
    fAgnostic.close()

    with open(os.path.join(path, nombrearchivoagnostico1), "r") as f:
        fAgnostic2.write(f.read())

    os.remove(os.path.join(path, nombrearchivoagnostico1))


def close():
    fKern.close()
    fAgnostic.close()
