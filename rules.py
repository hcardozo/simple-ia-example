import networkx as nx

# Definición de la base de conocimiento como un conjunto de reglas lógicas
base_conocimiento = [
    ("A", "B", 5),
    ("A", "C", 2),
    ("B", "D", 4),
    ("C", "D", 2),
    ("C", "E", 7),
    ("D", "F", 3),
    ("E", "F", 1)
]

# Crear un grafo dirigido
grafo = nx.DiGraph()

# Agregar arcos al grafo con sus pesos (distancias)
for conexion in base_conocimiento:
    inicio, fin, distancia = conexion
    grafo.add_edge(inicio, fin, weight=distancia)

# Regla para encontrar la mejor ruta desde un punto de partida hasta un punto de destino
def encontrar_ruta(inicio, fin):
    try:
        # Utilizar el algoritmo de Dijkstra para encontrar la ruta más corta
        ruta_corta = nx.shortest_path(grafo, inicio, fin, weight='weight')
        distancia = nx.shortest_path_length(grafo, inicio, fin, weight='weight')
        return ruta_corta, distancia
    except nx.NetworkXNoPath:
        return None, None

# Ejemplo de uso
inicio = "A"  # Punto de inicio
fin = "D"     # Punto de destino
mejor_ruta, distancia = encontrar_ruta(inicio, fin)

if mejor_ruta:
    print(f"La mejor ruta desde {inicio} hasta {fin} es: {' -> '.join(mejor_ruta)}")
    print(f"La distancia total es: {distancia}")
else:
    print(f"No se encontró una ruta desde {inicio} hasta {fin}")