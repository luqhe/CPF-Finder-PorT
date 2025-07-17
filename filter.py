import os
import json

path = os.fsencode('./saves/')

for fn in os.listdir(path):
    fp = os.path.join(path, fn)
    with open(fp, 'r') as fj:
        jsonFile = json.load(fj)
        reg = jsonFile.get('registros')

        if reg[0].get('nome') == 'NOME COMPLETO': print(os.fsdecode(fp))
