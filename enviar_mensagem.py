
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import verifica_midia


#ENVIA MENSAGEM DE TEXTO
def enviar_mensagem(dfmensagem, dfmidia, navegador):
    campo_mensagem = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[3]/div[1]/p')
    time.sleep(1)
    campo_mensagem.send_keys(dfmensagem)
    
    #VERIFICA SE A MIDIA EXISTE
    dfmidia = verifica_midia.verifica_midia(dfmidia)

    #SE A MIDIA FOR INVALIDA ENVIA A MENSAGEM E ENCERRA A FUNÇÃO
    if dfmidia == "sem":
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[3]/div[1]/p').send_keys(Keys.ENTER)
        return()
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button/span').click()
    time.sleep(1)
    navegador.find_element(By.CSS_SELECTOR, "input[accept='image/*,video/mp4,video/3gpp,video/quicktime']").send_keys(dfmidia)
    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
    time.sleep(5)