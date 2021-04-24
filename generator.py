import random
import os
import symbol
import dictionary
import manager

compass_accidentals = {}
compass_accidentals2 = {}

nc = input("Introduce el número de compases... ")  #Numero de compases
numScores = input("Introduce el número de partituras... ") #numero de partituras
typeagnostic = input("Introduce traducción agnótica standard(0) o split(1)...")
monopoly = input("Indica si las partituras seran monofónicas(0) o polifónicas(1)...")

nc = int(nc)
numScores= int(numScores)

#funcion principal en la que se recogen los parametros y se generan las partituras
def scoreGenerator(ncompasses, nscores):
    for j in range(nscores):
        try:
            #creo las carpeta para las salidas
            path = 'salida'+str(j)
            if not os.path.exists(path):
                os.makedirs(path)
            
            nombrearchivo = 'salida' + str(j) +'.txt'
            with open(os.path.join(path, nombrearchivo), "w") as f1:

                #se elige el tipo de compas
                compass = chooseCompass()
            
                if monopoly == '0': #MONOPHONIC
                    #creo los archivos de salida
                    manager.init(j, path, typeagnostic)
                    #se decide el tipo de clave a utilizar
                    clef = chooseClef()
                    manager.clef(clef)

                    f1.write(clef + '\n')

                    #se elige la tonalidad
                    key = chooseKey()
                    manager.key(key)

                    f1.write(key + '\n')

                    manager.metric(compass)
                    f1.write(compass[0] + '\n')

                    #inicializamos la ligadura y la altura
                    tie = 0
                    pitch = 11 #número entre el 1 y el 22 -> lo podría cambiar por un random
                    #se empiezan a generar compases
                    for i in range(ncompasses):
                        lastcompass = False
                        if i == ncompasses - 1:
                            lastcompass = True

                        #indicamos en qué compás estamos
                        manager.compas(i)

                        f1.write('compas ')
                        f1.write(str(i))
                        f1.write('\n')
            
                        #duración del compás
                        duration = compass[1]

                        while duration>0:
                            #generamos la nota o el silencio
                            simbolo = symbol.generateSymbol(clef, key, duration, tie, pitch, lastcompass, compass_accidentals) #SALIDA -> [LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]

                            #Escribimos el simbolo
                            manager.simbolo(simbolo[0], compass_accidentals)

                            f1.write(simbolo[0])
                            f1.write('\n')
                            
                            duration = duration - simbolo[1]
                            tie = simbolo[3]
                            pitch = simbolo[2]
                        
                        #cuando se acaba el compás borramos el diccionario temporal de alteraciones
                        compass_accidentals.clear()
                    #fin de los archivos
                    manager.end(ncompasses+1)
                elif monopoly == '1': #POLYPHONIC
                    #creo los archivos de salida
                    manager.polyinit(j, path, typeagnostic)
                    #se decide el tipo de clave a utilizar
                    clef = 'clefF4'
                    clef2 = 'clefG2'
                    manager.polyclef(clef, clef2)

                    f1.write(clef + '\t' + clef2 + '\n')

                    #se elige la tonalidad
                    key = chooseKey()
                    manager.polykey(key)

                    f1.write(key + '\t' + key + '\n')

                    manager.polymetric(compass)
                    f1.write(compass[0] + '\t' + compass[0] + '\n')

                    #inicializamos la ligadura y la altura
                    tie1 = 0
                    tie2 = 0
                    pitch1 = 11 #número entre el 1 y el 22 -> lo podría cambiar por un random
                    pitch2 = 11 #número entre el 1 y el 22 -> lo podría cambiar por un random
                    #se empiezan a generar compases
                    for i in range(ncompasses):
                        lastcompass = False
                        if i == ncompasses - 1:
                            lastcompass = True

                        #indicamos en qué compás estamos
                        manager.polycompas(i)

                        f1.write('compas ' + str(i) + '\t' + 'compas ' + str(i) + '\n')
            
                        duration1 = compass[1] #duración del compás en el primer pentagrama
                        duration2 = compass[1] #duración del compás en el segundo pentagrama

                        while duration1>0 or duration2>0: #mientras haya espacio en alguno de los dos pentagramas
                            if duration1 == duration2: #hay la misma duración en los dos pentagramas
                                #generamos la nota o el silencio para cada uno de los compases
                                simbolo1 = symbol.generateSymbol(clef, key, duration1, tie1, pitch1, lastcompass, compass_accidentals) #SALIDA -> [LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]
                                simbolo2 = symbol.generateSymbol(clef2, key, duration2, tie2, pitch2, lastcompass, compass_accidentals2) #SALIDA -> [LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]
                                
                                #Escribimos el simbolo
                                manager.polysimbolo(simbolo1[0], simbolo2[0], compass_accidentals, compass_accidentals2)

                                f1.write(simbolo1[0] + '\t' + simbolo2[0] + '\n')
                           
                                #actualizamos las duraciones
                                duration1 = duration1 - simbolo1[1]
                                duration2 = duration2 - simbolo2[1]
                                                        
                                tie1 = simbolo1[3]
                                tie2 = simbolo2[3]
                                pitch1 = simbolo1[2]
                                pitch2 = simbolo2[2]
                            else: #uno de los dos pentagramas va mas adelantado que el otro
                                if duration1<duration2: #El primer pentagrama va más adelantado
                                    simbolo2 = symbol.generateSymbol(clef2, key, duration2, tie2, pitch2, lastcompass, compass_accidentals2) #SALIDA -> [LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]
                                    
                                    #Escribimos el simbolo
                                    manager.polysimbolo('.', simbolo2[0], '', compass_accidentals2)
                                    f1.write('nada' + '\t' + simbolo2[0] + '\n')
                                    
                                    #Actualizamos las duraciones
                                    duration2 = duration2 - simbolo2[1]

                                    tie2 = simbolo2[3]
                                    pitch2 = simbolo2[2]
                                    
                                else: #El segundo pentagrama va mas adelantado
                                    simbolo1 = symbol.generateSymbol(clef, key, duration1, tie1, pitch1, lastcompass, compass_accidentals) #SALIDA -> [LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA]
                                    
                                    #Escribimos el simbolo
                                    f1.write(simbolo1[0] + '\t' + 'nada' + '\n')
                                    manager.polysimbolo(simbolo1[0], '.', compass_accidentals, '')
                                        
                                    #actualizamos las duraciones
                                    duration1 = duration1 - simbolo1[1]

                                    tie1 = simbolo1[3]
                                    pitch1 = simbolo1[2]                             
                        
                        #cuando se acaba el compás borramos el diccionario temporal de alteraciones
                        compass_accidentals.clear()
                        compass_accidentals2.clear()
                
                    #fin de los archivos
                    manager.polyend(ncompasses+1, path)
        except:
            print('Error')
            raise

        finally:
            manager.close()
                
    
        

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