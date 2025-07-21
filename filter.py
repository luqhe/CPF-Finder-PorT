import os
import json
from unidecode import unidecode

def verify(fp, n):
    n = unidecode(n).upper()
    with open(fp, 'r') as fj:
        jsonFile = json.load(fj)
        reg = jsonFile.get('registros')
    
        if jsonFile.get('totalRegistros') != 0 and reg[0].get('nome') == f'{n}': return 1
        else: return 0

path = os.fsencode('./saves/')
def json_path(name):
    for fn in os.listdir(path):
        fp = os.path.join(path, fn)
        
        if verify(fp, name): return os.fsdecode(fp)
