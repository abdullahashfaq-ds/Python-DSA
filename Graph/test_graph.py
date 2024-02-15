import unittest
from graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        edges = [
            ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
            ('E', 'F'), ('F', 'G'), ('G', 'A')
        ]

        for vertex in vertices:
            self.graph.add_vertex(vertex)

        for edge in edges:
            self.graph.add_edge(edge[0], edge[1])

    def test_remove_edge(self):
        self.assertTrue(self.graph.remove_edge('A', 'B'))
        self.assertFalse(self.graph.remove_edge('A', 'H'))
        self.assertEqual(self.graph.adj_list, {
            'A': ['G'],
            'B': ['C'],
            'C': ['B', 'D'],
            'D': ['C', 'E'],
            'E': ['D', 'F'],
            'F': ['E', 'G'],
            'G': ['F', 'A']
        })

    def test_remove_vertex(self):
        self.assertTrue(self.graph.remove_vertex('A'))
        self.assertFalse(self.graph.remove_vertex('H'))
        self.assertEqual(self.graph.adj_list, {
            'B': ['C'],
            'C': ['B', 'D'],
            'D': ['C', 'E'],
            'E': ['D', 'F'],
            'F': ['E', 'G'],
            'G': ['F']
        })


if __name__ == '__main__':
    unittest.main()
