from stru.Nodos import  NodeS
from stru.nodoav import nodeavl
hola=""

listaestudiante=[]

class noode:
    def __init__(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo):
        self.Carnet = carnet
        self.DPI = dpi
        self.Nombre = nombre
        self.Carrera = carrera
        self.Password = password
        self.Creditos = creditos
        self.Edad = edad
        self.Correo = correo
        
class List:

    def __init__(self):
        self.First = None
        self.Last = None

    def getSize(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.Next()

        return counter

    def isEmpty(self):
        return self.First is None

    def getver(self):
        global hola
        return hola
    def getList(self):
        aux = self.First
        global hola
        global listaestudiante
        while aux is not None:
            print(aux.Carnet + " - " + aux.Nombre + "-" + aux.DPI + "-" + aux.Descripcion + "-" + aux.Correo)
            hola=hola+aux.Carnet + " - " + aux.Nombre + "-" + aux.DPI + "-" + aux.Descripcion + "-" + aux.Correo+"\n"
            if(aux.tipo=="user"):
                listaestudiante.append(noode(aux.Carnet,aux.DPI,aux.Nombre,aux.Carrera,aux.Password,aux.Creditos,aux.Edad,aux.Correo))
            aux = aux.Next


    def insertValue(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado,tipo):
        new_node = NodeS(carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado,tipo)

        if self.isEmpty():
            self.Last = new_node
            self.First = self.Last
        else:
            self.Last.Next = new_node
            new_node.Previous = self.Last
            self.Last = new_node

class avl:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root == None: return ''
        content='\n'
        cur_nodes = [self.root]
        cur_height = self.root.height
        sep=' '*(2**(cur_height-1))
        while True:
            cur_height += -1
            if len(cur_nodes) == 0: break
            cur_row=' '
            next_row=''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:
                if n == None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None, None])
                    continue
                if n.value != None:
                    buf=' '*int((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
                else:
                    cur_row+=' '*5+sep

                if n.left_child != None:
                    next_nodes.append(n.left_child)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
                if n.right_child!=None: 
                    next_nodes.append(n.right_child)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes = next_nodes
            sep=' '*int(len(sep)/2)
        return content

    def insert(self, value,nombre,carrera,dpi):
        if self.root == None:
            self.root = nodeavl(value,nombre,carrera,dpi)
        else:
            self._insert(value, self.root)

    def _insert(self, value,nombre,carrera,dpi, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = nodeavl(value,nombre,carrera,dpi)
                cur_node.left_child.parent = cur_node
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = nodeavl(value,nombre,carrera,dpi)

                
                cur_node.right_child.parent = cur_node
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('El valor ya existe en el arbol')

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)
    
    def delete_value(self,value):
        return self.delete_node(self.find(value))
    def delete_node(self,node):
        if node==None or self.find(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current
        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children
        node_parent=node.parent
        node_children=num_children(node)
        if node_children == 0:
            if node_parent !=None:
                if node_parent.left_child==node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root=None
        if node_children == 1:
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child
            
            if node_parent!=None:
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child
            
            child.parent=node_parent
        if node_children == 2:
            successor=min_value_node(node.right_child)
            node.value=successor.value
            self.delete_node(successor)
            return
        if node_parent!=None:
            node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))
            self._inspect_deletion(node_parent)
    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    
    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search(value,cur_node.right_child)
        return False
    
    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None: return
        path=[cur_node]+path

        left_height =self.get_height(cur_node.parent.left_child)
        right_height=self.get_height(cur_node.parent.right_child)

        if abs(left_height-right_height)>1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return
        new_height=1+cur_node.height
        if new_height>cur_node.parent.height:
            cur_node.parent.height=new_height
        self._inspect_insertion(cur_node.parent,path)
    def _inspect_deletion(self,cur_node):
        if cur_node==None: return
        left_height =self.get_height(cur_node.left_child)
        right_height=self.get_height(cur_node.right_child)

        if abs(left_height-right_height)>1:
            y=self.taller_child(cur_node)
            x=self.taller_child(y)
            self._rebalance_node(cur_node,y,x)
        self._inspect_deletion(cur_node.parent)
    def _rebalance_node(self,z,y,x):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')
    def _right_rotate(self,z):
        sub_root=z.parent
        y=z.left_child
        t3=y.right_child
        y.right_child=z
        z.parent=y
        z.left_child=t3
        if t3!=None: t3.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
            z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
            y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))

    def _left_rotate(self,z):
        sub_root=z.parent 
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2
        if t2!=None: t2.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))

    def get_height(self,cur_node):
        if cur_node==None: return 0
        return cur_node.height
    
    def taller_child(self,cur_node):
        left=self.get_height(cur_node.left_child)
        right=self.get_height(cur_node.right_child)
        return cur_node.left_child if left>=right else cur_node.right_child


