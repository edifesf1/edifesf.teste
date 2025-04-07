import continua_sair

from playwright.sync_api import sync_playwright
import time

def abre_whatsapp(linkp):
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False) #headless é para rodar em segundo plano sem mostrar a pagina
        pagina = navegador.new_page()
        pagina.goto("https://web.whatsapp.com")
        time.sleep(1)
    return("erro")
