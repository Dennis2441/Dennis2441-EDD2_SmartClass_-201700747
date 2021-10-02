
import os


cc=0
ff=0
ncolumna=0
nfila=0
listahora=[]
listadia=[]
listamatriz=[]
numerocarnet=""
veryear=""
vermes=""
class Nodo1(): #Nodo que guarda las cantidades de combustible
    def __init__(self,fila,columna,carnet,nombre,descripcion,materia,fecha,hora,estado):
        self.carnet=carnet
        self.nombre=nombre
        self.descripcion=descripcion
        self.materia=materia
        self.fecha=fecha
        self.hora=hora
        self.fecha=fecha
        self.fila=fila
        self.estado=estado
        self.derecha=None
        self.izquierda=None
        self.abajo=None
        self.arriba=None
class nodoencabezado:
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        self.acceso=None
class listaencabezado:
    def __init__(self,primero=None):
        self.primero=primero
    def eliminarp(self):
        if(self.primero==None):
            print("vacio")
        
        if self.primero.siguiente==None:
                self.primero=None
                return
        
        self.primero=self.primero.siguiente
        self.primero.anterior=None
    def eliminar(self,id):
        if(self.primero==None):
            print("vacio")
        else:
            if(self.primero==id):
                print(self.primero.id)
                self.eliminarp()
                return

    def setencabezadp(self,nuevo):
        if (self.primero==None):
            self.primero=nuevo
        elif(nuevo.id<self.primero.id):
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente !=None:
                if(nuevo.id<self.primero.id):
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente
            if(actual.siguiente==None):
                actual.siguiente=nuevo
                nuevo.anterior=actual
    def getencabezado(self,id):
        actual=self.primero
        while actual !=None:
            if(actual.id==id):
                return actual
            actual=actual.siguiente
        return None

class matrizx:
    
    
    def __init__(self):
        
        self.efilas=listaencabezado()
        self.ecolumnas=listaencabezado()
    def insertar(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        
        global ff
        global cc
        nuevo=Nodo1(ff,cc,carnet,nombre,descripcion,materia,fecha,hora,estado)
        ecolumna=self.ecolumnas.getencabezado(cc)
        print(ecolumna)
        if ecolumna==None:
            ecolumna=nodoencabezado(cc)
            ecolumna.acceso=nuevo
            self.ecolumnas.setencabezadp(ecolumna)
           
        else:
            if (nuevo.fila < ecolumna.acceso.fila):
                nuevo.abajo=ecolumna.acceso
                ecolumna.acceso.arriba=nuevo
                ecolumna.acceso=nuevo
            else:
                actual=ecolumna.acceso
                while actual.abajo !=None:
                    if nuevo.fila< actual.abajo.fila:
                        nuevo.abajo=actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba=actual
                        actual.abajo=nuevo
                        break
                    actual=actual.abajo
                if(actual.abajo==None):
                    actual.abajo=nuevo
                    nuevo.arriba=actual
        #insercion encabezado por filas
        efila= self.efilas.getencabezado(ff)
        if efila==None:
            efila=nodoencabezado(ff)
            efila.acceso=nuevo
            self.efilas.setencabezadp(efila)
        else:
            if (nuevo.columna < efila.acceso.columna):
                nuevo.derecha=efila.acceso
                efila.acceso.izquierda=nuevo
                efila.acceso=nuevo
            else:
                actual=efila.acceso
                while actual.derecha !=None:
                    if nuevo.columna< actual.derecha.columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha
                if(actual.derecha==None):
                    actual.derecha=nuevo
                    nuevo.izquierda=actual
        cc=cc+1
        ff=ff+1
   
    def buscar3(self,dia,hora,carnet,year,mes):
        global listadia
        global listahora
        global ncolumna
        global nfila
        
        global numerocarnet
        
        
        ecolumna=self.ecolumnas.primero
        ver=False
        quotes='"'
        estado=0
        contado=0
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.carnet==carnet:
                    
                    strin=str(actual.fecha)
                    dayy=strin.split("/")[0]
                    mess=strin.split("/")[1]
                    yearr=strin.split("/")[2]

                    if(year==yearr):

                        if(mes==mess):
                            if(dayy==dia):
                                if(actual.hora==hora):
                                    contado=contado+1
                                    
                                        
                actual=actual.abajo
            ecolumna=ecolumna.siguiente


                
        return contado

    def imprimir(self):
        global numerocarnet
        global ncolumna
        global nfila
        kf=nfila+1
        kc=ncolumna+1
        global veryear
        global vermes
        inde=0
        inde2=0
        inde3=0
        ver=False
        MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\ima2.txt",'w')
        MapaRuta.write('digraph {' + "\n")
        MapaRuta.write('node [shape=plaintext]' + "\n")
        MapaRuta.write('some_node [' + "\n")
        MapaRuta.write('label=<' + "\n")
        MapaRuta.write('<table border="0" cellborder="1" cellspacing="0">' + "\n")
        MapaRuta.write('<tr>' + "\n")
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(numerocarnet + "\n")
        MapaRuta.write('</td>' + "\n")
        for i in listadia:
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write("Dia: "+str(i) + "\n")
            MapaRuta.write('</td>' + "\n")
        MapaRuta.write('</tr>' + "\n")
        for i in range(1,kf):
            MapaRuta.write('<tr>' + "\n")
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write("Hora: "+str(listahora[inde3]) + "\n")
            MapaRuta.write('</td>' + "\n")
            inde3=inde3+1
            if(ver==False):
                inde2=0
            else:
                inde=inde+1
                inde2=0
            for j in range(1,kc):
                val=self.buscar3(str(listadia[inde2]),str(listahora[inde]),numerocarnet,veryear,vermes)
                inde2=inde2+1
                if(val==0):
                    val=""
                    MapaRuta.write('<td>' + "\n")
                    MapaRuta.write(val + "\n")
                    MapaRuta.write('</td>' + "\n")
                    ver=True
                else:
                    MapaRuta.write('<td>' + "\n")
                    MapaRuta.write(str(val) + "\n")
                    MapaRuta.write('</td>' + "\n")
                    ver=True
                if(j==ncolumna):
                    MapaRuta.write('</tr>' + "\n")
                    ver=True
        MapaRuta.write(' </table>>' + "\n")
        MapaRuta.write('  ];' + "\n")
        MapaRuta.write(' }' + "\n")
        MapaRuta.close()
        os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.svg")
        os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.jpg")
        os.system("dot -Tpng "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.png")


    def buscar2(self,dia,carnet,year,mes):
        global listadia
        global listahora
        global ncolumna
        global nfila
        temporal=[]
        ecolumna=self.ecolumnas.primero
        for x in listadia:
            fecha=str(x)+"/"+mes+"/"+year
            while ecolumna !=None:
                actual=ecolumna.acceso
                while actual !=None:
                    if actual.carnet==carnet:
                        
                        strin=str(actual.fecha)
                        if(strin==fecha):
                            listahora.append(int(actual.hora))
                    actual=actual.abajo
                ecolumna=ecolumna.siguiente
            listahora.sort()
            temporal.extend(listahora)
            listahora=[]

            for x in temporal:
                if(x in listahora):
                    hola=""
                else:
                    print(x)
                    listahora.append(int(x))
            nfila=len(listahora)
            ncolumna=len(listadia)                
 
    def imprimir2(self,dia,carnet,year,mes,hora):
        global listadia
        global listahora
        global ncolumna
        global nfila
        
        global numerocarnet
        arhivo=""
        anterior=""
        ecolumna=self.ecolumnas.primero
        ver=False
        quotes='"'
        estado=0
        contado=0
        br ="\n"
        MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\listatarea.txt",'w')
        MapaRuta.write('digraph foo {' + "\n")
        MapaRuta.write('rankdir=LR;' + "\n")
        MapaRuta.write('node [shape=record]' + "\n")
        ver=False
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.carnet==carnet:
                    nodooo="nodo"+str(contado)
                    strin=str(actual.fecha)
                    dayy=strin.split("/")[0]
                    mess=strin.split("/")[1]
                    yearr=strin.split("/")[2]

                    if(year==yearr):

                        if(mes==mess):
                            if(dayy==dia):
                                if(actual.hora==hora):
                                    ver=True
                                    MapaRuta.write(br+nodooo+"[label=\"Carnet:"+actual.carnet+"|Nombre:"+actual.nombre+"|Descripcion:"+actual.descripcion+"|Materia:"+actual.materia+"|fecha:"+actual.fecha+"|Hora:"+actual.hora+"|Estado:"+actual.estado+"\"];\n")

                                    if(anterior==""):
                                        MapaRuta.write(br+nodooo)
                                    
                                        anterior=nodooo
                                        nodooo=""
                                    else:
                                    
                                        MapaRuta.write("\n"+anterior+"->"+nodooo+"\n")
                                        
                                        anterior=nodooo
                                        nodooo=""

            
                                    contado=contado+1
                                    
                                        
                actual=actual.abajo
            ecolumna=ecolumna.siguiente
        if(ver==False):
            return "ver"                     
        else:
            MapaRuta.write(' }' + "\n")
            MapaRuta.close()
            os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\listatarea.txt -o "r"C:\Users\denni\OneDrive\Desktop\listatarea.svg")
            os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\listatarea.txt -o "r"C:\Users\denni\OneDrive\Desktop\listatarea.jpg") 
            return "Okey"                          
                            

                    


    def buscar1(self,carnet,year,mes):
        hola=""

         
        global listadia
        global listahora
        temporal=[]
        global numerocarnet
        global veryear
        global vermes
        vermes=mes
        veryear=year
        numerocarnet=carnet
        ecolumna=self.ecolumnas.primero
        ver=False
        quotes='"'
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.carnet==carnet:
                    
                    strin=str(actual.fecha)
                    dayy=strin.split("/")[0]
                    mess=strin.split("/")[1]
                    yearr=strin.split("/")[2]

                    if(year==yearr):

                        if(mes==mess):
                            ver=True
                            listadia.append(int(dayy))    
                actual=actual.abajo
            

                
                        
            

            ecolumna=ecolumna.siguiente
            if(ver==False):
                return ver
            else:
                listadia.sort()
                temporal.extend(listadia)
                listadia=[]

                for x in temporal:
                    if(x in listadia):
                        hola=""
                    else:
                        print(x)
                        listadia.append(int(x))
                temporal=[]
                for i in listadia:
                    self.buscar2(i,carnet,year,mes)


       
            

                
                        
            



if __name__=='__main__':
    hola=matrizx()

    hola.insertar("201700747","descripcion","descripcion","hdfskhdfs","10/5/2020","8","activado")
    hola.insertar("201700747","descripcion","descripcion","hdfskhdfs","10/5/2020","8","activado")
    hola.insertar("201700747","descripcion","hsdkfkdsf","hdfskhdfs","9/5/2020","6","deactivado")
    hola.insertar("201700747","descripcion","sfddsf","hdfskhdfs","9/5/2020","6","activado")
    hola.insertar("201700747","descripcion","descripcion","hdfskhdfs","9/5/2020","7","activado")
    hola.buscar1("201700747","2020","5")
    hola.imprimir()
    hola.imprimir2("9","201700747","2020","5","6")
    
    