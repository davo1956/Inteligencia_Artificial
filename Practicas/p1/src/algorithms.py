from collections import deque
from src.environment import Environment
from src.helpers import *


# Algoritmo Depth First Search
def dfs(environment):
    global GoalState, GoalNode, MaxSearchDeep, MaxFrontier, initial_state
    boardVisited = set()
    stack = list([environment])
    initial_state = environment.state
    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        print("Nodo Meta:", GoalState)
        print("Nodo Actual:", node.state)
        if node.state == GoalState:
            print("\n")
            print("---------------------------------- RESULTADOS ----------------------------------")
            print("Encontramos la solucion!")
            GoalNode = node
            setMoves(initial_state, GoalNode)
            return stack
        # Invertimos el orden por cuestion de programacion
        print("\nProfundidad Nodo Actual:", node.depth)
        posiblePaths = reversed(environment.subNodes(node.state, node, node.depth))
        for path in posiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep
        if len(stack) > MaxFrontier:
            
            MaxFrontier = len(stack)
            
    # Resultado si no encontramos la solucion
    print("No encontramos solucion!")
    return False

# Regresa la profunidad del nodo
def getNodeDeep():
    return GoalNode.depth

# Regresa la profundidad maxima
def getMaxSearchDeep():
    return MaxSearchDeep

moves = []

# Agregamos los movimientos que realiza: "Arriba", "Abajo", "Izquierda" y "Derecha"
def setMoves(initial_state, GoalNode):
    while initial_state != GoalNode.state:
        string = ""
        if GoalNode.direccion == 1:
            string = 'Arriba'
        elif GoalNode.direccion == 2:
            string = 'Abajo'
        elif GoalNode.direccion == 3:
            string = 'Izquierda'
        else:
            string = 'Derecha'
        moves.insert(0, string)
        GoalNode = GoalNode.parent

# Regresa la lista de movimientos
def getMoves():
    return moves
    
