"""
This module provides functionality to process user input, validate it, and perform
arithmetic or comparison operations on two numbers separated by an operator.

The supported operators are:
+ (addition), - (subtraction), * (multiplication), / (division),
< (less than), > (greater than), = (equality).

The module uses a doubly linked list (imported from the `dll` module) to represent
the input and perform operations on the parsed numbers.

Functions:
- main(): The entry point of the program.
- str_to_num(): Converts a doubly linked list of characters into an integer.
- validate_input(): Validates the input string for valid numbers and operators.
- parse_for_operators(): Finds the index of the first valid operator in the input.
"""

import operator

from dll import DoublyLinkedList, Node


def main() -> None:
    """
    Main function to process user input, validate it, and perform the specified operation
    on two numbers separated by an operator.

    The function supports the following operators:
    +, -, *, /, <, >, =

    Raises:
        ZeroDivisionError: If division by zero is attempted.
    """
    # TODO handle stacked operators => return error
    # TODO write tests

    print(
        """"Provide two numbers separated by a valid operator. The number can be negative.
    Valid operators: +, -, * , /, <, >, ="""
    )
    original_input = input("Input: ")
    cleaned_input = "".join(original_input.split())

    num_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }

    operator_map = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "<": lambda a, b: 1 if a < b else -1 if a > b else 0,
        ">": lambda a, b: -1 if a < b else 1 if a > b else 0,
        "=": lambda a, b: 0 if a == b else 1 if a < b else -1,
    }
    validate_input(cleaned_input, num_map, operator_map)

    original_input = DoublyLinkedList()
    for i in cleaned_input:
        original_input.append(i)

    operator_index = parse_for_operators(original_input, operator_map, num_map)
    first_half, second_half = original_input.split(operator_index)
    operation = operator_map.get(second_half.pop(0).data)
    first_num = str_to_num(first_half, num_map)
    second_num = str_to_num(second_half, num_map)

    # Handle division by zero
    if operation == operator.truediv and second_num == 0:
        raise ZeroDivisionError("Can't divide by zero")

    result = operation(first_num, second_num)
    print(str(result))


def str_to_num(input_string: "DoublyLinkedList", num_map: dict) -> int:
    """
    Converts a doubly linked list of characters representing a number into an integer.

    Args:
        input_string (DoublyLinkedList): The linked list containing the number as characters.
        num_map (dict): A mapping of character digits to their integer values.

    Returns:
        int: The integer representation of the number.
    """
    num = 0
    negative = False
    if input_string[0] == "-":
        input_string.pop(0)
        negative = True
    for node in input_string:
        num = (num * 10) + num_map[node.data]
    return num * -1 if negative else num


def validate_input(
    data: str,
    number_map: dict,
    operator_map: dict,
) -> None:
    """
    Validates the input string to ensure it contains only valid numbers and operators.

    Args:
        data (str): The input string to validate.
        number_map (dict): A mapping of valid number characters.
        operator_map (dict): A mapping of valid operator characters.

    Raises:
        ValueError: If the input contains invalid characters.
    """
    for char in data:
        if char not in number_map and char not in operator_map:
            raise ValueError("Character is not a number or operator. Exiting program.")


def parse_for_operators(
    data: "DoublyLinkedList", operator_map: dict, numbers: dict
) -> int | None:
    """
    Finds the index of the first valid operator in the doubly linked list.

    Args:
        data (DoublyLinkedList): The linked list containing the input data.
        operator_map (dict): A mapping of valid operator characters.
        numbers (dict): A mapping of valid number characters.

    Returns:
        int: The index of the first valid operator, or None if no operator is found.
    """
    operator_index = None
    node: "Node"
    for index, node in enumerate(data):
        if node.data in operator_map and node.previous_node is not None:
            if node.previous_node.data in numbers and (
                node.next_node.data in numbers or node.next_node.data == "-"
            ):
                operator_index = index
    return operator_index


if __name__ == "__main__":
    main()
