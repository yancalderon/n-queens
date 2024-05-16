class Estado:
    def __init__(self, tablero):
        self.tablero = tablero

    def sucesor(self, n):
        if -1 not in self.tablero:
            return []
        fila = self.tablero.index(-1)
        sucesores = []
        for col in range(n):
            nuevo_tablero = list(self.tablero)
            nuevo_tablero[fila] = col
            if es_seguro(nuevo_tablero, fila):
                sucesores.append(Estado(nuevo_tablero))
        return sucesores

    def es_meta(self):
        return -1 not in self.tablero

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
    def __init__(self, estado_inicial):
        self.pila = [Nodo(estado_inicial)]

    def DFS(self):
        while self.pila:
            nodo = self.pila.pop()
            if nodo.estado.es_meta():
                return nodo.estado.tablero
            for sucesor in nodo.estado.sucesor(len(nodo.estado.tablero)):
                hijo = Nodo(sucesor, nodo.nivel + 1, nodo.costo + 1)
                if not hijo.cerrado:
                    hijo.cerrado = True
                    self.pila.append(hijo)
        return None

def es_seguro(tablero, ocuppied_rows):
    for i in range(ocuppied_rows):
        if tablero[i] == tablero[ocuppied_rows] or \
            tablero[i] - i == tablero[ocuppied_rows] - ocuppied_rows or \
            tablero[i] + i == tablero[ocuppied_rows] + ocuppied_rows:
            return False
    return True

# Ejemplo de uso:
n = 4
tablero_inicial = [-1] * n
estado_inicial = Estado(tablero_inicial)
arbol = Arbol(estado_inicial)
solucion = arbol.DFS()
print(solucion)