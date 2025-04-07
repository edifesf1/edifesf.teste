from main import app
from flask import Flask, render_template, request

import abre_whatsapp
import verifica_ativacao
import busca_contato
import continua_sair
import enviar_mensagem
import programa_exec
import verifica_midia


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginn", methods=['GET', 'POST'])
def loginn():
    imei = request.form['imei'] #PEGA A INFORMAÇÃO DO FORMULARIO DE LOGIN
    result = verifica_ativacao.verifica_ativacao(imei) #ARMAZENA EM RESULTADO A PALARA ERRO PARA BLOQUEAR
    if result == "erro":
        return render_template("index.html")
    if result != "erro":
        result = abre_whatsapp.abre_whatsapp(result)
        if result == "erro":
            return render_template("erro.html")
    