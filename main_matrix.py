from graph import Graph_Adjacent_Matrix


def main_matrix():
    simple_graph_using_matrix = Graph_Adjacent_Matrix(5)
    simple_graph_using_matrix.add_link(0, 0)
    simple_graph_using_matrix.add_link(0, 4)
    simple_graph_using_matrix.add_link(1, 3)
    simple_graph_using_matrix.add_link(1, 4)
    simple_graph_using_matrix.add_link(2, 3)
    simple_graph_using_matrix.add_link(3, 4)

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
    simple_graph_using_matrix.DFS()


if __name__ == '__main__':
    main_matrix()
