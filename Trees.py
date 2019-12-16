# para crear copias de los arboles
from copy import deepcopy
# random
import random
import numbers

# esta funcion dice si el argumento es una funcion o no
def is_function(f):
    return hasattr(f, "__call__")

# esto nos permite recorrer una lista de a pedazos
# ejemplo el input es [1,2,3,4,5,6,7,8]
# con n=2 esta funcion nos hara tener
# [(1,2), (3,4), (5,6), (7,8)]
def chunks(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

class Node:
    def __init__(self, function):
        # nos aseguramos que el nodo recibe una funcion
        assert is_function(function)
        self.operation = function
        # esto nos permite contar cuantos argumentos recibe la funcion
        self.num_arguments = function.__code__.co_argcount
        self.arguments = []
        
    # funcion para evaluar un nodo (calcular el resultado)
    def eval(self):
        # es importante chequear que los argumentos que nos dieron
        # coincidan con los argumentos que necesitamos
        assert len(self.arguments) == self.num_arguments
        # evaluamos los argumentos, y luego los pasamos como argumentos a
        # la operacion
        # NOTA: esto -> *[...] significa que separa los elementos de la lista
        # ejemplo si tenemos `lista = [1,2,3]`
        # print(lista) -> [1,2,3]
        # print(*lista) -> 1 2 3
        # esto se llama `unpacking`.
        # lo necesitamos porque nuestra funcion recibe N argumentos
        # no una lista de tamaño N.
        return self.operation(*[node.eval() for node in self.arguments])
    
    # hace una lista con todos los hijos
    def serialize(self):
        l = [self]
        for node in self.arguments:
            l.extend(node.serialize())
        return l
    
    # copia al nodo
    def copy(self):
        return deepcopy(self)
    
    # reemplaza el nodo por otro
    def replace(self, otherNode):
        # aqui estamos haciendo algo medio hacky.
        # la forma correcta seria tener una referencia al nodo padre y
        # reemplazarse a si mismo por otro.
        # por temas de mantener el codigo corto lo hacemos asi
        # pero no lo hagan en casa!
        assert isinstance(otherNode, Node)
        self.__class__ = otherNode.__class__
        self.__dict__ = otherNode.__dict__


# esta clase representa todos los nodos quetienen 2 argumentos
class BinaryNode(Node):
    num_args = 2
    def __init__(self, function, left, right):
        # revisamos que todo sea un nodo y agregamos a las lista de
        # argumentos
        assert isinstance(left, Node)
        assert isinstance(right, Node)
        super(BinaryNode, self).__init__(function)
        self.arguments.append(left)
        self.arguments.append(right)
        

class AddNode(BinaryNode):
    def __init__(self, left, right):
        def _add(x,y):
            if isinstance(x,numbers) and isinstance(y,numbers):
                return x + y
            elif isinstance(x,dict) and not isinstance(y,dict):
                x["+"]=x["+"]+y
                return x
            elif  not isinstance(x,dict) and isinstance(y,dict):
                y["+"]=y["+"]+x
                return y
            else:
                x["+v"]=x["+v"]+y
                return x
        super(AddNode, self).__init__(_add, left, right)
        
    # esta es la funcion que define como se mostrara el nodo
    # como es un nodo que REPResenta la suma, lo mostramos como suma
    def __repr__(self):
        return "({} + {})".format(*self.arguments)
        
    
class SubNode(BinaryNode):
    def __init__(self, left, right):
        def _sub(x,y):
            if isinstance(x,numbers) and isinstance(y,numbers):
                return x - y
            elif isinstance(x,dict) and not isinstance(y,dict):
                x["+"]=x["+"]-y
                return x
            elif  not isinstance(x,dict) and isinstance(y,dict):
                y["+"]=y["+"]-x
                return y
            else:
                y["*"]=y["*"]*-1
                x["+v"]=x["+v"]+y
                return x
        super(SubNode, self).__init__(_sub, left, right)
        
    def __repr__(self):
        return "({} - {})".format(*self.arguments)
    
    
class MaxNode(BinaryNode):
    def __init__(self, left, right):
        def _max(x,y):
            return max(x,y)
        super(MaxNode, self).__init__(_max, left, right)
        
    def __repr__(self):
        return "max({{{}, {}}})".format(*self.arguments)


class MultNode(BinaryNode):
    def __init__(self, left, right):
        def _mult(x,y):
            if isinstance(x,numbers) and isinstance(y,numbers):
                return x * y
            #Aqui nos ponemos en el caso de que vengan variables
            elif isinstance(x,dict) and not isinstance(y,dict):
                x["*"]=x["*"]*y
                return x
            elif  not isinstance(x,dict) and isinstance(y,dict):
                y["*"]=y["*"]*x
                return y
            else:
                x["*v"]=x["*v"]+[y]+y["*v"]
                x["*"]=x["*"]*y["*"]
                y["*"]=1
                y["*"]=[]
                x["+v"]=x["+v"]+[{"name":x["name"],"*":y["+"], "+":0, "*v":y["+v"],"+v":[]}]
                return x

        super(MultNode, self).__init__(_mult, left, right)
        
    def __repr__(self):
        return "({} * {})".format(*self.arguments)
    
    
class TerminalNode(Node):
    # Este nodo representa una hoja de arbol. Es el nodo terminal
    # por lo que no tiene argumentos
    num_args = 0
    def __init__(self, value):
        # igual tenemos que representarlo como una funcion, por como
        # diseñamos el programa. Pero aqui va a ser una funcion vacia
        def _nothind(): pass
        super(TerminalNode, self).__init__(_nothind)
        self.value = value
        
    def __repr__(self):
        if isinstance(self.value,numbers):
            return str(self.value)


    
    def eval(self):
        # la evaluacion de un nodo terminal es el valor que contiene
        if isinstance(self.value,numbers):
            return self.value
        #caso de que sea una variable
        else:
            return {"name": self.value, "*":1, "+":0, "*v":[],"+v":[]}

