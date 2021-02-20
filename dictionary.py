'''
###############
CLAVES
###############
'''
clefs = ["clefG2", "clefF4", "clefC3", "clefC1", "clefG1", "clefC2", "clefC4"]

#clave = en cada clave hacemos un array de con 22 elementos(uno por altura) y en cada altura podemos indicar la altura absoluta a la que corresponde

clefG2 = {}

clefF4 = {}

clefC3 = {}

clefC1 = {}

clefG1 = {}

clefC2 = {}

clefC4 = {}



'''
###############
TONALIDADES
###############
'''
keys = ["cM", "gM", "dM", "lM", "eM", "bM", "cbm", "gbm", "fsm", "dbm", "csm", "lbM", "ebM", "bbM", "fM"]

#para cada tonalidad podemos guardar un array con las alturas absolutas que se encuentran alteradas en cada tonalidad, entonces luego al poner las alturas, con un find en este array de la altura podemos ver si está alterada o no

cM = {}