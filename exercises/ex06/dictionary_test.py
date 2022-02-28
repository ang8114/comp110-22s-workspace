"""The unit tests for the dictionary functions in dictionart.py."""

__author__ = "730391695"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count


def test_invert_none() -> None:
    """Tests when there is nothing in the dictionary."""
    my_dictionary: dict[str, str] = dict()
    assert invert(my_dictionary) == {}


def test_invert_normal() -> None:
    """Tests the invert function when there is an input."""
    my_dictionary: dict[str, str] = {"No": "Way", "Yes": "Nope"}
    assert invert(my_dictionary) == {"Way": "No", "Nope": "Yes"}


def test_invert_numbers() -> None:
    """Tests the invert function with a string of numbers."""
    my_dictionary: dict[str, str] = {"1": "2", "3": "4", "5": "6"}
    assert invert(my_dictionary) == {"2": "1", "4": "3", "6": "5"}


def test_favorite_color() -> None:
    """Tests which color is most liked."""
    final_dict: dict[str, str] = {"Angela": "Blue", "Emma": "Purple", "Olivia": "Blue", "Mack": "Blue"}
    assert favorite_color(final_dict) == ("Blue")


def test_favorite_color_again() -> None:
    """Tests which color is most liked."""
    final_dict: dict[str, str] = {"Angela": "Pink", "Emma": "Yellow", "Olivia": "Pink", "Mack": "Blue"}
    assert favorite_color(final_dict) == ("Pink")


def test_favorite_color_tied() -> None:
    """Tests when there is a tie in favorite colors."""
    final_dict: dict[str, str] = {"Angela": "Pink", "Emma": "Yellow"}
    assert favorite_color(final_dict) == ("Pink")


def test_count_normal() -> None:
    """Tests the amount of times a string is repeated in the list."""
    values: list[str] = ["pink", "pink", "blue", "green", "pink"]
    assert count(values) == {"pink": 3, "blue": 1, "green": 1}


def test_count_empty() -> None:
    """Tests the count when the list is empty."""
    values: list[str] = [""]
    assert count(values) == {"": 1}


def test_count_normal_again() -> None:
    """Tests the amount of times a string is repeated in the list."""
    values: list[str] = ["ice", "tea", "coffee", "coffee", "ice"]
    assert count(values) == {"ice": 2, "tea": 1, "coffee": 2}