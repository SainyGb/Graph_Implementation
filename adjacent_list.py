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

    def DFS(self, source=None, verbose=False):
        visited = set()
        antecessors = {}
        vertex_times = {}
        time = 0

        if verbose:
            print("Passing through the graph using DFS")

        if source is not None:
            time = self.DFS_Aux(vertex=source, visited=visited,
                                time=time, antecessors=antecessors, vertex_times=vertex_times, verbose=verbose)
        else:
            for vertex in self.adjacent_list:
                if vertex not in visited:
                    time = self.DFS_Aux(vertex=vertex, visited=visited,
                                        time=time, antecessors=antecessors, vertex_times=vertex_times, verbose=verbose)

        if verbose:
            print(antecessors)
            print(vertex_times)
            print(visited)
            print()
        return visited

    def DFS_Aux(self, vertex, visited, antecessors, time, vertex_times, verbose):
        visited.add(vertex)

        time += 1
        vertex_times[vertex] = [f"init in {time}"]

        if verbose:
            if vertex in antecessors.keys():
                print(
                    f"Time: {time} | Vertex: {vertex} | Antecessor: { antecessors[vertex]}")
            else:
                print(f"Time: {time} | Vertex: {vertex} | Antecessor: {None}")

        for neighbor in self.adjacent_list[vertex]:
            if neighbor not in visited:
                antecessors[neighbor] = vertex
                time = self.DFS_Aux(vertex=neighbor,
                                    visited=visited, antecessors=antecessors, time=time, vertex_times=vertex_times, verbose=verbose)
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
                        f"Vertex: {neighbor} | Distance from Vertex {source_vertex}: {self.vertex_distances[neighbor]} |" +
                        "Antecessor: {self.vertex_antecessors[neighbor]}")

    def relax(self, vertex1, vertex2):
        if self.vertex_distances[vertex2] > self.vertex_distances[vertex1] + self.edge_weights[(vertex1, vertex2)]:
            self.vertex_distances[vertex2] = self.vertex_distances[vertex1] + \
                self.edge_weights[(vertex1, vertex2)]
            self.vertex_antecessors[vertex2] = vertex1
            return vertex2

    def bellman_ford(self, source_vertex):
        self.vertex_distances = [inf for vertex in self.adjacent_list]
        self.vertex_antecessors = [None for vertex in self.adjacent_list]
        self.vertex_distances[source_vertex] = 0
        edge_list = self.get_edges_list()
        for _ in range(len(self.adjacent_list)-1):
            for edge in edge_list:
                self.relax(edge[0], edge[1])
        for edge in edge_list:
            if self.vertex_distances[edge[1]] > self.vertex_distances[edge[0]] + self.edge_weights[(edge[0], edge[1])]:
                return True
        return False

    def floyd_warshall(self):
        self.vertex_distances = [inf for vertex in self.adjacent_list]
        self.vertex_antecessors = [None for vertex in self.adjacent_list]

        aux_matrix = [[] for row in self.adjacent_list]

        for row_idx, _ in enumerate(self.adjacent_list):
            for col_idx, _ in enumerate(self.adjacent_list):
                if row_idx == col_idx:
                    aux_matrix[row_idx].append(0)
                elif (row_idx, col_idx) in self.edge_weights:
                    aux_matrix[row_idx].append(self.edge_weights[
                        (row_idx, col_idx)])
                else:
                    aux_matrix[row_idx].append(inf)

        for number_of_row, row in enumerate(aux_matrix):
            print(number_of_row, row)
        print()

        for k, _ in enumerate(aux_matrix):
            for i, _ in enumerate(aux_matrix):
                for j, _ in enumerate(aux_matrix):
                    aux_matrix[i][j] = min(aux_matrix[i][j], aux_matrix[i][k] +
                                           aux_matrix[k][j])
                    self.vertex_antecessors[j] = k

        for number_of_row, row in enumerate(aux_matrix):
            print(number_of_row, row)

    def connected_components(self):
        visited = set()
        component_count = 0
        print("Executing Connected Components Algorithm")
        for vertex, _ in enumerate(self.adjacent_list):
            if vertex not in visited:
                visited = visited.union(self.DFS(vertex, verbose=False))
                component_count += 1

                print(
                    f"Visited vertex in the {component_count} DFS pass: {visited}")

        print(f"Total amount of components: {component_count}")

    def transitive_closure(self):
        closure_matrix = [[] for row in self.adjacent_list]
        edge_list = self.get_edges_list()

        for row_idx, _ in enumerate(self.adjacent_list):
            for col_idx, _ in enumerate(self.adjacent_list):
                if (row_idx, col_idx) in edge_list:
                    closure_matrix[row_idx].append(1)
                else:
                    closure_matrix[row_idx].append(0)

        for k, _ in enumerate(closure_matrix):
            for i, _ in enumerate(closure_matrix):
                for j, _ in enumerate(closure_matrix):
                    closure_matrix[i][j] = closure_matrix[i][j] or (
                        closure_matrix[i][k] and closure_matrix[k][j])

        for number_of_row, row in enumerate(closure_matrix):
            print(number_of_row, row)

    def get_edges_list(self) -> list[tuple]:
        edge_list = []
        for vertex, edges in self.adjacent_list.items():
            edge_list += [(vertex, edge) for edge in edges]
        return edge_list

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
