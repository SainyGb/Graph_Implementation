# Adjacenccy Matrix
#from tabulate import tabulate


class Graph_Adjacent_Matrix():

    def __init__(self, size):
        self.adjacent_matrix = []
        for i in range(size):
            self.adjacent_matrix.append([0 for i in range(size)])
        self.size = size

    def add_link(self, vertex1, vertex2):
        self.adjacent_matrix[vertex1][vertex2] = 1
        #self.adjacent_matrix[vertex2][vertex1] = 1

    def remove_link(self, vertex1, vertex2):
        if self.adjacent_matrix[vertex1][vertex2] == 0:
            print(f"There are no links of {vertex1} to {vertex2}")
            return
        print(f"Removing links between vertex {vertex1} and vertex {vertex2}")
        self.adjacent_matrix[vertex1][vertex2] = 0
        #self.adjacent_matrix[vertex2][vertex1] = 0

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
            if exist == 1 and possible_neighbor not in visited:
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
                if exist == 1 and possible_neighbor not in visited:
                    visited.add(possible_neighbor)
                    vertex_distances[possible_neighbor] = vertex_distances[first_vertex_stack] + 1
                    antecessors[possible_neighbor] = first_vertex_stack
                    stack.append(possible_neighbor)

                    print(
                        f"Vertex: {possible_neighbor} | Distance: {vertex_distances[possible_neighbor]} | Antecessor: {antecessors[possible_neighbor]}")
        print()

    def print_vertex_amount(self):
        print(f"There are {self.size} vertex")

    def print_links_amount(self):
        count = 0
        for row in self.adjacent_matrix:
            for value in row:
                if value == 1:
                    count += 1
        print(f"There are {count} links")

    def print_vertex_links(self, vertex):
        count = []
        for row_index, row in enumerate(self.adjacent_matrix):
            if row_index == vertex:
                for value_index, value in enumerate(row):
                    if value == 1:
                        count.append(f"vertex {value_index}")
        print(f"Vertex {vertex} has {len(count)} links")
        print(f"They are with: {count}")

    def print_matrix(self):
        for number_of_row, row in enumerate(self.adjacent_matrix):
            print(number_of_row, row)

    # def print_pretty_matrix(self):
    #     table = {}
    #     for number_of_row, row in enumerate(self.adjacent_matrix):
    #         table[f"vertex {number_of_row}"] = row
    #     print(tabulate(table, headers="keys",
    #           showindex=table.keys(), tablefmt="fancy_outline"))


class Graph_Adjacent_List():

    def __init__(self, size):
        self.adjacent_list = {}
        for i in range(size):
            self.adjacent_list[i] = []
        self.size = size

    def add_link(self, vertex1, vertex2):
        # if vertex1 == vertex2:
        #     self.adjacent_list[f"vertex {vertex1}"].append(vertex2)
        #     return
        self.adjacent_list[vertex1].append(vertex2)
        #self.adjacent_list[f"vertex {vertex2}"].append(vertex1)

    def remove_link(self, vertex1, vertex2):
        if vertex1 not in self.adjacent_list[vertex2]:
            print(f"There are no links of {vertex1} to {vertex2}")
            return
        print(f"Removing links between vertex {vertex1} and vertex {vertex2}")
        # if vertex1 == vertex2:
        #     self.adjacent_list[f"vertex {vertex1}"].remove(vertex2)
        #     return
        self.adjacent_list[vertex1].remove(vertex2)
        #self.adjacent_list[f"vertex {vertex2}"].remove(vertex1)

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
