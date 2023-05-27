from adjacent_matrix import Graph_Adjacent_Matrix


def teste1():
    simple_graph_using_matrix = Graph_Adjacent_Matrix(4)
    simple_graph_using_matrix.add_link(0, 1)
    simple_graph_using_matrix.add_link(0, 3)
    simple_graph_using_matrix.add_link(1, 0)
    simple_graph_using_matrix.add_link(1, 2)
    simple_graph_using_matrix.add_link(2, 1)
    simple_graph_using_matrix.add_link(3, 0)

    # simple_graph_using_matrix.print_pretty_matrix()
    simple_graph_using_matrix.print_matrix()
    print()
    simple_graph_using_matrix.print_vertex_amount()
    print()
    simple_graph_using_matrix.print_links_amount()
    print()
    simple_graph_using_matrix.print_vertex_links(0)
    print()

    print("\n\n")
    simple_graph_using_matrix.remove_link(0, 0)
    print("\n\n")

    # simple_graph_using_matrix.print_pretty_matrix()
    simple_graph_using_matrix.print_matrix()
    print()
    simple_graph_using_matrix.print_vertex_amount()
    print()
    simple_graph_using_matrix.print_links_amount()
    print()
    simple_graph_using_matrix.print_vertex_links(0)
    print()
    simple_graph_using_matrix.BFS(0)
    simple_graph_using_matrix.DFS()


def teste2():
    simple_graph_using_matrix = Graph_Adjacent_Matrix(
        3, bigraph=False, weighted=True)
    simple_graph_using_matrix.add_link(0, 2, -5)
    simple_graph_using_matrix.add_link(2, 1, 3)
    simple_graph_using_matrix.add_link(0, 1, 2)

    # simple_graph_using_matrix.print_pretty_matrix()
    simple_graph_using_matrix.print_matrix()
    print()
    simple_graph_using_matrix.print_vertex_amount()
    print()
    simple_graph_using_matrix.print_links_amount()
    print()
    simple_graph_using_matrix.print_vertex_links(0)
    print()

    print("\n\n")
    simple_graph_using_matrix.remove_link(0, 0)
    print("\n\n")

    # simple_graph_using_matrix.print_pretty_matrix()
    simple_graph_using_matrix.print_matrix()
    print()
    simple_graph_using_matrix.print_vertex_amount()
    print()
    simple_graph_using_matrix.print_links_amount()
    print()
    simple_graph_using_matrix.print_vertex_links(0)
    print()
    simple_graph_using_matrix.BFS(0)
    simple_graph_using_matrix.DFS()
    simple_graph_using_matrix.dijkstra(0)
    print(simple_graph_using_matrix.bellman_ford(0))


if __name__ == '__main__':
    teste2()
