import random
import dictionary

def generateSymbol(clef, key, duration, tie, pitch, lastcompass, compass_accidentals):
    #SALIDA -> res = (LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA, ACORDE)
    res = []
    duraciones = [(4, 2, 1, 0.5, 0.25), []]
    alteracion = '' # b -> bemol, # -> sostenido,  n -> becuadro

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
    if res[0] == 'n': #si es una nota
        nota = randomWalk(pitch)
        res.append(nota)
    else:
        res.append(pitch)

    #definimos si es acorde
    if res[0] == 'n': #si es una nota
        chord = random.choices([0,1], weights=(90, 10), k=1)[0]
    else:
        chord = 0

    #definimos alteracion
    esalterada =  random.choices([0,1], weights=(90, 10), k=1)[0]   # 0 -> no alteración, 1 -> si alteración
    if esalterada == 1 and res[0] == 'n':
        notaAbs = dictionary.pitches[clef][nota - 1]
        alteraciones = dictionary.accidentals[key]

        #La nota ya ha sido alterada previamente en el compás solo podremos cambiar esta alteración por una de las otras dos
        if notaAbs in compass_accidentals:
            #vemos con que estaba alterada
            if compass_accidentals[notaAbs] == '#':
                alteracion = random.choice(['+ ', '- '])
            if compass_accidentals[notaAbs] == '-':
                alteracion = random.choice(['# ', '+ '])
            if compass_accidentals[notaAbs] == '+':
                alteracion = random.choice(['# ', '- '])
        
        #si no ha sido alterada todavia
        else:
            #si la nota aparece alterada en la tonalidad solo podemos cambiar la alteración por una de las otras dos
            if notaAbs[0] in alteraciones[1]:
                alteracion = random.choice(['+', alteraciones[2]])
            else:
                alteracion = random.choice(['#', '-'])

        compass_accidentals[notaAbs] = alteracion
    
    #definimos ligadura -> 0 no hay ligadura, 1 se abre ligadura, 2 hay ligadura abierta, 3 se cierra ligadura
    if res[0] == 'n' and tie == 0 and lastcompass==False: #es una nota y NO hay ligadura empezada y no estamos en el último compass
        res.append(random.choices([0,1], weights=(90, 10), k=1)[0])
    elif res[0] == 'n' and tie != 0 and lastcompass==True and chord != 1: #si estamos en el último compás y no es la primera nota de un acorde y hay una ligadura abierta se cierra automáticamente
        res.append(3)
    elif res[0] == 'n' and tie != 0 and chord != 1: #es una nota, no es la primera nota de un acorde y SI hay ligadura empezada
        res.append(random.choices([3,2], weights=(80, 20), k=1)[0])
    elif res[0] == 'n' and tie != 0 and chord == 1: #es una nota, y es la primera de un acorde, pero ya hay una ligadura empezada
        res.append(2)
    else:
        res.append(0)

    #añado el acorde al final del res
    res.append(chord)

    #definimos puntillo
    durpunt = res[1] + res[1]/2
    if durpunt <= duration and res[1] > 0.25:   #si es semicorchea no le ponemos puntillo porque se lia un pitote que todavia no se como solucionar
        puntillo =  random.choices([0,1], weights=(90, 10), k=1)[0]
    else:
        puntillo = 0

    if chord == 1:  #si hay un acorde tenemos que saber si hay puntillo para ponerselo a las demás notas del acorde
        res.append(puntillo)  

    #preparamos la salida
    #SALIDA -> res = (LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA, ACORDE)
    if res[0] == 'n': #si es una nota lleva altura
        res[0] = str(res[0]) + ' ' + str(res[1]) + ' ' + str(res[2]) + ' ' + alteracion
    else:   #si es un silencio no lleva altura
        res[0] = str(res[0]) + ' ' + str(res[1]) + ' ' 
    
    if puntillo == 1:
        res[0] += ' .'
        if chord != 1:  #si hay acorde la duración que tenemos que pasarle es sin puntillo para que sepa la duración de las demás notas del acorde
            res[1] = durpunt #si hay puntillo actualizamos la duración total
    if res[3] == 1:
        res[0] += ' ('
        #res[3] = 2 #indica que hay una ligadura empezada
    if res[3] == 3:
        res[0] += ' )'
        res[3] = 0 #si se acaba la ligadura la reiniciamos

    return res

def generateChord(clef, key, duration, pitch, dot, tie, compass_accidentals, lastcompass, lastNote): #la duración es la de las demás notas del acorde, y la altura es la altura de la nota anterior del acorde
    #SALIDA -> res = (LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA)    
    res = []
    alteracion = '' # b -> bemol, # -> sostenido,  n -> becuadro

    res.append('n') #será seguro una nota

    res.append(duration)

    #definimos la altura de la nota
    nota = alturaAcorde(pitch, lastNote)
    res.append(nota)

    #definimos alteracion
    esalterada =  random.choices([0,1], weights=(90, 10), k=1)[0]   # 0 -> no alteración, 1 -> si alteración
    if esalterada == 1:
        notaAbs = dictionary.pitches[clef][nota - 1]
        alteraciones = dictionary.accidentals[key]

        #La nota ya ha sido alterada previamente en el compás solo podremos cambiar esta alteración por una de las otras dos
        if notaAbs in compass_accidentals:
            #vemos con que estaba alterada
            if compass_accidentals[notaAbs] == '#':
                alteracion = random.choice(['+ ', '- '])
            if compass_accidentals[notaAbs] == '-':
                alteracion = random.choice(['# ', '+ '])
            if compass_accidentals[notaAbs] == '+':
                alteracion = random.choice(['# ', '- '])
        
        #si no ha sido alterada todavia
        else:
            #si la nota aparece alterada en la tonalidad solo podemos cambiar la alteración por una de las otras dos
            if notaAbs[0] in alteraciones[1]:
                alteracion = random.choice(['+', alteraciones[2]])
            else:
                alteracion = random.choice(['#', '-'])

        compass_accidentals[notaAbs] = alteracion

    #definimos ligadura -> 0 no hay ligadura, 1 se abre ligadura, 2 hay ligadura abierta, 3 se cierra ligadura
    if tie != 0 and lastcompass==True and lastNote==True: #si es la ultima nota de un compás, si hay ligadura abierta y estamos en el úlitmo compás se cierra automaticamente
        res.append(3)
    elif tie != 0 and tie != 1 and lastcompass==False and lastNote==True: #si es la ultima nota de un acorde y en ese acorde no se ha abierto la ligadura, si hay ligadura pero no estamos en el úlitmo compás se puede cerrar o no
        res.append(random.choices([3,2], weights=(80, 20), k=1)[0])
    elif tie == 1:
        res.append(2)
    else:
        res.append(0)
        
    #preparamos la salida
    #SALIDA -> res = (LO QUE SE ESCRIBE, DURACION, ALTURA, LIGADURA)
    res[0] = str(res[0]) + ' ' + str(duration) + ' ' + str(nota) + ' ' + alteracion

    if dot == 1:
        res[0] += ' .'
        if lastNote:
            res[1] = res[1] + res[1]/2
    if res[3] == 1:
        res[0] += ' ('
        res[3] = 2 #indica que hay una ligadura empezada
    if res[3] == 3:
        res[0] += ' )'
        res[3] = 0 #si se acaba la ligadura la reiniciamos

    return res

#metodo de composicion algoritmica randomwalk
def randomWalk(prevpitch):
    paso = random.choice([0, 1, 2]) #el 0 resta 1, el 1 lo deja como esta y el 2 le suma 1
    limite = random.choice([0, 1]) #0 limite absorbente, 1 limite reflectivo

    if paso == 0:
        pitch = int(prevpitch) - 1
        if pitch<0 and limite==0:
            pitch = 0
        if pitch<0 and limite==1:
            pitch += 2
    elif paso == 1:
        pitch = int(prevpitch)
    else:
        pitch = int(prevpitch) + 1
        if pitch>21 and limite==0:
            pitch = 21
        if pitch>21 and limite==1:
            pitch -= 2

    return pitch

    

def alturaAcorde(chordpitch, lastnote):
    #se restan dos alturas de la altura anterior, excepto si no caben que se hacen cosas raras que en mi cabeza tienen sentido
    if lastnote:
        if chordpitch<2:
            if chordpitch<1:
                pitch = chordpitch + 1
            else:
                pitch = chordpitch -1
        else:
            pitch = chordpitch - 2
    else:
        if chordpitch<2:
            pitch = chordpitch + 3
        else:
            pitch = chordpitch -2

    return pitch
