class Edge:
    def __init__(self, vertex1, vertex2):
        self.v1 = vertex1
        self.v2 = vertex2
        self.next_v1 = None
        self.next_v2 = None

class Vertex:
    def __init__(self, data):
        self.data = data
        self.edge = None  

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        if data not in self.vertices:
            self.vertices[data] = Vertex(data)

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        edge = Edge(v1, v2)

        # Insert edge into v1's list
        edge.next_v1 = self.vertices[v1].edge
        self.vertices[v1].edge = edge

        # Insert edge into v2's list
        edge.next_v2 = self.vertices[v2].edge
        self.vertices[v2].edge = edge

    def print_graph(self):
        for v_key in self.vertices:
            v = self.vertices[v_key]
            print(f"{v.data} ->", end=" ")
            edge = v.edge
            visited = set()
            while edge:
                neighbor = edge.v2 if edge.v1 == v.data else edge.v1
                if (v.data, neighbor) not in visited and (neighbor, v.data) not in visited:
                    print(neighbor, end=" ")
                    visited.add((v.data, neighbor))
                edge = edge.next_v1 if edge.v1 == v.data else edge.next_v2
            print()

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('C', 'E')

g.print_graph()
