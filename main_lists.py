from adjacent_list import Graph_Adjacent_List


def teste1():
    simple_graph_using_lists = Graph_Adjacent_List(4)
    simple_graph_using_lists.add_link(0, 1)
    simple_graph_using_lists.add_link(0, 3)
    simple_graph_using_lists.add_link(1, 0)
    simple_graph_using_lists.add_link(1, 2)
    simple_graph_using_lists.add_link(2, 1)
    simple_graph_using_lists.add_link(3, 0)

    simple_graph_using_lists.print_lists()
    print()
    simple_graph_using_lists.print_vertex()
    print()
    simple_graph_using_lists.print_links()
    print()
    simple_graph_using_lists.print_vertex_links(0)

    print("\n\n")
    simple_graph_using_lists.remove_link(0, 0)
    print("\n\n")

    simple_graph_using_lists.print_lists()
    print()
    simple_graph_using_lists.print_vertex()
    print()
    simple_graph_using_lists.print_links()
    print()
    simple_graph_using_lists.print_vertex_links(0)
    print()
    simple_graph_using_lists.BFS(0)
    simple_graph_using_lists.DFS()


def teste2():
    simple_graph_using_lists = Graph_Adjacent_List(
        4, bigraph=False, weighted=True)
    simple_graph_using_lists.print_lists()
    simple_graph_using_lists.add_link(0, 1, 2)
    simple_graph_using_lists.add_link(1, 2, 3)
    simple_graph_using_lists.add_link(0, 2, 4)
    simple_graph_using_lists.print_lists()
    simple_graph_using_lists.DFS()
    print(simple_graph_using_lists.edge_weights)
    simple_graph_using_lists.dijkstra(0)


def teste3():
    simple_graph_using_lists = Graph_Adjacent_List(
        7, bigraph=False, weighted=True)
    simple_graph_using_lists.add_link(0, 1, 2)
    simple_graph_using_lists.add_link(0, 2, 6)
    simple_graph_using_lists.add_link(1, 3, 5)
    simple_graph_using_lists.add_link(2, 3, 8)
    simple_graph_using_lists.add_link(3, 5, 15)
    simple_graph_using_lists.add_link(3, 4, 10)
    simple_graph_using_lists.add_link(4, 5, 6)
    simple_graph_using_lists.add_link(4, 6, 2)
    simple_graph_using_lists.add_link(5, 6, 6)
    simple_graph_using_lists.dijkstra(0)


if __name__ == '__main__':
    teste3()
