from crl import getJson
import shutil
import json
import time

def checkJson(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data.get('totalRegistros')

with open('gen file_path', 'r') as f:
    cpf = f.readline().strip()
    while cpf:
        print(cpf)
        jsonPath = getJson(cpf)[0][0]
        
        if jsonPath is None:
            time.sleep(60)
            continue

        if checkJson(jsonPath):
            shutil.copyfile(jsonPath, f'saves/{cpf}.json')
            print('bingo!')

        cpf = f.readline().strip()
