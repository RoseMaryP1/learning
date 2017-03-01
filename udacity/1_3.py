class Node(object):
    def __init__(self, id):
        self.links = set()
        self.dimension = 0
        self.id = id

    def link(self, node):
        self.links.add(node)
        self.dimension += 1
        node.links.add(self)
        node.dimension += 1

    def unlink(self, node):
        self.links.remove(node)
        node.links.remove(self)

    def follow(self):
        next_node = self.links.pop()
        next_node.links.remove(self)
        return next_node


def find_eulerian_tour(paths):
    nodes = []
    graph = {}

    # Parse all the paths into our graph.
    for path in paths:
        path_start = path[0]
        path_end = path[1]
        if not graph.has_key(path_start):
            graph[path_start] = Node(path_start)
        if not graph.has_key(path_end):
            graph[path_end] = Node(path_end)
        graph[path_start].link(graph[path_end])

    # Ensure there are the right amount of odd dimensions.
    odds = []
    for node in graph.values():
        if (node.dimension % 2) != 0:
            odds.append(node)
    if len(odds) != 0 and len(odds) != 2:
        raise Exception("can't create a tour with %i odd nodes." % len(odds))

    # Find the correct start and end points.
    if len(odds) == 2:
        last = odds[0]
        end = odds[1]
    else:
        last = end = graph.get(paths[0][0])

    # Follow all the paths.
    nodes.append(last.id)
    last = last.follow()
    while last != end or len(last.links) != 0:
        nodes.append(last.id)
        last = last.follow()
    nodes.append(end.id)
    return nodes

print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])

print find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)])

print find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)])

print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])



