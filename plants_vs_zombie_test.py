from plants_vs_zombie import is_plants_win_zombies


def test_valid_values():
    assert is_plants_win_zombies([2, 4, 6, 8], [1, 3, 5, 7]) == True
    assert is_plants_win_zombies([2, 4, 0, 8], [1, 3, 5, 7]) == True
    assert is_plants_win_zombies([1, 2, 1, 1], [2, 1, 1, 1]) == True


def test_invalid_values():
    assert is_plants_win_zombies([2, 4], [1, 3, 5, 7]) == False
