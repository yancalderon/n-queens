class Estado:
    """
    Clase que Representa un estado del tablero en el problema de las N Reinas.
    Atributos:
        tablero (list): Un arreglo unidimensional que representa el tablero.
                        Los indices del vector 0, 1, ..., n-1 indican la fila en la que se encuentra la reina en esa casilla.
                        Los valores del arreglo 0, 1, ..., n-1 indican la columna en la que se encuentra la reina en esa casilla.
                        -1 indica que no hay reina en esa casilla.
    Métodos:
        __str__(self): Devuelve una representación gráfica del estado del tablero.
    """
    def __init__(self, tablero):
        """Inicializa el estado con un tablero vacío de tamaño n x n."""
        self.tablero = tablero

    def es_seguro(self, tablero, ocuppied_rows):
        """Inicializa el estado con un tablero vacío de tamaño n x n."""
        for i in range(ocuppied_rows):
            if tablero[i] == tablero[ocuppied_rows] or \
                tablero[i] - i == tablero[ocuppied_rows] - ocuppied_rows or \
                tablero[i] + i == tablero[ocuppied_rows] + ocuppied_rows:
                return False
        return True

    def sucesor(self, n):
        """Funcion sucesor """
        if -1 not in self.tablero:
            return []
        fila = self.tablero.index(-1)
        sucesores = []
        for col in range(n):
            nuevo_tablero = list(self.tablero)
            nuevo_tablero[fila] = col
            if self.es_seguro(nuevo_tablero, fila):
                sucesores.append(Estado(nuevo_tablero))
        return sucesores

    def es_meta(self):
        return -1 not in self.tablero


    def __str__(self):
        tablero_str = ""
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero)):
                if self.tablero[fila] == columna:
                    tablero_str += "Q "
                else:
                    tablero_str += ". "
            tablero_str += "\n"
        return tablero_str


class Nodo:
    id_nodo = 0

    def __init__(self, estado, nivel=0, costo=0):
        self.estado = estado
        self.hijos = []
        self.id = Nodo.id_nodo
        Nodo.id_nodo += 1
        self.nivel = nivel
        self.cerrado = False
        self.costo = costo

    def obtener_estado(self):
        return self.estado.tablero



class Arbol:
    def __init__(self, estado_inicial, nombre) -> None:
        self.raiz = Nodo(estado_inicial)
        self.nombre = nombre

    def DFS(self, nodo):
        if nodo.estado.es_meta():
            print(nodo.id)
            return nodo.estado.tablero, nodo.estado, nodo
        for sucesor in nodo.estado.sucesor(len(nodo.estado.tablero)):
            nodo.hijos.append(Nodo(sucesor, nodo.nivel + 1, nodo.costo + 1))
        for hijo in nodo.hijos:
            if not hijo.cerrado:
                hijo.cerrado = True
                print(nodo.id)
                print(nodo.estado.__str__())
                print(nodo.estado.tablero)
                solucion = self.DFS(hijo)
                if solucion is not None:
                    return solucion
        return None

# Ejemplo de uso:
n = 8
nombre_arbol = 'Arbol de solucion n reinas'
tablero_inicial = [-1] * n
estado_inicial = Estado(tablero_inicial)
arbol = Arbol(estado_inicial, nombre_arbol)
solucion, estado, nodo_meta = arbol.DFS(arbol.raiz)
print(solucion)
print(estado.__str__())
print('hijos: ', nodo_meta.hijos)
print('nivel: ', nodo_meta.nivel)
print('costo: ', nodo_meta.costo)