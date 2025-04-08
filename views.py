from main import app

import verifica_ativacao
#import abre_whatsapp
import test

from flask import Flask, render_template, request


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
        return render_template("login.html")
    if result != "erro":
        result = test.test(result)
        if result == "erro":
            return render_template("login.html")
