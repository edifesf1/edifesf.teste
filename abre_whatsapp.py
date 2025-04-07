import continua_sair

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def abre_whatsapp(linkp):
    try:
        navegador = webdriver.Chrome()
        navegador.get("https://web.whatsapp.com")
        while len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[2]')) < 1:
            pass
            time.sleep(5)
        continua_sair.continua_sair(navegador, linkp)
    except:
        return("erro")
