"""Where I test the functions in utils."""

from exercises.ex05.utils import sub
from exercises.ex05.utils import concat
from exercises.ex05.utils import only_evens 


def test_sub_diff_bounds() -> None:
    """Tests if the end parameter is greater than length of the list."""
    a_list: list[int] = [2, 4, 5]
    start = 1
    end = 4
    assert sub(a_list, start, end) == [4, 5]


def test_only_evens_multiple() -> None:
    """Tests a normal list of intergers."""
    evens: list[int] = [222, 3, 28, 9, 98]
    assert only_evens(evens) == [222, 28, 98]


def test_only_evens_empty() -> None:
    """Test the only evens empty list."""
    evens: list[int] = []
    assert only_evens(evens) == []


def test_only_evens_small() -> None:
    """Tests a small list of integers."""
    evens: list[int] = [2, 4]
    assert only_evens(evens) == [2, 4]


def test_sub_normal() -> None:
    """Tests the sub function normally."""
    a_list: list[int] = [1, 9, 3, 6, 100, 5, 7, 4]
    start = 2
    end = 6
    assert sub(a_list, start, end) == [3, 6, 100, 5]


def test_sub_empty() -> None:
    """Tests the sub function when the start parameter is negative."""
    a_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = -1
    end = 6
    assert sub(a_list, start, end) == [1, 2, 3, 4, 5, 6]


def test_concat_list() -> None:
    """Tests the concat function for combining lists."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_big_list() -> None:
    """Tests the concat function with a big list."""
    list1: list[int] = [1, 2, 3, 4, 5, 6]
    list2: list[int] = [7, 8, 9, 10, 11, 12]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_concat_empty() -> None:
    """Tests the concat function with an empty list."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []