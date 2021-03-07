import random
import os
import symbol
import dictionary
import kerntranslate as kern

nc = input("Introduce el número de compases... ")  #Numero de compases
numScores = input("Introduce el número de partituras... ") #numero de partituras

nc = int(nc)
numScores= int(numScores)

#funcion principal en la que se recogen los parametros y se generan las partituras
def scoreGenerator(ncompasses, nscores):
    try:
        for j in range(nscores):
            path = 'salida'+str(j)
            if not os.path.exists(path):
                os.makedirs(path)
            nombrearchivo = 'salida' + str(j) +'.txt'
            nombrearchivokern = 'k' + str(j) +'.kern'
            #creamos los archivos
            with open(os.path.join(path, nombrearchivo), "w") as f1, open(os.path.join(path, nombrearchivokern), "w") as f2:

                #inicializar los archivos
                f2.write('**kern\n')

                #se decide el tipo de clave a utilizar
                clef = chooseClef()
                f1.write(clef)
                f1.write('\n')

                f2.write(kern.clefs[clef])
                f2.write('\n')
                
                #se elige la tonalidad
                key = chooseKey()
                f1.write(key)
                f1.write('\n')

                f2.write(kern.accidentals[key])
                f2.write('\n')
                
                #se elige el tipo de compas
                compass = chooseCompass()
                f1.write(compass[0])
                f1.write('\n')

                f2.write(kern.compasses[compass[0]])
                f2.write('\n')

                #inicializamos la ligadura y la altura
                tie = 0
                pitch = 11 #número entre el 1 y el 22
                #se empiezan a generar compases
                for i in range(ncompasses):
                    lastcompass = False
                    if i == ncompasses - 1:
                        lastcompass = True
                    #indicamos en qué compás estamos
                    f1.write('compas ')
                    f1.write(str(i))
                    f1.write('\n')

                    f2.write(kern.compas(i))
                    f2.write('\n')                    

                    #duración del compás
                    duration = compass[1]

                    while duration>0:
                        #generamos la nota o el silencio
                        simbolo = symbol.generateSymbol(clef, key, duration, tie, pitch, lastcompass) #SALIDA -> [LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]
                        f1.write(simbolo[0])
                        f1.write('\n')

                        f2.write(kern.simbolo(simbolo[0], clef, key))
                        f2.write('\n')

                        duration = duration - simbolo[1]
                        tie = simbolo[3]
                        pitch = simbolo[2]
                    
                    #cuando se acaba el compás borramos el diccionario temporal de alteraciones
                    dictionary.compass_accidentals.clear()
                
                #fin de los archivos
                f2.write('=')
                f2.write(str(ncompasses+1))
                f2.write('\n')                    
                f2.write('*_')
    
    except:
        print('Error')
        raise

#funcion para elegir la clave a utilizar
def chooseClef():
    #choices para elegir un elemento de la lista clefs -> weigths la probabilidad que tiene cada elemento de ser elegido
    return random.choices(dictionary.clefs, weights=(45, 20, 15, 5, 5, 5, 5), k=1)[0]

#funcion para elegir el tipo de compas
def chooseCompass():
    return random.choices(dictionary.compasses, weights=(50, 25, 12, 5, 2, 2, 2, 2), k=1)[0]
    
#funcion para elegir la tonalidad
def chooseKey():
    return random.choices(dictionary.keys, weights=(42, 10, 8, 6, 4, 1, 1, 1, 1, 1, 1, 4, 6, 8, 10), k=1)[0]

scoreGenerator(nc, numScores)