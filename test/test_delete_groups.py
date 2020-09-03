import random


def test_delete_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("add new group")
    old_lst = app.groups.get_group_list()
    group = random.choice(old_lst)
    app.groups.delete_exist_group(group)
    new_list = app.groups.get_group_list()
    old_lst.remove(group)
    assert sorted(old_lst) == sorted(new_list)
