import pytest

def multiply_pairs(a, b):
    return [x * y for x, y in zip(a, b)]

def test_multiply_pairs():
    assert multiply_pairs([1, 2, 3], [4, 5, 6]) == [4, 10, 18]

def test_multiply_pairs_empty_lists():
    assert multiply_pairs([], []) == []

def test_multiply_pairs_unequal_length_lists():
    with pytest.raises(ValueError):
        multiply_pairs([1, 2, 3], [4, 5])

def test_multiply_pairs_non_numeric_values():
    with pytest.raises(TypeError):
        multiply_pairs([1, 2, 'a'], [4, 5, 6])
