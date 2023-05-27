from math import inf

from vertex_class import Vertex


class Graph_Adjacent_Matrix():

    def __init__(self, vertex_number, bigraph=True, weighted=False):
        self.bigraph = bigraph
        self.weighted = weighted
        self.adjacent_matrix = []
        self.vertex_list = []

        for idx in range(vertex_number):
            self.vertex_list.append(Vertex(idx).label)

        # if weighted:
        for idx in range(vertex_number):
            self.adjacent_matrix.append(
                [None for idx in range(vertex_number)])
        # else:
        #     for idx in range(vertex_number):
        #         self.adjacent_matrix.append(
        #             [0 for idx in range(vertex_number)])

        self.vertex_number = vertex_number

    def add_link(self, vertex1, vertex2, weight=0):
        if self.weighted:
            if self.bigraph:
                self.adjacent_matrix[vertex1][vertex2] = weight
                return
            self.adjacent_matrix[vertex1][vertex2] = weight
            self.adjacent_matrix[vertex2][vertex1] = weight
            return

        # if not weighted graphs
        if self.bigraph:
            self.adjacent_matrix[vertex1][vertex2] = 1
            return
        self.adjacent_matrix[vertex1][vertex2] = 1
        self.adjacent_matrix[vertex2][vertex1] = 1
        return

    def remove_link(self, vertex1, vertex2):
        if not self.weighted:
            if self.bigraph:
                if self.adjacent_matrix[vertex1][vertex2] == 0:
                    print(f"There are no links of {vertex1} to {vertex2}")
                    return
                print(
                    f"Removing links between vertex {vertex1} and vertex {vertex2}")
                self.adjacent_matrix[vertex1][vertex2] = 0
                return

            # if not bigraph
            if self.adjacent_matrix[vertex1][vertex2] == 0:
                print(f"There are no links of {vertex1} to {vertex2}")
                return
            print(
                f"Removing links between vertex {vertex1} and vertex {vertex2}")
            self.adjacent_matrix[vertex1][vertex2] = 0
            self.adjacent_matrix[vertex2][vertex1] = 0
            return

        # if weighted
        if self.bigraph:
            if self.adjacent_matrix[vertex1][vertex2] == None:
                print(f"There are no links of {vertex1} to {vertex2}")
                return
            print(
                f"Removing links between vertex {vertex1} and vertex {vertex2}")
            self.adjacent_matrix[vertex1][vertex2] = None
            return

        # if not bigraph
        if self.adjacent_matrix[vertex1][vertex2] == None:
            print(f"There are no links of {vertex1} to {vertex2}")
            return
        print(
            f"Removing links between vertex {vertex1} and vertex {vertex2}")
        self.adjacent_matrix[vertex1][vertex2] = None
        self.adjacent_matrix[vertex2][vertex1] = None
        return

    def DFS(self):
        visited = set()
        antecessors = {}
        vertex_times = {}
        time = 0

        print("Passing through the graph using DFS")

        for vertex, _ in enumerate(self.adjacent_matrix):
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

        for possible_neighbor, exist in enumerate(self.adjacent_matrix[vertex]):
            if exist is not None and possible_neighbor not in visited:
                antecessors[possible_neighbor] = vertex
                time = self.DFS_Aux(vertex=possible_neighbor,
                                    visited=visited, antecessors=antecessors, time=time, vertex_times=vertex_times)
        time += 1
        vertex_times[vertex].append(f"finalized in {time}")
        return time

    def BFS(self, init_vertex):
        visited = set()
        antecessors = {}
        vertex_distances = {}
        print("Passing through the graph using BFS")

        for vertex, _ in enumerate(self.adjacent_matrix):
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
            for possible_neighbor, exist in enumerate(self.adjacent_matrix[first_vertex_stack]):
                if exist is not None and possible_neighbor not in visited:
                    visited.add(possible_neighbor)
                    vertex_distances[possible_neighbor] = vertex_distances[first_vertex_stack] + 1
                    antecessors[possible_neighbor] = first_vertex_stack
                    stack.append(possible_neighbor)

                    print(
                        f"Vertex: {possible_neighbor} | Distance: {vertex_distances[possible_neighbor]} | Antecessor: {antecessors[possible_neighbor]}")
        print()

    def dijkstra(self, source_vertex):
        vertex_distances = [inf for vertex in self.vertex_list]
        vertex_antecessors = [None for vertex in self.vertex_list]
        vertex_distances[source_vertex] = 0

        vertex_list = self.vertex_list[:]
        print(
            "Getting the distances using Djikstra")
        print(f"Starting vertex: {source_vertex}")

        while vertex_list:
            min_vertex = vertex_list.pop(vertex_list.index(min(vertex_list)))
            for neighbor in self.get_vertex_links(min_vertex):
                # do Relax(min_vertex, neighbor, weight)
                if vertex_distances[neighbor] > vertex_distances[min_vertex] + self.adjacent_matrix[min_vertex][neighbor]:
                    vertex_distances[neighbor] = vertex_distances[min_vertex] + \
                        self.adjacent_matrix[min_vertex][neighbor]
                    vertex_antecessors[neighbor] = min_vertex
                    print(
                        f"Vertex: {neighbor} | Distance from Vertex {source_vertex}: {vertex_distances[neighbor]} | Antecessor: {vertex_antecessors[neighbor]}")

    def bellman_ford(self, source_vertex):
        vertex_distances = [inf for vertex in self.vertex_list]
        vertex_antecessors = [None for vertex in self.vertex_list]
        vertex_distances[source_vertex] = 0

        for _ in range(len(self.vertex_list)-1):
            for edge in self.get_links_list():
                # do Relax(min_vertex, neighbor, weight)
                if vertex_distances[edge[1]] > vertex_distances[edge[0]] + self.adjacent_matrix[edge[0]][edge[1]]:
                    vertex_distances[edge[1]] = vertex_distances[edge[0]] + \
                        self.adjacent_matrix[edge[0]][edge[1]]
                    vertex_antecessors[edge[1]] = edge[0]
        for edge in self.get_links_list():
            if vertex_distances[edge[1]] > vertex_distances[edge[0]] + self.adjacent_matrix[edge[0]][edge[1]]:
                return True
        return False

    def get_vertex_links(self, vertex):
        count = []

        if self.weighted:
            for row_index, row in enumerate(self.adjacent_matrix):
                if row_index == vertex:
                    for value_index, value in enumerate(row):
                        if value:
                            count.append(value_index)
            return count
        else:
            for row_index, row in enumerate(self.adjacent_matrix):
                if row_index == vertex:
                    for value_index, value in enumerate(row):
                        if value == 1:
                            count.append(value_index)
            return count

    def get_links_list(self):
        count = 0
        links_list = []
        list_of_connections = set()
        if not self.weighted:
            if self.bigraph:
                for row_idx, row in enumerate(self.adjacent_matrix):
                    for col_idx, value in enumerate(row):
                        if value == 1:
                            links_list.append((row_idx, col_idx))
                return links_list

            # if not bigraphs

            for row_idx, row in enumerate(self.adjacent_matrix):
                for col_idx, value in enumerate(row):
                    if value == 1 and ((row_idx, col_idx) and (col_idx, row_idx)) not in list_of_connections:
                        count += 1
                        list_of_connections.add((row_idx, col_idx))
                        list_of_connections.add((col_idx, row_idx))
                        links_list.append((row_idx, col_idx))
                        links_list.append((col_idx, row_idx))
            return links_list

        # if weighted
        if self.bigraph:
            for row_idx, row in enumerate(self.adjacent_matrix):
                for col_idx, value in enumerate(row):
                    if value:
                        links_list.append((row_idx, col_idx))
            return links_list

        # if not bigraphs
        for row_idx, row in enumerate(self.adjacent_matrix):
            for col_idx, value in enumerate(row):
                if value and ((row_idx, col_idx) and (col_idx, row_idx)) not in list_of_connections:
                    count += 1
                    list_of_connections.add((row_idx, col_idx))
                    list_of_connections.add((col_idx, row_idx))
                    links_list.append((row_idx, col_idx))
                    links_list.append((col_idx, row_idx))
        return links_list

    def print_vertex_amount(self):
        print(f"There are {self.vertex_number} vertex")

    def print_links_amount(self):
        count = 0
        if not self.weighted:
            if self.bigraph:
                for row in self.adjacent_matrix:
                    for value in row:
                        if value == 1:
                            count += 1
                print(f"There are {count} links")
                return

            # if not bigraphs
            list_of_connections = set()

            for row_idx, row in enumerate(self.adjacent_matrix):
                for col_idx, value in enumerate(row):
                    if value == 1 and ((row_idx, col_idx) and (col_idx, row_idx)) not in list_of_connections:
                        count += 1
                        list_of_connections.add((row_idx, col_idx))
            print(f"There are {count} links")
            return

        # if weighted
        if self.bigraph:
            for row in self.adjacent_matrix:
                for value in row:
                    if value:
                        count += 1
            print(f"There are {count} links")
            return

        # if not bigraphs
        list_of_connections = set()

        for row_idx, row in enumerate(self.adjacent_matrix):
            for col_idx, value in enumerate(row):
                if value and ((row_idx, col_idx) and (col_idx, row_idx)) not in list_of_connections:
                    count += 1
                    list_of_connections.add((row_idx, col_idx))
        print(f"There are {count} links")
        return

    def print_vertex_links(self, vertex):
        count = []

        if self.weighted:
            for row_index, row in enumerate(self.adjacent_matrix):
                if row_index == vertex:
                    for value_index, value in enumerate(row):
                        if value:
                            count.append(value_index)
            print(f"Vertex {vertex} has {len(count)} links")
            print(f"They are with: {count}")
            return count
        else:
            for row_index, row in enumerate(self.adjacent_matrix):
                if row_index == vertex:
                    for value_index, value in enumerate(row):
                        if value == 1:
                            count.append(value_index)
            print(f"Vertex {vertex} has {len(count)} links")
            print(f"They are with: {count}")
            return count

    def print_matrix(self):
        for number_of_row, row in enumerate(self.adjacent_matrix):
            print(number_of_row, row)

    # def print_pretty_matrix(self):
    #     table = {}
    #     for number_of_row, row in enumerate(self.adjacent_matrix):
    #         table[f"vertex {number_of_row}"] = row
    #     print(tabulate(table, headers="keys",
    #           showindex=table.keys(), tablefmt="fancy_outline"))
