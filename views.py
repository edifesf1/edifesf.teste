from main import app

import abre_whatsapp

from flask import Flask, render_template, request

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/loginn", methods=['GET', 'POST'])
def loginn():
    imei = request.form['imei'] #PEGA A INFORMAÇÃO DO FORMULARIO DE LOGIN
    abre_whatsapp.abre_whatsapp(imei)