import dictionary

'''
###############
CLAVES
###############
'''
clefs = {
    "clefG2": "*clefG2",
    "clefF4": "*clefF4",
    "clefC3": "*clefC3",
    "clefC1": "*clefC1",
    "clefG1": "*clefG1",
    "clefC2": "*clefC2",
    "clefC4": "*clefC4"
}

'''
###############
TONALIDADES
###############
'''
accidentals = {
    "cM": "*k[]",
    "gM": "*k[f#]",
    "dM": "*k[f#c#]",
    "aM": "*k[f#c#g#]",
    "eM": "*k[f#c#g#d#]",
    "bM": "*k[f#c#g#d#a#]",
    "fs": "*k[f#c#g#d#a#e#]",
    "cs": "*k[f#c#g#d#a#e#b#]",
    "fM": "*k[b-]",
    "bbM": "*k[b-e-]",
    "ebM": "*k[b-e-a-]",
    "abM": "*k[b-e-a-d-]",
    "dbM": "*k[b-e-a-d-g-]",
    "gbM": "*k[b-e-a-d-g-c-]",
    "cbM": "*k[b-e-a-d-g-c-f-]"
}

'''
###############
COMPASES
###############
'''

compasses = {
    "M4/4": "*M4/4",
    "M3/4": "*M3/4",
    "M2/2": "*M2/2",
    "M2/4": "*M2/4",
    "M6/8": "*M6/8",
    "M12/8": "*M12/8",
    "M9/8": "*M9/8",
    "M5/4": "*M5/4"
}

'''
###############
DURACIONES
###############
'''

durations = {
    "4": "1",
    "2": "2",
    "1": "4",
    "0.5": "8",
    "0.25": "16"
}

def compas(n):
    if n == 0:
        return '=1-'
    else:
        return '=' + str(n+1)

def simbolo(linea, clef, key):
    x = linea.split(" ")

    #primero escribimos la duración
    res = durations[x[1]]

    #si hay puntillo lo escribimos
    if '.' in x:
        res+= '.'

    #traducimos la altura de la nota o el silencio
    if x[0] == 'n':
        notaAbs = dictionary.pitches[clef][int(x[2])-1]
        if int(notaAbs[1]) < 4:
            for i in range(4 - int(notaAbs[1])):
                res += notaAbs[0]
        else:
            nota = notaAbs[0].lower()
            for i in range(int(notaAbs[1])-4 + 1):
                res += nota

        #si hay alguna alteracion la añadimos
        #en kern las alteraciones se escriben segun se tocan no segun se escriben en la partitura
        if '#' in x:
            res+= '#'
        elif '-' in x:
            res+= '-'
        elif '+' in x:
            res+= 'n'
        else:
            notaAbs = dictionary.pitches[clef][int(x[2])-1]
            alteraciones = dictionary.accidentals[key]
            if notaAbs in dictionary.compass_accidentals:
                if dictionary.compass_accidentals[notaAbs] == '#':
                    res+= '#'
                if dictionary.compass_accidentals[notaAbs] == '-':
                    res+= '-'
                if dictionary.compass_accidentals[notaAbs] == '+':
                    res+= 'n'
            elif notaAbs[0] in alteraciones[1]:
                if alteraciones[0] == '#':
                    res+= '#'
                if alteraciones[0] == '-':
                    res+= '-'
                if alteraciones[0] == '+':
                    res+= 'n'

        #si hay ligadura la añadimos
        if '(' in x:
            res = '(' + res

        if ')' in x:
            res+= ')'
    
    if x[0] == 'r':
        res += 'r'
    return res