
#Panda para lidar com excell
import pandas as pd


from flask import Flask, render_template, request


#-----------------VERIFICA O STATUS--------
def verifica_ativacao(imei):
    #LER GOOGLE SHEETS
    try:
        link = 'https://docs.google.com/spreadsheets/d/10ys9Yphe2pahOP5Bxza-rln4kBcF1pMN_4McOjE96hE/export?format=csv'
                
        #ARMAZENA A PLANILHA E EXCLUI LINHAS VAZIAS
        valida_df = pd.read_csv(link)
        valida_df = valida_df.dropna(subset=["CODIGO"])
    except:
        return("erro")
        

    #VERIFICA O CODIGO DO PROGAMA E COLETA O STATUS
    for i, dfcodigo in enumerate(valida_df["CODIGO"]):
        dfstatus = valida_df.loc[i, "STATUS"]
        linkp = valida_df.loc[i, "LINKP"]
        if (dfcodigo == imei):
            dfcodigo = imei
            break

    #SE CODIGO DO PROGAMA NÃO FOR ENCONTRADO
    if  dfcodigo != imei:
        return("erro")
    
    #-------RETORNA O RESULTADO DO STATUS-------
    if  dfstatus == "A":
        return(linkp)
    if  dfstatus == "B":
        return(linkp)
    if  dfstatus == "C":
        return("erro")
    if  dfstatus == "D":
        return("erro")
    if  dfstatus == "E":
        return("erro")
    else:
        return("erro")
    