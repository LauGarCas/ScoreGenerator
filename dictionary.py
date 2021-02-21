'''
###############
CLAVES
###############
'''
#En cada clave hacemos un array de con las 22 alturas absolutas que tiene

clefs = ["clefG2", "clefF4", "clefC3", "clefC1", "clefG1", "clefC2", "clefC4"]

pitches = {
    "clefG2": ['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6'],
    "clefF4": ['G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4'],
    "clefC3": ['F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5'],
    "clefC1": ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6'],
    "clefG1": ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6'],
    "clefC2": ['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5'],
    "clefC4": ['D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5']
}

'''
###############
TONALIDADES
###############
'''
#para cada tonalidad guardamos una lista con las notas absolutas afectadas y la alteración que les corresponde

keys = ["cM", "gM", "dM", "aM", "eM", "bM", "fs", "cs", "cbM", "gbM", "dbM", "abM", "ebM", "bbM", "fM"]

accidentals = {
    "cM": ['', []],
    "gM": ['#', ['F5']],
    "dM": ['#', ['F5', 'C5']],
    "aM": ['#', ['F5', 'C5', 'G5']],
    "eM": ['#', ['F5', 'C5', 'G5', 'D5']],
    "bM": ['#', ['F5', 'C5', 'G5', 'D5', 'A4']],
    "fs": ['#', ['F5', 'C5', 'G5', 'D5', 'A4', 'E5']],
    "cs": ['#', ['F5', 'C5', 'G5', 'D5', 'A4', 'E5', 'B4']],
    "cbM": ['b', ['B4', 'E5', 'A4', 'D5', 'G4', 'C5', 'F4']],
    "gbM": ['b', ['B4', 'E5', 'A4', 'D5', 'G4', 'C5']],
    "dbM": ['b', ['B4', 'E5', 'A4', 'D5', 'G4']],
    "abM": ['b', ['B4', 'E5', 'A4', 'D5']],
    "ebM": ['b', ['B4', 'E5', 'A4']],
    "bbM": ['b', ['B4', 'E5']],
    "fM": ['b', ['B4']]
}

'''
###############
COMPASES
###############
'''
compasses = [("M4/4", 4), ("M3/4", 3), ("M2/2", 4), ("M2/4", 2) , ("M6/8", 3), ("M12/8", 6), ("M9/8", 4.5), ("M5/4", 5)] #métrica de los compases con su duración en negras
