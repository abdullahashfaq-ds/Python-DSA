class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            if vertex2 in self.adj_list[vertex1]:
                self.adj_list[vertex1].remove(vertex2)

            if vertex1 in self.adj_list[vertex2]:
                self.adj_list[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def __str__(self):
        graph = ""
        for vertex in self.adj_list:
            graph += f"{vertex}: {self.adj_list[vertex]}\n"
        return graph

    def display_aux(self, root, level, seen):
        if root is not None and not seen[root]:
            seen[root] = True
            print("    " * level, root, sep="")

            for child in self.adj_list.get(root, []):
                self.display_aux(child, level + 1, seen)

    def display(self):
        seen = {vertex: False for vertex in self.adj_list}

        if len(self.adj_list) > 0:
            start_vertex = next(iter(self.adj_list), None)

            if start_vertex is not None:
                self.display_aux(start_vertex, 0, seen)
        print()
