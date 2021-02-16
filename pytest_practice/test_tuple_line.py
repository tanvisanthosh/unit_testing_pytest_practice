#test_tuple_line.py

def test_slope_line():
    from tuple_line import slope_line
    result = slope_line(1, 1, 2, 2, 4)
    expected = 4
    assert result == expected
