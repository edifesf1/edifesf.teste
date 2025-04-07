import continua_sair

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import time

def abre_whatsapp(linkp):
    try:
        varservice = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=varservice)
        navegador.get("https://web.whatsapp.com")
        while len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[2]')) < 1:
            pass
            time.sleep(5)
        continua_sair.continua_sair(navegador, linkp)
    except:
        return("erro")
