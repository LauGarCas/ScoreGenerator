import os
import kerntranslate as kern
import agnostictranslate as agnostic

def init(i, path):
    nombrearchivokern = 'k' + str(i) +'.kern'
    global fKern 
    fKern = open(os.path.join(path, nombrearchivokern), "w")
    fKern.write('**kern\n')

    nombrearchivoagnostico = 'a' + str(i) +'.txt'
    global fAgnostic 
    fAgnostic = open(os.path.join(path, nombrearchivoagnostico), "w")

def clef(c):
    global clave
    clave = c
    fKern.write(kern.clefs[clave])
    fKern.write('\n')

    fAgnostic.write(agnostic.clefs[clave][0])
    fAgnostic.write(agnostic.advance)

def key(k):
    global tonalidad
    tonalidad = k
    fKern.write(kern.accidentals[tonalidad])
    fKern.write('\n')

    fAgnostic.write(agnostic.accidentals(tonalidad, clave))


def metric(c):
    fKern.write(kern.compasses[c[0]])
    fKern.write('\n')

    fAgnostic.write(agnostic.compasses[c[0]])
    fAgnostic.write(agnostic.advance)

def compas(i):
    fKern.write(kern.compas(i))
    fKern.write('\n') 

    fAgnostic.write(agnostic.compas(i))

def simbolo(s):
    fKern.write(kern.simbolo(s, clave, tonalidad))
    fKern.write('\n')

    fAgnostic.write(agnostic.simbolo(s, clave))
    fAgnostic.write(agnostic.advance)

def end(i):
    fKern.write('=')
    fKern.write(str(i))
    fKern.write('\n')                    
    fKern.write('*_')

    fAgnostic.write(agnostic.end())

def close():
    fKern.close()
    fAgnostic.close()