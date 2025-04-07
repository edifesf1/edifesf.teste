import continua_sair

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import time

def abre_whatsapp(linkp):
    print("cheguei")
    varservice = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=varservice)
    navegador.get("https://www.google.com/")
    exit()
    navegador.get("https://web.whatsapp.com")
    time.sleep(6)
