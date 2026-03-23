import pytest
from main import bubble


def test_unsorted_list():
    """Test bubble sort with an unsorted list"""
    input_list = [4, 1, 3, 9, 7]
    original_length = len(input_list)
    result = bubble(input_list)
    assert result == [1, 3, 4, 7, 9], "Output should be correctly sorted"
    assert len(result) == original_length, "No elements should be lost"
    assert sorted(input_list) == result, "All elements must be preserved"


def test_already_sorted():
    """Test bubble sort with an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    original_length = len(input_list)
    result = bubble(input_list)
    assert result == [1, 2, 3, 4, 5], "Already sorted list should remain unchanged"
    assert len(result) == original_length, "No elements should be lost"
    assert sorted(input_list) == result, "All elements must be preserved"


def test_reverse_sorted():
    """Test bubble sort with a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    original_length = len(input_list)
    result = bubble(input_list)
    assert result == [1, 2, 3, 4, 5], "Reverse sorted list should be sorted ascending"
    assert len(result) == original_length, "No elements should be lost"
    assert sorted(input_list) == result, "All elements must be preserved"


def test_empty_list():
    """Test bubble sort with an empty list"""
    input_list = []
    result = bubble(input_list)
    assert result == [], "Empty list should remain empty"
    assert len(result) == 0, "Length should be 0"


def test_single_element():
    """Test bubble sort with a single-element list"""
    input_list = [42]
    result = bubble(input_list)
    assert result == [42], "Single element list should be unchanged"
    assert len(result) == 1, "Length should be preserved"
    assert sorted(input_list) == result, "Element must be preserved"
