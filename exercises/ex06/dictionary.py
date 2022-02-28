"""Where I implent my skeleton functions for dictionaries."""

__author__ = "730391695"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of a dictionary."""
    final_dict: dict[str, str] = dict()
    for key in my_dictionary:
        if my_dictionary[key] in final_dict:
            raise KeyError("Value is repeated.")
        final_dict[my_dictionary[key]] = key
    return final_dict
  
 
def favorite_color(dictionary: dict[str, str]) -> str:
    """Will show what color is most liked within the group."""
    final_dict: dict[str, int] = dict()
    for key in dictionary:
        color = dictionary[key]
        if color in final_dict:
            final_dict[color] += 1
        else:
            final_dict[color] = 1
    max_value: int = 0
    fav_color: str = ""
    for key in final_dict:
        count = final_dict[key]
        if count > max_value:
            max_value = count
            fav_color = key
    return fav_color


def count(values: list[str]) -> dict[str, int]:
    """The amount of times a value is appeared in the list."""
    finale: dict[str, int] = dict()
    for i in values:
        if i in finale:
            finale[i] += 1
        else:
            finale[i] = 1
    return finale
