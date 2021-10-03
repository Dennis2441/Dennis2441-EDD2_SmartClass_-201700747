from flask import Flask, jsonify, request,Response
from flask_cors import CORS
from tkinter import filedialog
from tkinter import Tk

import json
import types
from xml.dom.minidom import Node
from datetime import datetime
import numpy as np
import datetime
import plotly.graph_objects as go
import os
import re

from analizador.Syntactic import parser
from analizador.Syntactic import user_list, task_list
from stru.list import av
from stru.list import matiz
app= Flask(__name__)
CORS(app, resources={r"/*": {"origin": "*"}})

@app.route('/entrada', methods=['POST','GET'])
def getentrada():
    if request.method=="POST":
        hola="Carga Completa"
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        print(aList)
        nombre=aList["tipo"]
        ruta=aList["path"]

        
        if(nombre=="estudiante"):
            f = open(ruta,"r", encoding="utf-8")
            mensaje = f.read()
            print(mensaje)
            f.close()
            parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
            parser.parse(mensaje)

            user_list.getList()
            print("------------------------")
            task_list.getList()
            
          #  av.imprimir2()
            
            user_list.getver()
            
        elif(nombre=="curso"):
            for p in aList['Cursos']:
                codigo=['Codigo']
                name=['Nombre']
                credito=str(p['Creditos'])
                pre=str(p['Prerequisitos'])
                obligatorio=str(p['Obligatorio'])
                

            

        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="GET":
        hola="hola"
        return Response(hola,content_type='application/x-www-form-urlencoded')


@app.route('/reporte', methods=['POST','GET'])
def getreporte():
    if request.method=="GET":
        hola="Buscar la Imagen"
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        print(aList)
        nombre=aList["tipo"]
        if(nombre==0):
           hola="Buscar la Imagen"
           av.imprimir2()
        elif(nombre==1):
            carnet=aList["carnet"]
            year=aList["año"]
            mes=aList["mes"]
            matiz.buscar1(carnet,year,mes)
            matiz.imprimir()
        elif(nombre==2):
            carnet=aList["carnet"]
            year=aList["año"]
            mes=aList["mes"]
            dia=aList["dia"]
            hora=aList["hora"]
            matiz.buscar1(carnet,year,mes)
            matiz.imprimir2(dia,carnet,year,mes,hora)
        elif(nombre==3):
            ho=""
        elif(nombre==4):
            ho=""
        
        #ruta=aList["path"]

        
        

            

        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="GET":
        hola="hola"
        return Response(hola,content_type='application/x-www-form-urlencoded')

@app.route('/estudiante', methods=['POST','GET','DELETE','PUT'])
def getestudiante():
    hola=""
    if request.method=="POST":
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=['carnet']
        DPI=['DPI']
        nombre=str['nombre']
        carrera=str['carrera']
        correo=['correo']
        password=['password']
        creditos=str(['creditos'])
        edad=str(['edad'])

        user_list.insertValue(carnet,DPI,nombre,carrera,password,creditos,edad,correo,"","","","","","user")
        av.insert(carnet,nombre,carrera,DPI)
        hola="Hecho"
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif(request.method=="DELETE"):
        jsonStr= request.data.decode('utf-8')
        
        aList = json.loads(jsonStr)
        carnet=['carnet']
        av.delete_value(carnet)
        hola="Hecho"
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif(request.method=="PUT"):
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=['carnet']
        DPI=['DPI']
        nombre=str['nombre']
        carrera=str['carrera']
        correo=['correo']
        password=['password']
        creditos=str(['creditos'])
        edad=str(['edad'])
        av.search(carnet,DPI,nombre,carrera,password,creditos,edad,correo)
        hola="Hecho"
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif(request.method=="GET"):
        jsonStr= request.data.decode('utf-8')
        
        aList = json.loads(jsonStr)
        carnet=['carnet']
        av.search2(carnet)
    



if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)