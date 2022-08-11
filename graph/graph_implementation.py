class Graph:
    def __init__(self):
        self.adj_list = {}

    # O(1)
    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True

        return False

    # O(1)
    def add_edge(self, vertex1, vertex2) -> bool:
        if vertex1 not in self.adj_list:
            self.adj_list[vertex1] = []
        if vertex2 not in self.adj_list:
            self.adj_list[vertex2] = []

        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

        return True

    def remove_edge(self, vertex1, vertex2) -> bool:
        """
        Remove an edge from vertex x.
        O(M) = O(deg(x)) ~ O(E), deg(x) = outdegree of x = the numbers of neighbors of x
        Worst case = O(V) when x has V-1 neighbors
        -> in sparse graphs the operation is faster

        :param vertex1:
        :param vertex2:
        :return: True if remove successfully
        """
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return False

        try:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
        except ValueError:
            pass

        return True

    # O(V + E)
    def remove_vertex(self, vertex) -> bool:
        if vertex in self.adj_list:
            neighbors = self.adj_list[vertex]
            for neighbor in neighbors:
                self.adj_list[neighbor].remove(vertex)

            del self.adj_list[vertex]
            return True

        return False

    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")
        print("-----" * 10)


if __name__ == "__main__":
    my_graph = Graph()

    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")

    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("A", "D")
    my_graph.add_edge("B", "D")
    my_graph.add_edge("C", "D")

    my_graph.print_graph()

    # my_graph.remove_edge("A", "B")
    # my_graph.remove_edge("A", "C")
    my_graph.remove_vertex("D")

    my_graph.print_graph()
