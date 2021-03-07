separator = ':'
advance = ' + '
not_advance = ' '

# MARIA: La codificación agnóstica tiene dos reglas principales:
# (1) TODOS los simbolos se codifican siguiendo una estructura de dos partes diferenciadas: 
# <forma:posicionenelpentagrama>
# Por ejemplo un negra de D04 en clave de SOL2 sería -> note.quarter:L0
#(2) Se lee de izquierda a derecha y de arriba abajo, y eso se simboliza con el caracter advance. 
# Se separa la traducción individual de cada simbolo por ese caracterter de manera que:
#  note.quarter:L0 + rest.half:L2 -> son un nota que van una detras de otra
#  digit.4:L4 digit.4:L2 -> son los número de compas los cuales estan en uno encima de otro
# Imagina que el pentagrama es un plano XY, y el eje X es el como nos desplazamos para leer la partitura
# y el eje Y es el alto de la partitura. Pues los números de compás se encuentran en la misma posición horizontal,
# el mismo valor de X, pero en distinto valor de Y, y eso se simboliza dejando un espacio entre ellos. No utilizamos
# el caracter de advance porque no tenemos que avanzar, sino leer ambos juntos. Mientras que en los otros dos si avanzamos 
# en la lectura. Espero haberme explicado bien!

# Las posiciones son todas relativas a las líneas y espacios del pentagrama. La foto que te he adjuntado
# es un esquema de como se cuentan.

# 


'''
###############
CLAVES
###############
'''
clefs = {
    "clefG2": "clef.G:L2",
    "clefF4": "clef.F:L4",
    "clefC3": "clef.C:L3",
    "clefC1": "clef.C:L1",
    "clefG1": "clef.G:L1",
    "clefC2": "clef.C:L2",
    "clefC4": "clef.C:L4"
}

'''
###############
TONALIDADES
###############
'''
# MARIA
# Esto no se como podemos abordarlo sin utilizar un pedazo de dict.
# El problema es que dependiendo de la clave las alteraciones de las tonalidades aparecen en una posicion u otra.
# Entonces lo que se me ocurre es que tal vez podamos guardar solo la posicion relativa a la clave de sol en linea dos,
# apoyandonos en el vector positions y luego modificar eso en funcion de un offset.
# Te pongo un ejemplo:

# Bemoles
# clefG2{"L3","S4","S2","L4","L2","S3","S1"} -> Source
# clefF4{"L2","S3","S1","L3","L1","S2","S0"} -> Mantiene L y S pero el número es uno menos. 
# Esto es un offset = -2 (en posiciones relativas del pentagrama)
# Estás en L3 y tienes un offeset de -1, bajas a la siguiente posicion del pentagrama que es S2.
# clefC3{"S2","L4","L2","S3","S1","L3","L1"} -> Offset = -1
# clefC1{"L4","L2","S3","S1","L3","L1","S2"} -> Offset = +2
# clefG1{"L2","S3","S1","L3","L1","S2","S0"} -> Igual que clefF4. Offset = -2
# clefC2{"S1","L3","L1","S2","L4","L2","S3"} -> Offset = -3
# clefC4{"S3","L5","L3","S4","S2","L4","L2"} -> Offset = +1

# Sostenidos
# clefG2{"L5","S3","S5","L4","S2","S4","L3"} -> Source
# clefF4{"L4","S2","S4","L3","S1","S3","L2"} -> Offset = -2
# clefC3{"S4","L3","L5","S3","L2","L4","S2"} -> Offset = -1
# clefC1{"S2","L1","L3","S1","S3","L2","L4"} -> Offset = -5
# clefG1{"L4","S2","S4","L3","S1","S3","L2"} -> Offset = -2
# clefC2{"S3","L2","L4","S2","S4","L3","L5"} -> Offset = -3
# clefC4{"L2","L4","S2","S4","L3","L5","S3"} -> Offset = -6

# Nos guardamos un vector que sea [0, 2, 5, etc] que sea la posicion que ocupa las lineas de las alteraciones 
# dentro del vector positions y entonces vamos modificacion esas posiciones con los offset para obtener las lineas/espacios necesarios
# No se si me he explicado bien jeje Al igual que si tienes otra idea feel free!


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

'''
###############
NOTAS
###############
'''
positions = ["S-3", "L-2", "S-2", "L-1",  "S-1", "L0", "S0", "L1",  "S1", "L2", "S2", "L3", "S3", "L4", "S4", "L5", "S5", "L6" "S6", "L7", "S7", "L8"]
#S2 es el último con la plica hacia arriba, las lineas/espacios superiores tiene la plica hacia abajo
stem_sep = positions.index("S2")



def compas(n):
    if n == 0:
        return ''
    else:
        return 'verticalLine:L1'

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
    # MARIA
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