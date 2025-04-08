from main import app

import verifica_ativacao
import abre_whatsapp_Firefox
import abre_whatsapp_Chrome
import abre_whatsapp_Edge


from flask import Flask, render_template, request


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/homepage")
def homepage():
    return render_template("index.html")

@app.route("/loginn", methods=['GET', 'POST'])
def loginn():
    imei = request.form['imei'] #PEGA A INFORMAÇÃO DO FORMULARIO DE LOGIN
    result = verifica_ativacao.verifica_ativacao(imei) #ARMAZENA EM RESULTADO A PALARA ERRO PARA BLOQUEAR
    if result == "erro":
        return render_template("login.html")
    if result != "erro":
        return render_template("index.html")

@app.route("/abre_whatsapp1")
def Chrome():
    abre_whatsapp_Chrome.abre_whatsapp()
    return render_template("index.html")

@app.route("/abre_whatsapp2")
def Firefox():
    abre_whatsapp_Firefox.abre_whatsapp()
    return render_template("index.html")

@app.route("/abre_whatsapp3")
def Edge():
    abre_whatsapp_Edge.abre_whatsapp()
    return render_template("index.html")