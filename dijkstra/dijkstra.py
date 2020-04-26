import math


class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


class PathElement(object):
    def __init__(self, through_node, to_node, distance_from_start):
        self.through_node = through_node
        self.to_node = to_node
        self.distance_from_start = distance_from_start


def path_to(end_node, path_element_map):
    path = []
    node = end_node
    path.append(node)
    distance = path_element_map[node].distance_from_start
    while distance != 0:
        node = path_element_map[node].through_node
        path.append(node)
        distance = path_element_map[node].distance_from_start
    return path


def initial_distances(start_node):
    distance_map = {node: math.inf for node in graph.nodes}
    distance_map[start_node] = 0
    return distance_map


def dijkstra(start_node, end_node):
    distances = initial_distances(start_node)
    shortest_paths = {
        start_node: PathElement(start_node, start_node, 0)
    }

    while distances:
        from_node, distance = sorted(distances.items(), key=lambda x: x[1])[0]
        del distances[from_node]
        for edge in from_node.edges:
            if edge.node in distances:
                if distance + edge.distance < distances[edge.node]:
                    distances[edge.node] = distance + edge.distance
                    shortest_paths[edge.node] = PathElement(from_node, edge.node, distance + edge.distance)

    for _, v in shortest_paths.items():
        print(f"{v.through_node.value} -> {v.to_node.value}: {v.distance_from_start}")

    path = path_to(end_node, shortest_paths)
    while path:
        node = path.pop()
        print(node.value, end=" -> ")
    print("Done")

    return shortest_paths[end_node].distance_from_start


if __name__ == '__main__':
    node_u = GraphNode('U')
    node_d = GraphNode('D')
    node_a = GraphNode('A')
    node_c = GraphNode('C')
    node_i = GraphNode('I')
    node_t = GraphNode('T')
    node_y = GraphNode('Y')

    graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
    graph.add_edge(node_u, node_a, 4)
    graph.add_edge(node_u, node_c, 6)
    graph.add_edge(node_u, node_d, 3)
    graph.add_edge(node_d, node_u, 3)
    graph.add_edge(node_d, node_c, 4)
    graph.add_edge(node_a, node_u, 4)
    graph.add_edge(node_a, node_i, 7)
    graph.add_edge(node_c, node_d, 4)
    graph.add_edge(node_c, node_u, 6)
    graph.add_edge(node_c, node_i, 4)
    graph.add_edge(node_c, node_t, 5)
    graph.add_edge(node_i, node_a, 7)
    graph.add_edge(node_i, node_c, 4)
    graph.add_edge(node_i, node_y, 4)
    graph.add_edge(node_t, node_c, 5)
    graph.add_edge(node_t, node_y, 5)
    graph.add_edge(node_y, node_i, 4)
    graph.add_edge(node_y, node_t, 5)

    print(f'Shortest Distance from {node_u.value} to {node_y.value} is {dijkstra(node_u, node_y)}', end="")
    print()
