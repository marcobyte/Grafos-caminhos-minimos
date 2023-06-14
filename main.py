import numpy as np
from grafo import Grafo

def main():
    matriz_arestas = [[0, 1, np.inf,0], [np.inf, 0, 4, np.inf], [1, np.inf, 2, 1], [np.inf, 1, 1, 0]]
    G = Grafo(matriz_arestas)

    origem = 1

    # Dijkstra
    print("Dijkstra:")
    distancias_dijkstra = G.dijkstra(origem)
    print(distancias_dijkstra)

    matriz_arestas = [[0, -2, np.inf,-1], [np.inf, 0, 3, np.inf], [1, np.inf, 2, 1], [np.inf, 1, 1, 0]]
    D = Grafo(matriz_arestas) #]grado com pesos negativos
    # Bellman-Ford
    print("\nBellman-Ford:")
    distancias_bellman = D.bellman_ford(origem)
    print(distancias_bellman)

    # Floyd-Warshall
    print("\nFloyd-Warshall:")
    distancias_floyd = D.floyd_warshall()
    print(distancias_floyd)

if __name__ == "__main__":
    main()