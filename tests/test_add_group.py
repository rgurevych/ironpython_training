import fixture.group

def test_add_group(app, xlsx_groups):
    main_window = app
    group = xlsx_groups.name
    old_groups_list = fixture.group.get_group_list(main_window)
    fixture.group.add_new_group(main_window, group)
    new_groups_list = fixture.group.get_group_list(main_window)
    old_groups_list.append(group)
    assert sorted(new_groups_list) == sorted(old_groups_list)

