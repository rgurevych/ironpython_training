import fixture.group
from random import randint

def test_delete_group(app):
    main_window = app
    # Check if there is more then 1 group, add new group if fail (not possible to delete the last group)
    if len(fixture.group.get_group_list(main_window)) <= 1:
        fixture.group.add_new_group(main_window, "Group_for_deletion")
    old_groups_list = fixture.group.get_group_list(main_window)
    index = randint(0, len(old_groups_list))
    fixture.group.delete_group(main_window, index)
    new_groups_list = fixture.group.get_group_list(main_window)
    old_groups_list.pop(index)
    assert sorted(new_groups_list) == sorted(old_groups_list)