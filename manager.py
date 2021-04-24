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

def polyinit(i, path, typeagnostic):
    nombrearchivokern = 'k' + str(i) +'.kern'
    global fKern 
    fKern = open(os.path.join(path, nombrearchivokern), "w")
    fKern.write('**kern\t**kern\n')

    global nombrearchivoagnostico2
    nombrearchivoagnostico1 = 'a' + str(i) +'.txt'
    nombrearchivoagnostico2 = 'a_' + str(i) +'.txt'

    global fAgnostic 
    global fAgnostic2
    fAgnostic = open(os.path.join(path, nombrearchivoagnostico1), "w")
    fAgnostic2 = open(os.path.join(path, nombrearchivoagnostico2), "w")

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


def simbolo(s, compass_accidentals):
    fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\n')

    fAgnostic.write(agnostic.simbolo(s, clave))
    fAgnostic.write(agnostic.advance)

def polysimbolo(s, s2, compass_accidentals, compass_accidentals2):
    fKern.write(kern.simbolo(s, clave, tonalidad, compass_accidentals) + '\t' + kern.simbolo(s2, clave, tonalidad, compass_accidentals2) + '\n')

    fAgnostic.write(agnostic.simbolo(s, clave))
    fAgnostic.write(agnostic.advance)
    fAgnostic2.write(agnostic.simbolo(s2, clave2))
    fAgnostic2.write(agnostic.advance)

def end(i):
    fKern.write('=' + str(i) + '\n' + '*-')

    fAgnostic.write(agnostic.end())

def polyend(i):
    fKern.write('=' + str(i) + '\t' + '=' + str(i) + '\n' + '*-' + '\t' + '*-')

    fAgnostic.write(agnostic.end())
    fAgnostic.write(agnostic.end())
    #Combinamos los dos archivos en uno
    fAgnostic.write('\n')
    fAgnostic2.close()

    with open(nombrearchivoagnostico2) as infile:
        fAgnostic.write(infile.read())


def close():
    fKern.close()
    fAgnostic.close()