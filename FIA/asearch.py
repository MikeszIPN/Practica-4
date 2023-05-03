class Node:
    # Constructor para un nodo del Puzzle
    def _init_(self, nodeNumbers, parentNode):
        self._nodeNumbers = nodeNumbers # Matriz que representa el puzzle, es decir, los numeros de 0 a 8
        self._parentNode = parentNode # Padre del que proviene el nodo
        self._f = 0 # Valor de la funcion f(x), suma de g(x) + h(x)
        self._g = 0 # Valor de la funcion g(x), costo de lo que lleva recorrido
        self._h = 0 # Valor de la funcion h(x), costo de la heuristica, para llegar a la meta

    # Setters y getters para los atributos
    def getNodeNumbers(self):
        return self._nodeNumbers
    
    def setNodeNumbers(self,numbers):
        self._nodeNumbers = numbers
    
    def getParentNode(self):
        return self._parentNode
    
    def setParentNode(self,parentNode):
        self._parentNode = parentNode
    
    def getF(self):
        return self._f
    
    def setF(self,f):
        self._f = f
    
    def getH(self):
        return self._h
    
    def setH(self,h):
        self._h = h
    
    def getG(self):
        return self._g
    
    def setG(self,g):
        self._g = g
    
    # Imprimir la matriz de numeros
    def printNode(self):
        s = self.getNodeNumbers()
        for line in s:
            print(' '.join(map(str,line)))

    # Funcion para verificar si se llego a la meta
    def isGoal(self):
        goal = [[1,2,3],[8,0,4],[7,6,5]]
        numbers = self.getNodeNumbers()
        for i in range(3):
            for j in range(3):
                if numbers[i][j] != goal[i][j]:
                    return False
        return True
    
    # Funcion para encontrar el 0 en el puzzle
    def findZero(self):
        numbers = self.getNodeNumbers()
        for i in range(3):
            for j in range(3):
                if numbers[i][j] == 0:
                    return i,j
    
    # Funcion para mover el 0 de posicion
    def swap(self, x1, y1, x2, y2):
        nodeNumbers = self.getNodeNumbers()
        aux = []

        # Se copia la matriz a una matriz temporal
        for i in nodeNumbers:
            a = []
            for j in i:
                a.append(j)
            aux.append(a)

        # Se intercambian las posiciones
        aux2 = aux[x2][y2]
        aux[x2][y2] = aux[x1][y1]
        aux[x1][y1] = aux2

        return aux
    
    # Funcion para comprobar si un movimiento es valido
    def move(self,x1,y1,x2,y2):
        # Se verifica si el movimiento no ha excedido los limites
        if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3:
            aux = self.swap( x1, y1, x2, y2)
            return aux
        else:
            return None
        
    # Funcion para encontrar los vecinos del nodo
    def findNeighbours(self):
        # Se encuentra la posicion del 0
        x, y = self.findZero()

        # Se guardan las posiciones del 0 cuando se mueva a:
        # Hacia arriba (x,y-1)
        # Hacia abajo (x,y+1)
        # Hacia la izquierda (x-1,y)
        # Hacia la derecha (x+1,y)
        neighbour_zeros = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]

        # Se inicializa una lista para guardar los vecinos
        neighbour = []

        # Se obtiene los vecinos del nodo moviendo la posicion del 0
        for i in neighbour_zeros:
            n = self.move(x,y,i[0],i[1])
            if n is not None:
                neighbour_node = Node(n,0)
                neighbour_node.setG(neighbour_node.getG() + 1)
                neighbour.append(neighbour_node)
        return neighbour
    
# Funcion para hallar la distancia Manhattan
def manhattan(s):
    goal = [[1,2,3],[8,0,4],[7,6,5]]
    h = 0
    for i in range(3):
        for j in range(3):
            h += abs(goal[i][j]-s[i][j])
    return h

# Funcion para comprobar si el vecino no es un nodo padre que ya ha sido visitado
def isParent(parents,node):
    for k in parents:
        if k == node:
            return True

class Puzzle(Node):

    # Constructor del puzzle
    def _init_(self,nodeNumbers):
        self.nodeNumbers = nodeNumbers # Matriz del estado inicial del puzzle
        self.open = [] # Lista abierta para A* Search
        self.close = [] # Lista cerrada para A* Search

    # Funcion para calcular h con la heuristica de distancia Manhattan
    def h(self, state):
        h = manhattan(state)
        return h
    
    # Funcion para calcular f como la suma de h y g(el nivel del nodo)
    def f(self,state,g):
        f = self.h(state)+g
        return f
    
    # Funcion de busqueda A* Search
    def A_search(self,puzzle):
        # Se inicializa un nodo con la matriz pasada como parametro
        start = Node(puzzle,0)

        # Se asigna g(x) como su nivel, en este caso el primer nivel es 0
        start.setG(0)
        # Se calcula su valor de f(x)
        f_val = self.f(start.getNodeNumbers(),start.getG())
        start.setF(f_val)

        # Se coloca el nodo en la lista abierta
        self.open.append(start)

        # Se inicializa una lista para guardar a los nodos padre
        parents = []

        # Mientras halla elementos en la lista abierta se buscan los nuevos nodos
        while self.open:
            # Se extrae el primer elemento de la lista abierta
            current = self.open[0].getNodeNumbers()

            # Se inicializa un nuevo nodo con el elemento obtenido
            current = Node(current,0)
            print("Nodo: ")
            current.printNode()
            print("  |")
            print("  v")

            if self.h(current.getNodeNumbers()) == 0:
                break
            
            neighbours = current.findNeighbours()

            parents.append(current.getNodeNumbers())

            cont = 1
            for i in neighbours:
                if not isParent(parents,i.getNodeNumbers()):
                    print("Vecino: ", str(cont))
                    i.setF(self.f(i.getNodeNumbers(),i.getG()))
                    i.setG(i.getG() + 1)
                    i.printNode()
                    print()
                    self.open.append(i)
                    cont += 1

            self.close.append(current)

            del self.open[0]

            # Se ordenan los elementos de acuerdo al menor valor de f
            self.open.sort(key = lambda x: x.getF(), reverse = False)

# Programa principal
nodeNumbers = [[2,0,3],[1,8,4],[7,6,5]]

puzzle = Puzzle (nodeNumbers)
puzzle.A_search(nodeNumbers)