import busca_contato
import enviar_mensagem
import continua_sair

import pandas as pd
import time


def programa_exec(navegador,linkp):
    #ler a planilha e exclui linhas vazias baseado no nome
    try:
        contatos_df = pd.read_csv(linkp)
        time.sleep(2)
        contatos_df = contatos_df.dropna(subset=["NOME"])
        time.sleep(2)
    except:
        continua_sair.continua_sair(navegador, linkp)
    #pegar dados no excell
    for i, dfdia in enumerate(contatos_df['DIA']):
        dfmensagem = contatos_df.loc[i, 'MSG']
        dfnome = contatos_df.loc[i, "NOME"]
        dfmidia = contatos_df.loc[i, "MIDIA"]
        try:
            busca_contato.busca_contato(dfnome, navegador)
        except:
            time.sleep(1)
        try:
            enviar_mensagem.enviar_mensagem(dfmensagem, dfmidia, navegador)
        except:
            continua_sair.continua_sair(navegador, linkp)
    continua_sair.continua_sair(navegador, linkp)