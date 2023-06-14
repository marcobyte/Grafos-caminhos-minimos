import numpy as np
from grafo import Grafo

def main():
    matriz_arestas = [[0, 1, np.inf,0], [np.inf, 0, 1, np.inf], [1, np.inf, 0, 1], [np.inf, 1, 1, 0]]

    G = Grafo(matriz_arestas)

    origem = 1

    # Dijkstra
    print("Dijkstra:")
    distancias_dijkstra = G.dijkstra(origem)
    for i in range(len(distancias_dijkstra)):
        print(f"A distancia minima do vertice {origem} ao vertice {i+1} é: {distancias_dijkstra[i]}")

    # Bellman-Ford
    print("\nBellman-Ford:")
    distancias_bellman = G.bellman_ford(origem)
    if distancias_bellman is None:
        print("Ha um ciclo negativo no grafo.")
    else:
        for i in range(len(distancias_bellman)):
            print(f"A distancia minima do vertice {origem} ao vertice {i+1} é: {distancias_bellman[i]}")

    # Floyd-Warshall
    print("\nFloyd-Warshall:")
    distancias_floyd = G.floyd_warshall()
    for i in range(len(distancias_floyd)):
        for j in range(len(distancias_floyd)):
            print(f"A distancia minima do vertice {i+1} ao vertice {j+1} é: {distancias_floyd[i][j]}")

if __name__ == "__main__":
    main()