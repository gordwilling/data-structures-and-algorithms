

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user: str, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    def loop(g: Group):
        users = g.get_users()
        if user in users:
            return True
        child_groups = g.get_groups()
        for child_group in child_groups:
            return loop(child_group)
        return False

    return loop(group)


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    child.add_user("child_user")
    parent.add_group(child)

    print(is_user_in_group("sub_child_user", parent))
    # True

    print(is_user_in_group("sub_child_user", child))
    # True

    print(is_user_in_group("sub_child_user", sub_child))
    # True

    print(is_user_in_group("child_user", parent))
    # True

    print(is_user_in_group("child_user", child))
    # True

    print(is_user_in_group("child_user", sub_child))
    # False

    print(is_user_in_group("no_group_user", parent))
    # False

    print(is_user_in_group("no_group_user", child))
    # False

    print(is_user_in_group("no_group_user", sub_child))
    # False

