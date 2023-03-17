global GoalState, GoalNode, MaxSearchDeep, MaxFrontier, moves, NodesExpanded, deep
GoalNode = None  # Nodo meta
GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Estado meta
MaxSearchDeep= 0  # maxima profundidad
MaxFrontier= 0  # maxima frontera
NodesExpanded= 0  # total nodos visitados
deep = 0  # profundidad

# Tablero inicial
def setInitialBoard(data: [str]):
    board = []
    for i in range(0, 9):
        board.append(int(data[i]))
    return board


""" 
Metodo que mueve al agente en el tablero
@param state: el nuevo estado
@param direction: la direccion del agente
"""
def move(state: [int], direction: int):
    newState = state[:]
    # Obtiene la posicion del agente
    index = newState.index(0)

    if (index == 0):
        if (direction == 1):
            return None
        if (direction == 2):
            temp = newState[0]
            newState[0] = newState[3]
            newState[3] = temp
        if (direction == 3):
            return None
        if (direction == 4):
            temp = newState[0]
            newState[0] = newState[1]
            newState[1] = temp
        return newState
    if (index == 1):
        if (direction == 1):
            return None
        if (direction == 2):
            temp = newState[1]
            newState[1] = newState[4]
            newState[4] = temp
        if (direction == 3):
            temp = newState[1]
            newState[1] = newState[0]
            newState[0] = temp
        if (direction == 4):
            temp = newState[1]
            newState[1] = newState[2]
            newState[2] = temp
        return newState
    if (index == 2):
        if (direction == 1):
            return None
        if (direction == 2):
            temp = newState[2]
            newState[2] = newState[5]
            newState[5] = temp
        if (direction == 3):
            temp = newState[2]
            newState[2] = newState[1]
            newState[1] = temp
        if (direction == 4):
            return None
        return newState
    if (index == 3):
        if (direction == 1):
            temp = newState[3]
            newState[3] = newState[0]
            newState[0] = temp
        if (direction == 2):
            temp = newState[3]
            newState[3] = newState[6]
            newState[6] = temp
        if (direction == 3):
            return None
        if (direction == 4):
            temp = newState[3]
            newState[3] = newState[4]
            newState[4] = temp
        return newState
    if (index == 4):
        if (direction == 1):
            temp = newState[4]
            newState[4] = newState[1]
            newState[1] = temp
        if (direction == 2):
            temp = newState[4]
            newState[4] = newState[7]
            newState[7] = temp
        if (direction == 3):
            temp = newState[4]
            newState[4] = newState[3]
            newState[3] = temp
        if (direction == 4):
            temp = newState[4]
            newState[4] = newState[5]
            newState[5] = temp
        return newState
    if (index == 5):
        if (direction == 1):
            temp = newState[5]
            newState[5] = newState[2]
            newState[2] = temp
        if (direction == 2):
            temp = newState[5]
            newState[5] = newState[8]
            newState[8] = temp
        if (direction == 3):
            temp = newState[5]
            newState[5] = newState[4]
            newState[4] = temp
        if (direction == 4):
            return None
        return newState
    if (index == 6):
        if (direction == 1):
            temp = newState[6]
            newState[6] = newState[3]
            newState[3] = temp
        if (direction == 2):
            return None
        if (direction == 3):
            return None
        if (direction == 4):
            temp = newState[6]
            newState[6] = newState[7]
            newState[7] = temp
        return newState
    if (index == 7):
        if (direction == 1):
            temp = newState[7]
            newState[7] = newState[4]
            newState[4] = temp
        if (direction == 2):
            return None
        if (direction == 3):
            temp = newState[7]
            newState[7] = newState[6]
            newState[6] = temp
        if (direction == 4):
            temp = newState[7]
            newState[7] = newState[8]
            newState[8] = temp
        return newState
    if (index == 8):
        if (direction == 1):
            temp = newState[8]
            newState[8] = newState[5]
            newState[5] = temp
        if (direction == 2):
            return None
        if (direction == 3):
            temp = newState[8]
            newState[8] = newState[7]
            newState[7] = temp
        if (direction == 4):
            return None
        return newState

# Metodo para encontrar el 0 en el tablero
def findCero(state: [int]):
    for i in range(len(state)):
        if state[i] == 0:
            return i


def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# Metodo que regresa True si el puzzle tiene solucion
def isSolvable(puzzle: [int]):
    
    puzzle = transformToArray(puzzle)

    # Contador de inversiones del puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])

    # Regresa True si las inversiones son par
    return (inv_count % 2 == 0)

# Metodo que transforma nuestro puzzle a un array
def transformToArray(state: [int]):
    return [[state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]]]
