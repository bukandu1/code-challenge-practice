"""Given an undirected graph ↴ with maximum degree
D, find a graph coloring ↴ using at most D + 1 colors.*/
"""
class GraphNode:

def __init__(self, label):
    self.label = label
    self.neighbors = set()
    self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]

def graph_coloring(graph):
    to_visit_list = []
    seen = set()

    to_visit_list.append(graph[0])
    seen = graph[0]

    #while we have nodes to visit
    #remove the first node from tree to review
    if the color is null:
        


graph_coloring(graph)
