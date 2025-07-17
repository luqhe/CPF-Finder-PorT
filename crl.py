from seleniumwire import webdriver

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

import json, gzip
from io import BytesIO

driver = webdriver.Chrome()
driver.scopes = ['https://portaldatransparencia.gov.br/pessoa-fisica/busca/resultado?.*']

def gzipdecode(response):
    with gzip.GzipFile(fileobj=BytesIO(response.body)) as f:
        return f.read().decode('utf-8')

def getJson(cpf):
    del driver.requests
    driver.get(f'https://portaldatransparencia.gov.br/pessoa-fisica/busca/lista?termo={cpf}')
    
    responses = []
    def waitCheck(d):
        nonlocal responses
        for r in d.requests:
            if r.response and r.response.headers.get('content-type') == 'application/json':
                responses.append(r.response)

        return any(responses)

    try:
        WebDriverWait(driver, timeout=60).until(waitCheck)
    except TimeoutException:
        return [None], cpf

    f_paths = []
    for i, r in enumerate(responses):
        if r.headers.get('content-type') == 'application/json':
            json_data = json.loads(gzipdecode(r))
    
            f_path = f'./responses/{i}.json'
            with open(f_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
            f_paths.append(f_path)

    return f_paths, cpf
