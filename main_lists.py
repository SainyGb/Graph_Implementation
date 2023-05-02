from graph import Graph_Adjacent_List


def main_lists():
    simple_graph_using_lists = Graph_Adjacent_List(5)
    simple_graph_using_lists.add_link(0, 0)
    simple_graph_using_lists.add_link(0, 4)
    simple_graph_using_lists.add_link(1, 1)
    simple_graph_using_lists.add_link(1, 4)
    simple_graph_using_lists.add_link(2, 3)
    simple_graph_using_lists.add_link(3, 4)
    simple_graph_using_lists.add_link(4, 0)

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


if __name__ == '__main__':
    main_lists()
