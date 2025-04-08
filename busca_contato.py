
#para controlar o navegador
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


#FAZ A PESQUISA DO CONTATO OU GRUPO PELO NOME
def busca_contato(dfnome, navegador):
    campo_pesquisa = navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div[1]/div[2]/div/div/div/p')
    campo_pesquisa.click()
    time.sleep(1)
    campo_pesquisa.send_keys(dfnome)
    time.sleep(1)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button/span').click()
    time.sleep(1)