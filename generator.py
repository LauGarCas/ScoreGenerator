import random
import symbol


nc = input("Introduce el número de compases... ")  #Numero de compases
numScores = input("Introduce el número de partituras... ") #numero de partituras

nc = int(nc)
numScores= int(numScores)

clefs = ["clefG2", "clefF4", "clefC3", "clefC1", "clefG1", "clefC2", "clefC4"]
compasses = [("M4/4", 4), ("M3/4", 3), ("M2/2", 4), ("M2/4", 2) , ("M6/8", 3), ("M12/8", 6), ("M9/8", 4.5), ("M5/4", 5)] #métrica de los compases con su duración en negras
keys = ["cM", "gM", "dM", "lM", "eM", "bM", "cbm", "gbm", "fsm", "dbm", "csm", "lbM", "ebM", "bbM", "fM"]

#funcion principal en la que se recogen los parametros y se generan las partituras
def scoreGenerator(ncompasses, nscores):
    try:
        for j in range(nscores):
            nombrearchivo = 'salida' + str(j) +'.txt'
            #creamos los archivos
            with open(nombrearchivo, "w") as f1:

                #se decide el tipo de clave a utilizar
                clef = chooseClef()
                f1.write(clef)
                f1.write('\n')

                #se elige la tonalidad
                key = chooseKey()
                f1.write(key)
                f1.write('\n')

                #se elige el tipo de compas
                compass = chooseCompass()
                f1.write(compass[0])
                f1.write('\n')

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

                    #duración del compás
                    duration = compass[1]

                    while duration>0:
                        #generamos la nota o el silencio
                        simbolo = symbol.generateSymbol(duration, tie, pitch, lastcompass) #->[LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]
                        f1.write(simbolo[0])
                        f1.write('\n')

                        duration = duration - simbolo[1]
                        tie = simbolo[3]
                        pitch = simbolo[2]
    
    except:
        print('Error')
        raise

#funcion para elegir la clave a utilizar
def chooseClef():
    #choices para elegir un elemento de la lista clefs -> weigths la probabilidad que tiene cada elemento de ser elegido
    return random.choices(clefs, weights=(45, 20, 15, 5, 5, 5, 5), k=1)[0]

#funcion para elegir el tipo de compas
def chooseCompass():
    return random.choices(compasses, weights=(50, 25, 12, 5, 2, 2, 2, 2), k=1)[0]
    
#funcion para elegir la tonalidad
def chooseKey():
    return random.choices(keys, weights=(42, 10, 8, 6, 4, 1, 1, 1, 1, 1, 1, 4, 6, 8, 10), k=1)[0]


scoreGenerator(nc, numScores)