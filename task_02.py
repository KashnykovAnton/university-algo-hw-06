import networkx as nx
from collections import deque

G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "E"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "G"), ("C", "H"), ("D", "F"), ("D", "G"), ("D", "E"), ("C", "E")])

def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None

def bfs(graph, start, end):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None

start_node = "C"
end_node = "F"

dfs_path = dfs(G, start_node, end_node)
bfs_path = bfs(G, start_node, end_node)

print("Шлях за допомогою DFS:", dfs_path)
print("Шлях за допомогою BFS:", bfs_path)