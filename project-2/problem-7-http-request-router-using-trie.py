from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_list, handler):
        node = self.root
        for path in path_list:
            node = node.children[path]
        node.handler = handler

    def find(self, path_list):
        node = self.root
        for path in path_list:
            node = node.children[path]
        return node.handler


class Router:
    def __init__(self, root_handler, default_handler):
        self.root = RouteTrie(root_handler)
        self.default_handler = default_handler

    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        self.root.insert(path_list, handler)

    def lookup(self, path):
        path_list = self.split_path(path)
        handler = self.root.find(path_list)
        return handler if handler else self.default_handler

    @staticmethod
    def split_path(path):
        return filter(lambda s: s != "", path.split("/"))


if __name__ == '__main__':

    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    print(router.lookup(""))
    # 'root handler'

    print(router.lookup("/"))
    # 'root handler'

    print(router.lookup("/home"))
    # 'not found handler'

    print(router.lookup("/home/about"))
    # 'about handler'

    print(router.lookup("/home/about/"))
    # 'about handler'

    print(router.lookup("/home/about/me"))
    # 'not found handler'

    print(router.lookup("////"))
    # 'root handler'

    print(router.lookup("//home//about//"))
    # 'about handler'


