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

app= Flask(__name__)
CORS(app, resources={r"/*": {"origin": "*"}})

@app.route('/entrada', methods=['POST','GET'])
def getentrada():
    if request.method=="POST":
        hola="hola"
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

            hola=user_list.getver()
        elif(nombre=="curso"):
            nombre=""

            

        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="GET":
        hola="hola"
        return Response(hola,content_type='application/x-www-form-urlencoded')





if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)