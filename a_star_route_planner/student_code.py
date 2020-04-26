from math import sqrt, inf


class GraphNode(object):
    def __init__(self, nid: int, x: float, y: float):
        self.nid = nid
        self.x = x
        self.y = y
        self.edges = []

    def add_child(self, child):
        self.edges.append(GraphEdge(child, euclidian_distance(self, child)))


class GraphEdge(object):
    def __init__(self, node: GraphNode, distance: float):
        self.node = node
        self.distance = distance


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)


class PathElement(object):
    def __init__(self, through_node, to_node, distance_from_start):
        self.through_node = through_node
        self.to_node = to_node
        self.distance_from_start = distance_from_start


def initial_distances(graph: Graph, start_node: GraphNode):
    distance_map = {node: inf for node in graph.nodes}
    distance_map[start_node] = 0
    return distance_map


def initial_shortest_paths(graph: Graph, start_node: GraphNode):
    shortest_path_map = {node: PathElement(None, node, inf) for node in graph.nodes}
    shortest_path_map[start_node] = PathElement(start_node, start_node, 0)
    return shortest_path_map


def build_graph(M):
    node_list = [GraphNode(id, x, y) for id, (x, y) in M.intersections.items()]
    graph = Graph(node_list)
    for id, child_ids in enumerate(M.roads, start=0):
        for child_id in child_ids:
            graph.add_edge(node_list[id], node_list[child_id])
    return graph


def euclidian_distance(node1: GraphNode, node2: GraphNode):
    return sqrt((node2.y - node1.y) ** 2 + (node2.x - node1.x) ** 2)


def path_to(start_node, end_node: GraphNode, path_element_map):
    path = []
    node = end_node
    path.append(node.nid)
    while node is not start_node:
        node = path_element_map[node].through_node
        path.append(node.nid)
    return list(reversed(path))


def shortest_path(M, start, goal):
    graph = build_graph(M)
    start_node = graph.nodes[start]
    goal_node = graph.nodes[goal]
    estimated_distances_to_goal = initial_distances(graph, start_node)
    shortest_paths = initial_shortest_paths(graph, start_node)

    from_node = None
    while from_node is not goal_node:
        from_node, estimated_distance = sorted(estimated_distances_to_goal.items(), key=lambda x: x[1])[0]
        distance = shortest_paths[from_node].distance_from_start
        del estimated_distances_to_goal[from_node]

        for edge in from_node.edges:
            if edge.node in estimated_distances_to_goal:
                distance_from_start = distance + edge.distance
                estimate_from_edge_to_goal = euclidian_distance(edge.node, goal_node)
                if distance_from_start + estimate_from_edge_to_goal < estimated_distances_to_goal[edge.node]:
                    estimated_distances_to_goal[edge.node] = distance_from_start + estimate_from_edge_to_goal
                if distance_from_start < shortest_paths[edge.node].distance_from_start:
                    shortest_paths[edge.node] = PathElement(from_node, edge.node, distance_from_start)

    return path_to(start_node, goal_node, shortest_paths)
