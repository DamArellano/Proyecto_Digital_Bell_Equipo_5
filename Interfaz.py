# Crear un grafo usando una lista de adyacencia
grafo = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

# Función para mostrar el grafo
def mostrar_grafo(grafo):
    for vertice, adyacentes in grafo.items():
        print(f"{vertice}: {', '.join(adyacentes)}")

mostrar_grafo(grafo)