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
    "gM": ['#', ['F'], '-'],
    "dM": ['#', ['F', 'C'], '-'],
    "aM": ['#', ['F', 'C', 'G'], '-'],
    "eM": ['#', ['F', 'C', 'G', 'D'], '-'],
    "bM": ['#', ['F', 'C', 'G', 'D', 'A'], '-'],
    "fs": ['#', ['F', 'C', 'G', 'D', 'A', 'E'], '-'],
    "cs": ['#', ['F', 'C', 'G', 'D', 'A', 'E', 'B'], '-'],
    "cbM": ['-', ['B', 'E', 'A', 'D', 'G', 'C', 'F'], '#'],
    "gbM": ['-', ['B', 'E', 'A', 'D', 'G', 'C'], '#'],
    "dbM": ['-', ['B', 'E', 'A', 'D', 'G'], '#'],
    "abM": ['-', ['B', 'E', 'A', 'D'], '#'],
    "ebM": ['-', ['B', 'E', 'A'], '#'],
    "bbM": ['-', ['B', 'E'], '#'],
    "fM": ['-', ['B'], '#']
}

#diccionario para guardar las alteraciones que se dan en cada compás

'''
###############
COMPASES
###############
'''
compasses = [("M4/4", 4), ("M3/4", 3), ("M2/2", 4), ("M2/4", 2) , ("M6/8", 3), ("M12/8", 6), ("M9/8", 4.5), ("M5/4", 5)] #métrica de los compases con su duración en negras
