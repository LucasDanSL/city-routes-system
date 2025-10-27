import heapq
from collections import deque, defaultdict

class Grafo:
    """
    Grafo representado por lista de adjacência.
    """

    def __init__(self):
        self.adj = defaultdict(list)  # {v: [(vizinho, peso), ...]}

    def adicionar_aresta(self, u, v, peso=1, direcionado=False):
        self.adj[u].append((v, peso))
        if not direcionado:
            self.adj[v].append((u, peso))

    # BFS
    def bfs(self, start):
        visitado = set()
        fila = deque([start])
        ordem = []

        while fila:
            node = fila.popleft()
            if node not in visitado:
                visitado.add(node)
                ordem.append(node)
                for vizinho, _ in self.adj[node]:
                    if vizinho not in visitado:
                        fila.append(vizinho)
        return ordem

    # DFS
    def dfs(self, start):
        visitado = set()
        ordem = []

        def _dfs(node):
            if node in visitado:
                return
            visitado.add(node)
            ordem.append(node)
            for vizinho, _ in self.adj[node]:
                _dfs(vizinho)

        _dfs(start)
        return ordem

    # Dijkstra
    def dijkstra(self, start):
        dist = {v: float('inf') for v in self.adj}
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, peso in self.adj[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    heapq.heappush(heap, (dist[v], v))
        return dist
