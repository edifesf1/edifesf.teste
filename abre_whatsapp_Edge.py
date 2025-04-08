import continua_sair

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

def abre_whatsapp():
    try:        
        #servico = Service(EdgeChromiumDriverManager().install())
        #navegador = webdriver.Edge(service=servico)
        navegador = webdriver.Edge(EdgeChromiumDriverManager().install())
        navegador.get("https://web.whatsapp.com")
        while len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[2]')) < 1:
            pass
            time.sleep(5)
        #continua_sair.continua_sair(navegador, linkp)
    except:
        return("erro")
