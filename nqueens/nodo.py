from .estado import Estado

class Nodo:
    """
    Representa un nodo en el árbol de búsqueda del problema de las N Reinas.
    Atributos:
        estado (Estado): El estado del tablero correspondiente al nodo.
        padre (Nodo): El nodo padre en el árbol de búsqueda.
        hijos (list): La lista de nodos hijos.

    Métodos:
        __init__(self, estado, padre=None): Inicializa el nodo con un estado y un padre opcional.
        agregar_hijo(self, estado): Agrega un nodo hijo con el estado especificado.
        get_hijos_no_explorados(self): Obtiene la lista de nodos hijos que aún no han sido explorados.
        __str__(self): Devuelve una representación en cadena del estado del nodo.
    """
    id_nodo = 0

    def __init__(self, estado, nivel=0, costo=0, padre=None) -> None:
        self.estado = estado
        self.hijos = []
        self.id = Nodo.id_nodo
        Nodo.id_nodo += 1
        self.nivel = nivel
        self.cerrado = False
        self.costo = costo
        self.padre = padre

    def __str__(self) -> str:
        """ Devuelve una representación en cadena del estado del nodo. Returns: 
            str: La representación en cadena del estado del nodo.
        """
        return str(self.estado)

    def obtener_estado(self) -> list:
        """Funcion que retorna el estado asociado al nodo en su representación como vector unidimensional"""
        return self.estado.tablero
    
    def agregar_hijo(self, hijo) -> None:
        self.hijos.append(hijo)