import os
import kerntranslate as kern

def init(i, path):
    nombrearchivokern = 'k' + str(i) +'.kern'
    global fKern 
    fKern = open(os.path.join(path, nombrearchivokern), "w")
    fKern.write('**kern\n')

def clef(c):
    global clave
    clave = c
    fKern.write(kern.clefs[clave])
    fKern.write('\n')

def key(k):
    global tonalidad
    tonalidad = k
    fKern.write(kern.accidentals[tonalidad])
    fKern.write('\n')

def metric(compass):
    fKern.write(kern.compasses[compass[0]])
    fKern.write('\n')

def compas(i):
    fKern.write(kern.compas(i))
    fKern.write('\n') 

def simbolo(s):
    fKern.write(kern.simbolo(s, clave, tonalidad))
    fKern.write('\n')

def end(i):
    fKern.write('=')
    fKern.write(str(i))
    fKern.write('\n')                    
    fKern.write('*_')

def close():
    fKern.close()