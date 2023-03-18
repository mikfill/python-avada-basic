from pythagoras_triangle import is_pythagoras_triangle


def test_valid_triangles():
    assert is_pythagoras_triangle([5, 3, 4]) == True
    assert is_pythagoras_triangle([6, 8, 10]) == True


def test_invalid_triangles():
    assert is_pythagoras_triangle([100, 3, 65]) == False
    assert is_pythagoras_triangle([-5, 3, 4]) == None
