'''
###############
SEPARADORES
###############
'''
separator = ':'
advance = ' + '
not_advance = ' '

'''
###############
NOTAS
###############
'''
positions = ["S-3", "L-2", "S-2", "L-1",  "S-1", "L0", "S0", "L1",  "S1", "L2", "S2", "L3", "S3", "L4", "S4", "L5", "S5", "L6" "S6", "L7", "S7", "L8"]

#S2 es el último con la plica hacia arriba, las lineas/espacios superiores tiene la plica hacia abajo
stem_sep = positions.index("S2") # MARIA: Esto lo tenemos que dejar si o si porque es una norma que siempre se cumple

'''
###############
CLAVES
###############
'''
clefs = {
    "clefG2": ["clef.G:L2", ["L5","S3","S5","L4","S2","S4","L3"], ["L3","S4","S2","L4","L2","S3","S1"]],
    "clefF4": ["clef.F:L4", ["L4","S2","S4","L3","S1","S3","L2"], ["L2","S3","S1","L3","L1","S2","S0"]],
    "clefC3": ["clef.C:L3", ["S4","L3","L5","S3","L2","L4","S2"], ["S2","L4","L2","S3","S1","L3","L1"]],
    "clefC1": ["clef.C:L1", ["S2","L1","L3","S1","S3","L2","L4"], ["L4","L2","S3","S1","L3","L1","S2"]],
    "clefG1": ["clef.G:L1", ["L4","S2","S4","L3","S1","S3","L2"], ["L2","S3","S1","L3","L1","S2","S0"]],
    "clefC2": ["clef.C:L2", ["S3","L2","L4","S2","S4","L3","L5"], ["S1","L3","L1","S2","L4","L2","S3"]],
    "clefC4": ["clef.C:L4", ["L2","L4","S2","S4","L3","L5","S3"], ["S1","L3","L1","S2","L4","L2","S3"]]
}

'''
###############
TONALIDADES
###############
'''
#lo que se escribe, cuantas veces se escribe y el lugar en funcion de la clave, si es sostenido o bemol
accidentalsdic = {
    "cM": [],
    "gM": ['accidental.sharp', 1, 1],
    "dM": ['accidental.sharp', 2, 1],
    "aM": ['accidental.sharp', 3, 1],
    "eM": ['accidental.sharp', 4, 1],
    "bM": ['accidental.sharp', 5, 1],
    "fs": ['accidental.sharp', 6, 1],
    "cs": ['accidental.sharp', 7, 1],
    "cbM": ['accidental.flat' ,7, 2],
    "gbM": ['accidental.flat', 6, 2],
    "dbM": ['accidental.flat', 5, 2],
    "abM": ['accidental.flat', 4, 2],
    "ebM": ['accidental.flat', 3, 2],
    "bbM": ['accidental.flat', 2, 2],
    "fM": ['accidental.flat', 1, 2]
}

def accidentals(k, c):
    res = ''
    if k != "cM":
        simbolo = accidentalsdic[k][0]
        veces = accidentalsdic[k][1] 
        sitios = accidentalsdic[k][2]
        for i in range(veces):
            res += simbolo
            res += separator
            res += clefs[c][sitios][i]
            res += advance
    return res

'''
###############
COMPASES
###############
'''
compasses = {
    "M4/4": "digit.4:L4 digit.4:L2",
    "M3/4": "digit.3:L4 digit.4:L2",
    "M2/2": "digit.2:L4 digit.2:L2",
    "M2/4": "digit.2:L4 digit.4:L2",
    "M6/8": "digit.6:L4 digit.8:L2",
    "M12/8": "digit.12:L4 digit.8:L2",
    "M9/8": "digit.9:L4 digit.8:L2",
    "M5/4": "digit.5:L4 digit.4:L2"
}

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
        return 'verticalLine:L1 + '

def simbolo(linea, clef):
    x = linea.split(" ")

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
    if '-' in x:
        acc = 'accidental.natural' + separator + pos 
        res = acc + advance + res


    return res

def end():
    return 'verticalLine:L1'

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
