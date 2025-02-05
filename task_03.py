import networkx as nx
import heapq

G = nx.Graph()
G.add_weighted_edges_from([
    ("A", "B", 4), ("A", "E", 7), ("A", "C", 3),
    ("B", "C", 6), ("B", "D", 5),
    ("C", "G", 8), ("C", "H", 2), ("C", "E", 4),
    ("D", "F", 3), ("D", "G", 6), ("D", "E", 2),
    ("E", "C", 4)
])

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def dijkstra_all(graph):
  distances = {}
  for start in graph:
      distances[start] = dijkstra(graph, start)

  return distances

distances = dijkstra_all(G)

print(f" \n Згідно алгоритму Дейкстри\n найкоротші шляхи з урахуванням ваги є такими:")
for start, distance in distances.items():
    print()
    for destination, distance in distance.items():
        print(f"  від {start} до {destination}: {distance}")
