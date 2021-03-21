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
    fKern.write(kern.clefs[clave])
    fKern.write(kern.clefs[clave] + "\t" + kern.clefs[clave2] + "\n")

def key(k):
    global tonalidad
    tonalidad = k
    fKern.write(kern.accidentals[tonalidad] + '\n')

    fAgnostic.write(agnostic.accidentals(tonalidad, clave))


def metric(c):
    fKern.write(kern.compasses[c[0]] + '\n')

    fAgnostic.write(agnostic.compass(c[0]))
    fAgnostic.write(agnostic.advance)

def compas(i):
    fKern.write(kern.compas(i) + '\n')

    fAgnostic.write(agnostic.compas(i))

def simbolo(s):
    fKern.write(kern.simbolo(s, clave, tonalidad) + '\n')

    fAgnostic.write(agnostic.simbolo(s, clave))
    fAgnostic.write(agnostic.advance)

def end(i):
    fKern.write('=' + str(i) + '\n' + '*_')

    fAgnostic.write(agnostic.end())

def close():
    fKern.close()
    fAgnostic.close()