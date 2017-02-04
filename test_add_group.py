import fixture.group

def test_add_group(app):
    main_window = app
    old_groups_list = fixture.group.get_group_list(main_window)
    fixture.group.add_new_group(main_window, 'Test Group')
    new_groups_list = fixture.group.get_group_list(main_window)
    old_groups_list.append('Test Group')
    assert sorted(new_groups_list) == sorted(old_groups_list)


