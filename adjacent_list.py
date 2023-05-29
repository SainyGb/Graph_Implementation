import heapq
from math import inf


class Graph_Adjacent_List():

    def __init__(self, size, bigraph=True, weighted=False):
        self.adjacent_list = {}
        self.edge_weights = {}

        self.vertex_distances = []
        self.vertex_antecessors = []

        self.bigraph = bigraph
        self.weighted = weighted

        for i in range(size):
            self.adjacent_list[i] = []

        self.size = size

    def add_link(self, vertex1, vertex2, weight=None):
        if self.bigraph and not self.weighted:
            self.adjacent_list[vertex1].append(vertex2)
            return
        if not self.bigraph and not self.weighted:
            self.adjacent_list[vertex1].append(vertex2)
            self.adjacent_list[vertex2].append(vertex1)
            return

        if self.weighted:
            if self.bigraph:
                self.adjacent_list[vertex1].append(vertex2)
                self.edge_weights[(vertex1, vertex2)] = weight
                return
            if not self.bigraph:
                self.adjacent_list[vertex1].append(vertex2)
                self.adjacent_list[vertex2].append(vertex1)

                self.edge_weights[(vertex1, vertex2)] = weight
                self.edge_weights[(vertex2, vertex1)] = weight
                return

    def remove_link(self, vertex1, vertex2):

        if vertex2 not in self.adjacent_list[vertex1]:
            print(f"There are no links of {vertex1} to {vertex2}")
            return
        print(f"Removing links between vertex {vertex1} and vertex {vertex2}")

        if self.bigraph and not self.weighted:
            self.adjacent_list[vertex1].remove(vertex2)
            self.adjacent_list[vertex2].remove(vertex1)
            return
        if not self.bigraph and not self.weighted:
            self.adjacent_list[vertex1].remove(vertex2)
            return

        if self.weighted:
            if self.bigraph:
                self.adjacent_list[vertex1].remove(vertex2)
                del self.edge_weights[(vertex1, vertex2)]
                return
            if not self.bigraph:
                self.adjacent_list[vertex1].remove(vertex2)
                self.adjacent_list[vertex2].remove(vertex2)

                del self.edge_weights[(vertex1, vertex2)]
                del self.edge_weights[(vertex2, vertex1)]
                return

    def DFS(self):
        visited = set()
        antecessors = {}
        vertex_times = {}
        time = 0

        print("Passing through the graph using DFS")

        for vertex in self.adjacent_list:
            if vertex not in visited:
                time = self.DFS_Aux(vertex=vertex, visited=visited,
                                    time=time, antecessors=antecessors, vertex_times=vertex_times)
        print(antecessors)
        print(vertex_times)
        print(visited)
        print()

    def DFS_Aux(self, vertex, visited, antecessors, time, vertex_times):
        visited.add(vertex)

        time += 1
        vertex_times[vertex] = [f"init in {time}"]

        if vertex in antecessors.keys():
            print(
                f"Time: {time} | Vertex: {vertex} | Antecessor: { antecessors[vertex]}")
        else:
            print(f"Time: {time} | Vertex: {vertex} | Antecessor: {None}")

        for neighbor in self.adjacent_list[vertex]:
            if neighbor not in visited:
                antecessors[neighbor] = vertex
                time = self.DFS_Aux(vertex=neighbor,
                                    visited=visited, antecessors=antecessors, time=time, vertex_times=vertex_times)
        time += 1
        vertex_times[vertex].append(f"finalized in {time}")
        return time

    def BFS(self, init_vertex):
        visited = set()
        antecessors = {}
        vertex_distances = {}
        print("Passing through the graph using BFS")

        for vertex in self.adjacent_list:
            vertex_distances[vertex] = 0
            antecessors[vertex] = None

        visited.add(init_vertex)
        stack = []
        stack.append(init_vertex)

        # self.print_matrix()
        print(
            f"Initial Vertex: {init_vertex} | Distance: {vertex_distances[init_vertex]} | Antecessor: {antecessors[init_vertex]}")

        while len(stack) != 0:
            first_vertex_stack = stack.pop(0)
            for neighbor in self.adjacent_list[first_vertex_stack]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    vertex_distances[neighbor] = vertex_distances[first_vertex_stack] + 1
                    antecessors[neighbor] = first_vertex_stack
                    stack.append(neighbor)

                    print(
                        f"Vertex: {neighbor} | Distance: {vertex_distances[neighbor]} | Antecessor: {antecessors[neighbor]}")
        print()

    def dijkstra(self, source_vertex):
        self.vertex_distances = \
            [inf for _, _ in enumerate(self.adjacent_list.keys())]
        self.vertex_antecessors = \
            [None for _, _ in enumerate(self.adjacent_list.keys())]
        self.vertex_distances[source_vertex] = 0

        visited = set()
        visited.add(source_vertex)

        queue = []
        heapq.heappush(queue, (0, source_vertex))

        print(
            "Getting the distances using Djikstra")
        print(f"Starting vertex: {source_vertex}")

        while queue:
            weight_min_vertex, min_vertex = heapq.heappop(queue)
            for neighbor in self.adjacent_list[min_vertex]:
                if neighbor not in visited:
                    relax = self.relax(min_vertex, neighbor)
                    heapq.heappush(
                        queue, (self.vertex_distances[relax], relax))
                    visited.add(neighbor)
                    print(
                        f"Vertex: {neighbor} | Distance from Vertex {source_vertex}: {self.vertex_distances[neighbor]} | Antecessor: {self.vertex_antecessors[neighbor]}")

    def relax(self, vertex1, vertex2):
        if self.vertex_distances[vertex2] > self.vertex_distances[vertex1] + self.edge_weights[(vertex1, vertex2)]:
            self.vertex_distances[vertex2] = self.vertex_distances[vertex1] + \
                self.edge_weights[(vertex1, vertex2)]
            self.vertex_antecessors[vertex2] = vertex1
            return vertex2

    def print_vertex(self):
        print(
            f"There are {len(self.adjacent_list.keys())} Vertex \n" +
            f"They are: {list(self.adjacent_list.keys())}"
        )

    def print_links(self):
        print(
            f"There are {len([(key, value) for key in self.adjacent_list.keys() for value in self.adjacent_list[key]])} Links \n" +
            f"They are {[(key, value) for key in self.adjacent_list.keys() for value in self.adjacent_list[key]]}"
        )

    def print_lists(self):
        print(self.adjacent_list)

    def print_vertex_links(self, vertex):
        print(
            f"Vertex {vertex} has {len(self.adjacent_list[vertex])} links")
        print(f"They are with: {self.adjacent_list[vertex]}")
