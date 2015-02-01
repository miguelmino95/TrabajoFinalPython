'''
Created on 1/2/2015

@author: Miguelm
'''
from app import app
from flask import render_template, request,redirect, url_for
from ec.edu.itsae.labcon import Accionlabcon


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    usuario=str(request.args.get('username'))
    clave=str(request.args.get('password'))
    report=Accionlabcon.Accionlabcon().validarUsuario(usuario, clave)
    if len(report)==1:
        return redirect(url_for("main"))
    else :
        return redirect(url_for("index"))
    

@app.route("/main")
def main():
    return render_template("main.html")