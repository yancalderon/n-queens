from .nodo import Nodo
import graphviz
import time

class Arbol:
    """
    Representa un árbol de búsqueda para el problema de las N Reinas.

    Atributos:
        raiz (Nodo): El nodo raíz del árbol.
        pila (list): La pila de nodos para la búsqueda en profundidad (DFS).

    Métodos:
        __init__(self, estado_inicial): Inicializa el árbol con un estado inicial.
        __str__(self): Devuelve una representación en cadena del árbol.
    """
    def __init__(self, estado_inicial, nombre='Arbol de solucion n reinas') -> None:
        self.raiz = Nodo(estado_inicial)
        self.nombre = nombre
        self.profundidad_maxima = 0
        self.pila = [Nodo(estado_inicial)]
        self.nodos_abiertos = 1
        self.nodos_cerrados = 0
        self.max_profundidad= 30
        self.max_tiempo=120

    def agregar_a_pila(self, nodo):
        self.pila.append(nodo)
        self.nodos_abiertos += 1

    def eliminar_de_pila(self):
        nodo = self.pila.pop()
        self.nodos_abiertos -= 1
        self.nodos_cerrados += 1
        return nodo

    def verificar_profundidad(self, nivel):
        return nivel < self.max_profundidad

    def verificar_tiempo(self, inicio):
        return time.time() - inicio < self.max_tiempo

    def DFS_recursividad(self, nodo):
        if nodo.estado.es_meta():
            return nodo
        if self.verificar_profundidad(nodo.nivel):
            for sucesor in nodo.estado.sucesor(len(nodo.estado.tablero)):
                nodo.hijos.append(Nodo(sucesor, nodo.nivel + 1, nodo.costo + 1))
            for hijo in nodo.hijos:
                if not hijo.cerrado:
                    hijo.cerrado = True
                    if hijo.nivel > self.profundidad_maxima:
                        self.profundidad_maxima = hijo.nivel
                    solucion = self.DFS_recursividad(hijo)

                    if solucion is not None:
                        return solucion
        return None

    def DFS_pila(self):
        inicio = time.time()
        #print("Nodo:",self.pila[0].id, "nivel:",self.pila[0].nivel)
        #print(self.pila[0].__str__())
        while self.pila and self.verificar_tiempo(inicio):
            nodo = self.eliminar_de_pila()
            if nodo.estado.es_meta():
                return nodo
            if self.verificar_profundidad(nodo.nivel):
                hijos = [Nodo(sucesor, nodo.nivel + 1, nodo.costo + 1, nodo) for sucesor in nodo.estado.sucesor(len(nodo.estado.tablero))]
                for hijo in reversed(hijos):  # Agregar hijos en orden inverso
                    #print("Nodo:",hijo.id, "nivel:",hijo.nivel)
                    #print(hijo.__str__())
                    if not hijo.cerrado:
                        hijo.cerrado = True
                        if hijo.nivel > self.profundidad_maxima:
                            self.profundidad_maxima = hijo.nivel
                        nodo.agregar_hijo(hijo)
                        self.agregar_a_pila(hijo)
        return nodo