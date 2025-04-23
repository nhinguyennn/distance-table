import sys
from collections import defaultdict
import heapq


class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def initializeDistances(self):
        for i in self.nodes:
            for j in self.nodes:
                self.distances[(i, j)] = sys.maxsize
        for i in self.nodes:
            self.distances[(i, "")] = 0


def dijkstra_city_distance(graph, start):
    queue = [(0, start)]  # (distance, node)
    visited = {}  # keep track of visited nodes
    distances = {node: sys.maxsize for node in graph.nodes}  # Set all distances to infinity initially
    paths = {node: "" for node in graph.nodes}  # keep track of the path for each node

    distances[start] = 0
    paths[start] = start

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited[current_node] = current_distance

        for neighbor in graph.edges[current_node]:
            weight = graph.distances[(current_node, neighbor)]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = f"{paths[current_node]} to {neighbor}"
                heapq.heappush(queue, (distance, neighbor))

    # shortest path and distances
    for node in graph.nodes:
        print(f"Distance from {start} to {node}: {distances[node]} with path({paths[node]})")


def prim_mst(graph, start):
    # Initialize all nodes as not in the MST
    mst_set = set()
    parent = {node: "" for node in graph.nodes}
    key = {node: sys.maxsize for node in graph.nodes}
    key[start] = 0
    pq = [(0, start)]  # Priority queue for Prim's algorithm (min-heap)

    while pq:
        current_key, current_node = heapq.heappop(pq)

        # Skip if the node is already in the MST
        if current_node in mst_set:
            continue

        mst_set.add(current_node)
        print(f"{current_node} is selected. Distance: {current_key}")  # Print the current node and its distance

        # Relaxation step for all adjacent nodes
        for neighbor in graph.edges[current_node]:
            weight = graph.distances[(current_node, neighbor)]
            if neighbor not in mst_set and weight < key[neighbor]:
                key[neighbor] = weight
                parent[neighbor] = current_node
                heapq.heappush(pq, (key[neighbor], neighbor))

    # MST result - Include "Denver" as the root node with distance 0
    print("\n\t\tEdge \t\t\t\tWeight")
    total = 0
    # First print the starting node (Denver) as part of MST with distance 0
    print(f"{start:>15} {start:>15} {0:>20d}")

    for node in graph.nodes:
        if parent[node] != "":
            print(f"{parent[node]:>15} {node:>15} {graph.distances[(parent[node], node)]:>20d}")
            total += graph.distances[(parent[node], node)]
    print("\nTotal MST:", "\t", total)


if __name__ == "__main__":
    g = Graph()
    # set up nodes
    g.add_node('Atlanta')
    g.add_node('Boston')
    g.add_node('Chicago')
    g.add_node('Dallas')
    g.add_node('Denver')
    g.add_node('Houston')
    g.add_node('LA')
    g.add_node('Memphis')
    g.add_node('Miami')
    g.add_node('NY')
    g.add_node('Philadelphia')
    g.add_node('Phoenix')
    g.add_node('SF')
    g.add_node('Seattle')
    g.add_node('Washington')

    # set up edges for Prim's algorithm
    g.initializeDistances()

    g.add_edge('Seattle', 'SF', 1092)
    g.add_edge('SF', 'Seattle', 1092)
    g.add_edge('Seattle', 'LA', 1544)
    g.add_edge('LA', 'Seattle', 1544)
    g.add_edge('LA', 'SF', 559)
    g.add_edge('SF', 'LA', 559)
    g.add_edge('LA', 'Houston', 2205)
    g.add_edge('Houston', 'LA', 2205)
    g.add_edge('LA', 'Denver', 1335)
    g.add_edge('Denver', 'LA', 1335)
    g.add_edge('LA', 'NY', 3933)
    g.add_edge('NY', 'LA', 3933)
    g.add_edge('LA', 'Miami', 3755)
    g.add_edge('Miami', 'LA', 3755)
    g.add_edge('Denver', 'Dallas', 1064)
    g.add_edge('Dallas', 'Denver', 1064)
    g.add_edge('Denver', 'Boston', 2839)
    g.add_edge('Boston', 'Denver', 2839)
    g.add_edge('Denver', 'Memphis', 1411)
    g.add_edge('Memphis', 'Denver', 1411)
    g.add_edge('Denver', 'Chicago', 1474)
    g.add_edge('Chicago', 'Denver', 1474)
    g.add_edge('Chicago', 'Boston', 1367)
    g.add_edge('Boston', 'Chicago', 1367)
    g.add_edge('Chicago', 'NY', 1145)
    g.add_edge('NY', 'Chicago', 1145)
    g.add_edge('Boston', 'NY', 306)
    g.add_edge('NY', 'Boston', 306)
    g.add_edge('Boston', 'Atlanta', 1505)
    g.add_edge('Atlanta', 'Boston', 1505)
    g.add_edge('Atlanta', 'Dallas', 1157)
    g.add_edge('Dallas', 'Atlanta', 1157)
    g.add_edge('Dallas', 'Houston', 362)
    g.add_edge('Houston', 'Dallas', 362)
    g.add_edge('Atlanta', 'Miami', 973)
    g.add_edge('Miami', 'Atlanta', 973)
    g.add_edge('Atlanta', 'SF', 3434)
    g.add_edge('SF', 'Atlanta', 3434)
    g.add_edge('Dallas', 'Memphis', 675)
    g.add_edge('Memphis', 'Dallas', 675)
    g.add_edge('Memphis', 'Philadelphia', 1413)
    g.add_edge('Philadelphia', 'Memphis', 1413)
    g.add_edge('Miami', 'Phoenix', 3182)
    g.add_edge('Phoenix', 'Miami', 3182)
    g.add_edge('Miami', 'Washington', 1487)
    g.add_edge('Washington', 'Miami', 1487)
    g.add_edge('Phoenix', 'NY', 3441)
    g.add_edge('NY', 'Phoenix', 3441)
    g.add_edge('Phoenix', 'Chicago', 2332)
    g.add_edge('Chicago', 'Phoenix', 2332)
    g.add_edge('Phoenix', 'Dallas', 1422)
    g.add_edge('Dallas', 'Phoenix', 1422)
    g.add_edge('Philadelphia', 'Washington', 199)
    g.add_edge('Washington', 'Philadelphia', 199)
    g.add_edge('Philadelphia', 'Phoenix', 3342)
    g.add_edge('Phoenix', 'Philadelphia', 3342)
    g.add_edge('Washington', 'Dallas', 1900)
    g.add_edge('Dallas', 'Washington', 1900)
    g.add_edge('Washington', 'Denver', 2395)
    g.add_edge('Denver', 'Washington', 2395)

    # Run Dijkstra's algorithm from 'Denver'
    print(dijkstra_city_distance(g, 'Denver'))

    # Run Prim's MST algorithm starting from 'Denver'
    prim_mst(g, 'Denver')
