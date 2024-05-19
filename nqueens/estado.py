class Estado:
    """
    Representa los estados del problema, para el problema de las N Reinas un estado se representa como el tablero y la ubicacion de las i-esimas reinas (i=0,1,2..,n) .
    Atributos:
        tablero (list): Un vector (arreglo unidimensional) que representa el tablero.
                        Los indices del vector 0, 1, ..., n-1 indican la fila en la que se encuentra la reina en esa casilla.
                        Los valores del arreglo 0, 1, ..., n-1 indican la columna en la que se encuentra la reina en esa casilla.
                        -1 indica que no hay reina en esa casilla.
    """
    def __init__(self, tablero):
        """Inicializa el estado con un tablero determinado"""
        self.tablero = tablero

    def es_seguro(self, tablero, ocuppied_rows): # ocuppied_rows: el número de filas ocupadas (número de reinas ya colocadas).
        """Verifica si es seguro (no es atacada por otra reina) colocar una reina i en la posición que esta evaluando"""
        for i in range(ocuppied_rows):
            if tablero[i] == tablero[ocuppied_rows] or \
                tablero[i] - i == tablero[ocuppied_rows] - ocuppied_rows or \
                tablero[i] + i == tablero[ocuppied_rows] + ocuppied_rows:
                return False
        return True

    def sucesor(self, n):
        """Funcion para el calculo del estado sucesor"""
        if -1 not in self.tablero: # Si todas las reinas ya han sido colocadas, entonces no hay estados sucesores y la función devuelve una lista vacía.
            return []
        fila = self.tablero.index(-1) # Encuentra la primera fila donde no se ha colocado una reina (donde el valor es -1)
        sucesores = []
        for col in range(n):
            nuevo_tablero = list(self.tablero)
            nuevo_tablero[fila] = col
            if self.es_seguro(nuevo_tablero, fila):
                sucesores.append(Estado(nuevo_tablero))
                #print("nodos sucesores:" ,print(nuevo_tablero), "fila: ", fila, "suscesores:", sucesores)
        return sucesores

    def es_meta(self):
        """ Funcion prueba de meta, que verifica si el tablero ya tiene colocada las n reinas colocadas en el tablero
        (verificar si el valor -1 no está presente en la lista) en ese caso retorna True
        """
        return -1 not in self.tablero

    def __str__(self):
        """ Método especial en python que representa un objeto como una cadena de caracteres, es llamado automaticamente 
        por la funcion print() """
        tablero_str = ""
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero)):
                if self.tablero[fila] == columna:
                    tablero_str += "Q "
                else:
                    tablero_str += ". "
            tablero_str += "\n"
        return tablero_str