import numpy as np

class Vertice:
    def __init__(self, id, ini, fim):
        self.id = id
        self.listaAdjInicio = ini
        self.listaAdjFim = fim
        self.distancia = np.inf
        self.visitado = False

    def getId(self):
        return self.id

class Grafo:
    def __init__(self, matrizDeAdj):
        self.arestas = np.copy(matrizDeAdj)
        numVertices = np.shape(matrizDeAdj)[0]
        if (numVertices > 0 and np.shape(matrizDeAdj)[0] == np.shape(matrizDeAdj)[1]):
            self.vertices = []
            for i in range(numVertices):
                v = Vertice(i+1,[],[])
                self.vertices.append(v)
            for i in range(numVertices):
                for j in range(numVertices):
                    for k in self.vertices:
                        if(k.getId() == j+1):
                            a = k
                        if(k.getId() == i+1):
                            b = k
                    a.listaAdjFim.append(b.getId())
                    b.listaAdjInicio.append(a.getId())

    def getVertices(self):
        return len(self.vertices)
    
    def getArestas(self):
        return len(self.arestas)
    
    def dijkstra(self, origem):
        for v in self.vertices:
            if v.getId() == origem:
                v.distancia = 0
                break

        for _ in range(len(self.vertices)):
            menor_distancia = np.inf
            vertice_atual = None
            for v in self.vertices:
                if not v.visitado and v.distancia < menor_distancia:
                    menor_distancia = v.distancia
                    vertice_atual = v

            if vertice_atual is None:
                break

            vertice_atual.visitado = True

            for adjacente_id in vertice_atual.listaAdjFim:
                for adjacente in self.vertices:
                    if adjacente.getId() == adjacente_id and not adjacente.visitado:
                        nova_distancia = vertice_atual.distancia + self.arestas[vertice_atual.getId()-1][adjacente_id-1]
                        if nova_distancia < adjacente.distancia:
                            adjacente.distancia = nova_distancia

        return [v.distancia for v in self.vertices]
    
    def bellman_ford(self, origem):
        for v in self.vertices:
            if v.getId() == origem:
                v.distancia = 0
                break

        for _ in range(len(self.vertices) - 1):
            for i in range(len(self.arestas)):
                for j in range(len(self.arestas)):
                    if self.arestas[i][j] != 0:
                        u = self.vertices[i]
                        v = self.vertices[j]
                        nova_distancia = u.distancia + self.arestas[i][j]
                        if nova_distancia < v.distancia:
                            v.distancia = nova_distancia
        
        for i in range(len(self.arestas)): #Verifica se há ciclos negativos
            for j in range(len(self.arestas)):
                if self.arestas[i][j] != 0:
                    u = self.vertices[i]
                    v = self.vertices[j]
                    nova_distancia = u.distancia + self.arestas[i][j]
                    if nova_distancia < v.distancia:
                        return None
                
        return [v.distancia for v in self.vertices]
    
    def floyd_warshall(self):
        numVertices = len(self.vertices)
        distancias = np.copy(self.arestas)

        for i in range(numVertices):
            distancias[i][i] = 0

        for k in range(numVertices):
            for i in range(numVertices):
                for j in range(numVertices):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

        return distancias
