"""The functions for the create value project."""

from csv import DictReader


__author__ = "730391695"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of the csv into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Creates a list[str] of all the values within a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row orientated table into a column orientated table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produces a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
 
    for column in column_table:
        if number_of_rows > len(column_table[column]):
            return column_table

        i: int = 0 
        list_of_rows: list[str] = []
        while i < number_of_rows:
            list_of_rows.append(column_table[column][i])
            i += 1
        
        result[column] = list_of_rows
    
    return result


def select(table_column: dict[str, list[str]], names_of_column: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with only a specific subset of the original columns."""
    result_dict: dict[str, list[str]] = {}

    for column in table_column:
        if column in names_of_column:
            result_dict[column] = table_column[column]
    
    return result_dict


def concat(table_of_column: dict[str, list[str]], table_of_column_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column based tables combined."""
    result: dict[str, list[str]] = {}

    for column in table_of_column:
        result[column] = table_of_column[column]

    for column in table_of_column_2:
        if column in result:
            result[column] += table_of_column_2[column]
        else:
            result[column] = table_of_column_2[column]
    return result


def count(values_to_count: list[str]) -> dict[str, int]: 
    """Gives the amount of times a string is shown."""
    counted_dictionary: dict[str, int] = dict()
    for i in values_to_count:
        if i in counted_dictionary:
            counted_dictionary[i] += 1
        else:
            counted_dictionary[i] = 1
    return counted_dictionary


def count_greater_than(values: dict[str, list[int]], threshold: int) -> int:
    """Gives the amount of times a certain number greater than a number is shown in data."""
    for column in values:
        result: int = 0
        for key in values[column]:
            if key >= threshold:
                result += 1
            result
        return result
    return 0


def str_to_int(string: dict[str, list[str]]) -> dict[str, list[int]]:
    """Changes a dict of strings to inte."""
    result: dict[str, list[int]] = {}
 
    for column in string:
        list_of_rows: list[int] = []
        for i in string[column]:
            number: int = int(i)
            list_of_rows.append(number)
        result[column] = list_of_rows
    
    return result