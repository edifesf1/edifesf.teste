import continua_sair

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def abre_whatsapp(linkp):
    try:
        navegador = webdriver.Chrome()
        navegador.get("https://web.whatsapp.com")
        time.sleep(10)
        #continua_sair.continua_sair(navegador, linkp)
    except:
        navegador = webdriver.Chrome()
        navegador.get("https://web.whatsapp.com")
