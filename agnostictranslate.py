import dictionary

'''
###############
SEPARADORES
###############
'''
advance = ' + '
not_advance = ' '

def valueSeparator(typeagnostic):
    global separator
    if typeagnostic == '0':   
        separator = ':'
    elif typeagnostic == '1':
        separator = ' '

'''
###############
POSICIONES
###############
'''
positions = ["S-3", "L-2", "S-2", "L-1", "S-1", "L0", "S0", "L1", "S1", "L2", "S2", "L3", "S3", "L4", "S4", "L5", "S5", "L6", "S6", "L7", "S7", "L8"]

#S2 es el último con la plica hacia arriba, las lineas/espacios superiores tiene la plica hacia abajo
stem_sep = positions.index("S2") # MARIA: Esto lo tenemos que dejar si o si porque es una norma que siempre se cumple

'''
###############
CLAVES
###############
'''
clefsdic = {
    "clefG2": ["clef.G","L2", ["L5","S3","S5","L4","S2","S4","L3"], ["L3","S4","S2","L4","L2","S3","S1"]],
    "clefF4": ["clef.F","L4", ["L4","S2","S4","L3","S1","S3","L2"], ["L2","S3","S1","L3","L1","S2","S0"]],
    "clefC3": ["clef.C","L3", ["S4","L3","L5","S3","L2","L4","S2"], ["S2","L4","L2","S3","S1","L3","L1"]],
    "clefC1": ["clef.C","L1", ["S2","L1","L3","S1","S3","L2","L4"], ["L4","L2","S3","S1","L3","L1","S2"]],
    "clefG1": ["clef.G","L1", ["L4","S2","S4","L3","S1","S3","L2"], ["L2","S3","S1","L3","L1","S2","S0"]],
    "clefC2": ["clef.C","L2", ["S3","L2","L4","S2","S4","L3","L5"], ["S1","L3","L1","S2","L4","L2","S3"]],
    "clefC4": ["clef.C","L4", ["L2","L4","S2","S4","L3","L5","S3"], ["S1","L3","L1","S2","L4","L2","S3"]]
}

def clefs(c):
    res = clefsdic[c][0]+separator+clefsdic[c][1]
    return res

'''
###############
TONALIDADES
###############
'''
accidentalsdic = {"#":["accidental.sharp", 2], "-":["accidental.flat", 3]} 

def accidentals(k, c): 
    res = ''
    tipo = dictionary.accidentals[k][0] # returns "#" or "-"
    if k != "cM": 
        simbolo = accidentalsdic[tipo][0] 
        veces = len(dictionary.accidentals[k][1]) 
        sitios = accidentalsdic[tipo][1] 
        for i in range(veces): 
            res += simbolo 
            res += separator
            res += clefsdic[c][sitios][i] 
            res += advance 
    return res

'''
###############
COMPASES
###############
'''
m_c = ["digit", "L4", "L2"]  #nuevo dict

# ex: c = "M4/4"
# >> c = "M4/4"
# >> list(c)
# >> ['M', '4', '/', '4']
def compass(c):
    c_list = list(c)
    res = m_c[0] + '.' + c_list[1] + separator + m_c[1] + not_advance + m_c[0] + '.' + c_list[3] + separator + m_c[2]
    return res


'''
###############
DURACIONES
###############
'''
durations = {
    "4": "whole",
    "2": "half",
    "1": "quarter",
    "0.5": "eighth",
    "0.25": "sixteenth"
}

def compas(n):
    if n == 0:
        return ''
    else:
        return 'verticalLine'+separator+'L1 + '

def simbolo(linea, clef):
    x = linea.split(" ")
    if x[0]!= '.':

        #vemos si es una nota o un silencio
        if x[0] == 'n':
            res = 'note.'
        else:
            res = 'rest.'

        #escribimos la duración
        res += durations[x[1]]

        #traducimos la altura de la nota o el silencio
        if x[0] == 'n':
            notaAbs = int(x[2])-1
            if notaAbs > stem_sep:
                res += '_down'
            else: 
                res += '_up'
            pos = positions[notaAbs]  
        else:
            pos = 'L3'
            if durations[x[1]] == 'whole':
                pos = 'L4' #solo el silencio de redonda
        res += separator + pos    


        #si hay ligadura la añadimos
        # Las ligaduras se traducen su principio y fin de ligura
        # Principio -> slur.start:posiciondelanotaqueacompaña
        # Fin -> slur.end:posiciondelanotaqueacompaña
        # Por tanto, aparecen en la misma posición horizontal que la nota (van separadas por un espacio en blanco)
        # Si la plica de la nota está para abajo, la ligadura va encima de la nota
        # Si la plica de la nota está para arriba, la ligadura va debajo de la nota
        # Hay que llevar el orden en cuenta para poner primero una cosa u otra como en las alteraciones
        if '(' in x:
            slur = 'slur.start' + separator + pos
        if ')' in x:
            slur = 'slur.end' + separator + pos
        if '(' in x or ')' in x:
            if int(x[2])-1 > stem_sep:
                #down  
                res = slur + not_advance + res
            else:
                #up
                res += not_advance + slur


        #si hay puntillo lo escribimos
        if '.' in x:
            #el puntillo SIEMPRE va en un espacio
            #si la posición de una nota es una línea el puntillo aparece en el espacio que queda arriba de la línea
            if pos[0] == 'L':
                pos_dot = 'S' + pos[1:]
            else:
                pos_dot = pos
            res += advance + 'dot' + separator + pos_dot

        #si hay alguna alteracion la añadimos
        if '#' in x:
            acc = 'accidental.sharp' + separator + pos
            #las alteraciones aparecen a la derecha del simbolo
            res = acc + advance + res 
        if '-' in x:
            acc = 'accidental.flat' + separator + pos
            res = acc + advance + res
        if '+' in x:
            acc = 'accidental.natural' + separator + pos 
            res = acc + advance + res

    else:
        res = ''

    return res

def acorde(notas, clef):
    numPlicas = 0
    hayLigaduraInicio=False
    hayLigaduraFin=False
    alturas = []
    alteraciones = []
    puntillos = []
    res = ''
    for index, linea in enumerate(notas):
        x = linea.split(" ")
        if x[0]!= '.':
            
            #como es un acorde será siempre una nota
            res += 'note.'

            #escribimos la duración
            res += durations[x[1]]

            #traducimos la altura de la nota
            notaAbs = int(x[2])-1
            if notaAbs > stem_sep:
                numPlicas += 1
                res += '_down'
            else: 
                res += '_up'
            pos = positions[notaAbs]  

            res += separator + pos    

            #si hay puntillo lo escribimos
            if '.' in x:
                #el puntillo SIEMPRE va en un espacio
                #si la posición de una nota es una línea el puntillo aparece en el espacio que queda arriba de la línea
                if pos[0] == 'L':
                    pos_dot = 'S' + pos[1:]
                else:
                    pos_dot = pos
                puntillos.append('dot' + separator + pos_dot)

            if index!=len(notas)-1:
                res += not_advance

            #si hay ligadura indicamos si es el principio o el final de una
            if '(' in x:
                hayLigaduraInicio = True
            if ')' in x:
                hayLigaduraFin = True    

            #si hay alguna alteracion la añadimos al diccionario para escribirlas todas al final en el orden correspondiente
            if '#' in x:
                alturas.append(notaAbs)
                alteraciones.append('accidental.sharp')
            elif '-' in x:
                alturas.append(notaAbs)
                alteraciones.append('accidental.flat')
            elif '+' in x:
                alturas.append(notaAbs)
                alteraciones.append('accidental.natural')
            else:
                alturas.append(notaAbs)
                alteraciones.append('')
                
        else:
            res = ''

    #si hay ligadura la escribimos o al principio o al final del acorde en función del número de plicas que haya hacia abajo
    if numPlicas>1 and (hayLigaduraInicio or hayLigaduraFin):
        notaAbs = min(alturas)
        pos = positions[notaAbs]
        if hayLigaduraInicio:
            slur = 'slur.start' + separator + pos
        
        if hayLigaduraFin:
            slur = 'slur.end' + separator + pos

        res = slur + not_advance + res
    elif numPlicas<=1 and (hayLigaduraInicio or hayLigaduraFin):
        notaAbs = max(alturas)
        pos = positions[notaAbs]
        if hayLigaduraInicio:
            slur = 'slur.start' + separator + pos
        
        if hayLigaduraFin:
            slur = 'slur.end' + separator + pos

        res += not_advance + slur

    #si hay puntillos los escribimos
    if len(puntillos)>0:
        res += advance
        for index in range(len(puntillos)):
            if puntillos[index]!='':
                if index == len(puntillos)-1:
                    res += puntillos[index]
                else:
                    res += puntillos[index] + not_advance
    else:
        res += advance

    #si hay alteraciones las escribimos
    #busco la nota más aguda que su alteración iria la ultima
    acc = ''
    notaAbs = min(alturas)
    indice = alturas.index(notaAbs)
    if(alteraciones[indice] != ''):
        acc +=alteraciones[indice] + separator + positions[notaAbs]
    alturas.pop(indice)
    alteraciones.pop(indice)
    #busco la nota mas grave que será la siguiente a la aguda
    notaAbs = min(alturas)
    indice = alturas.index(notaAbs)
    if(alteraciones[indice] != ''):
        if acc!='':
            acc = not_advance + alteraciones[indice] + separator + positions[notaAbs] + not_advance + acc
        else:
            acc += alteraciones[indice] + separator + positions[notaAbs]
    alturas.pop(indice)
    alteraciones.pop(indice)
    #si queda una nota mas en los acordes va la primera
    if len(alturas)>0:
        notaAbs = min(alturas)
        indice = alturas.index(notaAbs)
        if(alteraciones[indice] != ''):
            if acc!='':
                acc =  alteraciones[indice] + separator + positions[notaAbs] + not_advance + acc
            else:
                acc += alteraciones[indice] + separator + positions[notaAbs]
        alturas.pop(indice)
        alteraciones.pop(indice)
    if acc!='':
        res = acc + advance + res
    
    return res

def end():
    return 'verticalLine'+separator+'L1'

# MARIA
# La traducción agnóstica que estamos sacando está en la forma standard, porque forma:posición
# son un mismo símbolo, un mismo string de caracteres. Sin embargo, en las últimas pruebas
# que hemos hecho con los modelos de OMR hemos empezado a obtener también buenos resultados
# si tenemos la traducción en la forma split, es decir, una traducción donde forma y posición 
# son strings de caracteres separados, uno tras otro, y sin hacer uso del separador ':'. 
# Entonces he pensado que en vez de guardar en cada símbolo su forma y su posición
# lo más fácil es añadir un input que pregunte que como se quiere  la traducción agnóstica 
# si en su forma standard o en su forma split, y si se dice split, se traduce en standard 
# y una vez que se tiene el entero de la standard, se lee y se podría hacer algo así:

# symbols = []
# with open(traduccion, 'r') as txt:
    # symbols.extend(txt.read().split(not_advance))

# with open(split, "w") as txt:
    # for s in symbols:
        # split_sym = advance
        # if s != advance:
            # split_sym = s.split(':')[0] + not_advance + s.split(':')[1]
        # txt.write(split_sym)

# Lo he escrito rapidisimo así que igual que a esto revisa todo por si he metido la gamba!
