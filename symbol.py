import random

def generateSymbol(duration, tie, pitch, lastcompass):
    #SALIDA -> res = (LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA)
    res = []
    duraciones = [(4, 2, 1, 0.5, 0.25), []]
    alturas = list(range(1,23)) #del 1 al 22

    #si hay una ligadura, el simbolo será seguro una nota
    if tie == 2:
        pesos = [100, 0]
    else:
        pesos = [90, 10]

    #silencio o nota    
    res.append(random.choices(["n", "r"], weights=(pesos), k=1)[0])

    #distribuimos los pesos de la duración del simbolo teniendo en cuenta si caben o no
    for i in range(len(duraciones[0])):
        if duraciones[0][i]>duration:
            duraciones[1].append(0)
        else:
            left = len(duraciones[0])-i
            j = i
            while j < len(duraciones[0]):
                duraciones[1].append(100/left)
                j += 1
            break    

    #definimos la duración
    res.append(random.choices(duraciones[0], weights=(duraciones[1]), k=1)[0])

    #definimos la altura
    '''
    ##############
    IMPLEMENTAR EL ALGORITMO
    ##############
    '''
    if res[0] == 'n': #si es una nota
        res.append(random.choice(alturas))
    else:
        res.append("")

    #definimos alteracion
    '''
    ##############
    QUEDA POR HACER
    ##############
    '''

    #definimos ligadura -> 0 no hay ligadura, 1 se abre ligadura, 2 hay ligadura abierta, 3 se cierra ligadura
    if res[0] == 'n' and tie == 0 and lastcompass==False: #es una nota y NO hay ligadura empezada y no estamos en el último compass
        res.append(random.choices([0,1], weights=(90, 10), k=1)[0])
    elif res[0] == 'n' and tie != 0 and lastcompass==True: #si estamos en el último compás y hay una ligadura abierta se cierra automáticamente
        res.append(3)
    elif res[0] == 'n' and tie != 0: #es una nota y SI hay ligadura empezada
        res.append(random.choices([3,2], weights=(80, 20), k=1)[0])
    else:
        res.append(0)

    #definimos puntillo
    durpunt = res[1] + res[1]/2
    if durpunt <= duration and res[1] > 0.25:   #si es semicorchea no le ponemos puntillo porque se lia un pitote que todavia no se como solucionar
        puntillo =  random.choices([0,1], weights=(90, 10), k=1)[0]
    else:
        puntillo = 0
    
    

    #preparamos la salida
    #SALIDA -> res = (LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA)
    res[0] = str(res[0]) + ' ' + str(res[1]) + ' ' + str(res[2]) + ' '
    if puntillo == 1:
        res[0] += '.'
        res[1] = durpunt #si hay puntillo actualizamos la duración total
    if res[3] == 1:
        res[0] += ' ('
        res[3] = 2 #indica que hay una ligadura empezada
    if res[3] == 3:
        res[0] += ' )'
        res[3] = 0 #si se acaba la ligadura la reiniciamos

    return res