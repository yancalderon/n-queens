from nqueens.arbol import Arbol
from nqueens.estado import Estado
from nqueens.nodo import Nodo
import time

# Inicializa los objetos:
n = 31
tablero_inicial = [-1] * n
estado_inicial = Estado(tablero_inicial)
nodo_inical = Nodo(estado_inicial)
arbol = Arbol(estado_inicial)

# Ejecucion del algoritmo para el N ingresado:
inicio = time.time()
nodo_solucion = arbol.DFS_pila()
#nodo_solucion = arbol.DFS_recursividad(nodo_inical)
fin = time.time()
print(nodo_solucion.estado.tablero)
print(nodo_solucion)

# Metricas del resultado de la busqueda
print("Solución:", nodo_solucion.obtener_estado())
print("Profundidad máxima:", arbol.profundidad_maxima)
print("Nodos abiertos:", arbol.nodos_abiertos)
print("Nodos cerrados:", arbol.nodos_cerrados)
# print("Factor de ramificación:", len(nodo_solucion.hijos))
# print("Factor de ramificación efectivo:", len(nodo_solucion.hijos) / arbol.nodos_abiertos if arbol.nodos_abiertos != 0 else 0)
print("Tiempo de ejecución:", fin - inicio, "segundos")

# Imprimir la ruta de la solución
ruta = []
nodo_actual = nodo_solucion
while nodo_actual is not None:
    ruta.append(nodo_actual.obtener_estado())
    nodo_actual = nodo_actual.padre
ruta.reverse()
print("Ruta de la solución:")
for estado in ruta:
    print(estado)