def test_add_group(app):
    old_lst = app.groups.get_group_list()
    app.groups.add_new_group("My group")
    new_lst = app.groups.get_group_list()
    old_lst.append("my group")
    assert sorted(old_lst) == sorted(new_lst)