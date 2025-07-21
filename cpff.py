from crl import getJson
from cpfgen import generate
from filter import verify
import shutil
import json
import time

def jsonCall(key):
    jsonPath = getJson(key)[0][0]
        
    if jsonPath is None:
        time.sleep(60)
        return jsonCall(key)
    return jsonPath

#def checkJson(file_path):
#    with open(file_path, 'r') as f:
#        data = json.load(f)
#        return data.get('totalRegistros')

name = input()
jsonPath = jsonCall(name)

with open(jsonPath, 'r') as f: data = json.load(f)
reg = data.get('registros')

cpfNis = reg[0].get('cpfNis')

idtype, id = cpfNis.split()
if idtype == 'NIS': raise TypeError('ID tipo NIS, deveria ser CPF')

id = ''.join(c for c in id if c.isalnum())

genfile_path = generate(id)

with open(genfile_path, 'r') as f:
    cpf = f.readline().strip()
    while cpf:
        print(cpf)

        jsonPath = jsonCall(cpf)
        if verify(jsonPath, name):
            shutil.copyfile(jsonPath, f'saves/{cpf}.json')
            print('bingo!')
            break

        cpf = f.readline().strip()
