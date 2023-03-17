from src.helpers import *

"""
En el ambiente vamos a tener el entorno o bien el "mundo" en el que se encuentra el agente que en
nuestro caso es el tablero de 3x3

El estado meta es el siguiente:
[1,2,3]
[4,5,6]
[7,8,0]
"""


class Environment():
    
    """ Environment constructor
        state = estado del nodo
        parent = padre del nodo
        depth = profundidad del nodo
        direccion = direccion del nodo
     """
    def __init__(self, state, parent, depth, direccion):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.direccion = direccion
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
    def __str__(self):
        return str(self.map)  

    # Metodo que realiza el movimiento del estado a una direccion
    def move(self, direction: int):
        move(self.state, direction)

    # Metodo que obtiene hijos de cada nodo
    def subNodes(node, state, parent, depth):

        global NodesExpanded
        NodesExpanded = NodesExpanded+1
        Environment.countNodes()

        print("Nodos Expandidos:", NodesExpanded)
        nextPaths = []
        nextPaths.append(Environment(move(state, 1), parent, depth + 1, 1))
        nextPaths.append(Environment(move(state, 2), parent, depth + 1, 2))
        nextPaths.append(Environment(move(state, 3), parent, depth + 1, 3))
        nextPaths.append(Environment(move(state, 4), parent, depth + 1, 4))
        nodes=[]
        for procPaths in nextPaths:
            if(procPaths.state!=None):
                nodes.append(procPaths)
        return nodes

    countNodes = 0

    # Contador de nodos expandidos, cada nodo expandido se cuenta
    def countNodes():
        countNodes = NodesExpanded
        return countNodes