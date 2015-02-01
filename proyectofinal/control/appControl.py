'''
Created on 1/2/2015

@author: Miguelm
'''

from app import app
from ec.edu.itsae.labcon import Accionlabcon
from flask import render_template, request



@app.route("/reportactivos")
def ReportActivos():
    objr=Accionlabcon.Accionlabcon().reportarPersona()    
    return render_template("formRegistroActivo.html", data=objr)

@app.route("/mostrarauto")
def buscarActivoDato():
    nombre=str(request.args.get('Anombre'))
    objr=Accionlabcon.Accionlabcon().buscarActivoDato(nombre) 
    return render_template("formRegistroActivo.html", data=objr)
