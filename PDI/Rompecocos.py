#Funcion para intercambiar los numero
def swap(puzzle, pos1_f, pos1_c, pos2_f, pos2_c):
    aux = puzzle[pos1_f][pos1_c]
    puzzle[pos1_f][pos1_c] = puzzle[pos2_f][pos2_c]
    puzzle[pos2_f][pos2_c] = aux
    return puzzle

# Funcion que busca en que posicion esta el 0
# Devuelve la posicion de fila y columna en un arreglo
def findZero(puzzle, pos):
    k = 0
    j = 0
    for k in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if puzzle[j][k] == '0':
                pos[0] = j  # Fila
                pos[1] = k  # Columna

# Funcion que verfica si ya se visito el nodo vecino
def isvisited(puzzle, visited):
    if puzzle in visited:
        return True
    
# Funcion para encontrar los nodos vecinos
def findNeighbours(puzzle, queue, visited):
    pos = [0, 0]
    # Se busca en donde esta el 8
    findZero(puzzle, pos)
    m = pos[0]  # Fila
    n = pos[1]  # Columna

    # Lista auxiliar para guardar el nodo visitado actualmente
    aux = []

    # Se mueve el 8
    # Se mueve a la izquierda y es valido
    if (n-1) >= 0:
        # Encuentra la posicion del 0
        findZero(puzzle, pos)
        m = pos[0]  # Fila
        n = pos[1]  # Columna
        # Asigna el nodo visitado auctualmente a la lista auxiliar
        aux = puzzle
        # Se intercambia el 0 a la izquiera, por eso se pasa la columna (n) menos 1
        swap(aux, m, n, m, n-1)
        # Se imprime como queda la matriz
        print(aux)
        # Se guarda el nodo vecino en la cola

    queue.append(aux)
    # Se verifica si no ha sido visitado
    if not isvisited(aux, visited):
        visited.append(aux)
    print('Se movió hacia la izquierda')

# Se mueve hacia arriba y es valido
    if (m-1) >= 0:
        findZero(puzzle, pos)
        m = pos[0]  # Fila
        n = pos[1]  # Columna
        aux = puzzle
        swap(aux, m, n, m-1, n)
        print(aux)
        queue.append(aux)

    if not isvisited(aux, visited):
        visited.append(aux)
    print('Se movió hacia arriba')

    # Se mueve hacia la derecha y es valido
    if (n+1) < len(puzzle[0]):
        findZero(puzzle, pos)
        m = pos[0]  # Fila
        n = pos[1]  # Columna
        aux = puzzle
        # print (puzzle)
        swap(aux, m, n, m, n+1)
        print(aux)
        queue.append(aux)

        if not isvisited(aux, visited):
            visited.append(aux)
        print('Se movió hacia la derecha')

    # Se mueve hacia abajo y es valido
    if (m+1) <= len(puzzle[1]):
        findZero(puzzle, pos)
        m = pos[0]  # Fila
        n = pos[1]  # Columna
        aux = puzzle
        swap(aux, m, n, m+1, n)
        print(aux)
        queue.append(aux)

        if not isvisited(aux, visited):
            visited.append(aux)
        print('Se movió hacia abajo')
    print("------------------------------------------------------")

# Funcion para verificar si la cola esta vacia
def emptyQueue(queue):
    if len(queue) == 0:
        return True
    
# Funcion BSF
def BSF_Search(puzzle, goal):
        visited=[]

        # Se inserta el nodo inicial en la cola
        queue.append(puzzle)
        # Se marca ese nodo inicial como visitado
        visited.append(puzzle)

        # Mientras la cola no este vacia se buscan los vecinos de cada nodo
        while not emptyQueue(queue):
            # Se saca el primer elemento de la cola
            current=queue.pop(0)
            # Se verifica si ya se llego al estado final
            if current == goal:
                return
        
        # Si no se ha llegado al estado final busca los vecinos
        else:
            findNeighbours(puzzle, queue, visited)

# Programa principal

first=[['2', '0', '3'], ['1', '8', '4'], ['7', '6', '5']]
second=[['1', '2', '3'], ['8', '0', '4'], ['7', '6', '5']]
queue=[]
visited=[]
print('---------------------------------------')

BSF_Search(first,second)
