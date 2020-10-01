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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent_user = "parent_user"

child.add_group(sub_child)
parent.add_group(child)
parent.add_user(parent_user)


def get_all_users_in_groups(user, group):
    users = group.get_users()
    groups = group.get_groups()

    for group in groups:
        users.extend(get_all_users_in_groups(user, group))

    return users


def is_user_in_group(user, group):
    if not user or not group:
        return False
    return user in get_all_users_in_groups(user, group)


print('Should return True:', is_user_in_group(parent_user, parent))
# returns True

print('Should return True:', is_user_in_group(sub_child_user, parent))
# returns True

print('Should return False:', is_user_in_group(parent_user, child))
# returns False

print('Should return False:', is_user_in_group(None, child))
# returns False

print('Should return False:', is_user_in_group(parent_user, None))
# returns False
