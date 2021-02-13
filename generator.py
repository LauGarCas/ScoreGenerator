import random

ncompasses = input("Introduce el número de compases... ")  #Numero de compases
numOfGenerations = input("Introduce el número de partituras... ") #creo que es el numero de partituras jj

clefs = ["clefG2", "clefF4", "clefC3", "clefC1", "clefG1", "clefC2", "clefC4"]
compasses = ["M4/4", "M3/4", "M2/2", "M2/4", "M6/8", "M12/8", "M9/8", "M5/4"]
keys = ["cM", "gM", "dM", "lM", "eM", "bM", "cbm", "gbm", "fsm", "dbm", "csm", "lbM", "ebM", "bbM", "fM"]

#funcion principal en la que se recogen los parametros y se generan las partituras
def scoreGenerator(ncompasses):
    try:
        #creamos los archivos
        with open("salida.txt", "w") as f1:

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
            f1.write(compass)
            f1.write('\n')

            #numero de compases -> ncompas

            #tipo de funcion para la generacion de la partitura -> tipofunc

            #se empiezan a generar compases
    except:
        print('Error')
        raise

#funcion para elegir la clave a utilizar
def chooseClef():
    #choices para elegir un elemento de la lista clefs -> weigths la probabilidad que tiene cada elemento de ser elegido
    return random.choices(clefs, weights=(45, 20, 15, 5, 5, 5, 5), k=1)

#funcion para elegir el tipo de compas
def chooseCompass():
    return random.choices(compasses, weights=(50, 25, 12, 5, 2, 2, 2, 2), k=1)
    
#funcion para elegir la tonalidad
def chooseKey():
    return random.choices(keys, weights=(42, 10, 8, 6, 4, 1, 1, 1, 1, 1, 1, 4, 6, 8, 10), k=1)