class nodeavl:
    def __init__(self, value=None,nombre=None,carrera=None,dpi=None):
        self.value = value
        self.nombre=nombre
        self.carrera=carrera
        self.dpi=dpi
        self.left_child = None
        self.right_child = None
        self.parent = None  
        self.height = 1
