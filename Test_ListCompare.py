import pytest
from ListCompare import ListCompare


def test_compare_list_one_greater():
    comparer = ListCompare([5, 6, 7], [1, 2, 3])
    result = comparer.compare_lists()
    assert result == "Первый список имеет большее среднее значение"


def test_compare_list_two_greater():
    comparer = ListCompare([1, 2, 3], [4, 5, 6])
    result = comparer.compare_lists()
    assert result == "Второй список имеет большее среднее значение"


def test_compare_lists_equal():
    comparer = ListCompare([1, 2, 3], [1, 2, 3])
    result = comparer.compare_lists()
    assert result == "Средние значения равны"


def test_compare_lists_empty():
    comparer = ListCompare([], [])
    result = comparer.compare_lists()
    assert result == "Средние значения равны"
