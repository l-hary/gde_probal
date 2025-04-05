"""Készítsen sztring összeadó, kivonó, összehasonlító, szorzó algoritmusokat! (4 fő)
Az algoritmus paraméterként két pozitív egész számokat tartalmazó sztringet kap, melyekkel elvégzi a kívánt
műveletet. Összeadás esetén visszatér a két szám összegét tartalmazó sztringgel. Kivonás esetén a két szám
különbségét tartalmazó sztringgel. Összehasonlítás esetén a visszatérési érték legyen 1 ha az első szám a
kisebb, legyen -1 ha a második paraméterként kapott szám a kisebb és 0, ha egyenlő a két szám. Szorzás
esetén a szorzattal térjen vissza.
Valósítsa meg azokat az algoritmusokat is, amelyek a negatív számokat is kezelik!
"""

import operator


def main() -> None:

    # TODO handle stacked operators => return error
    # TODO separate DLL into a separate module
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

    # debug is for the weak <- print debug for president
    first_num = str_to_num(first_half, num_map)
    second_num = str_to_num(second_half, num_map)
    print(first_num)
    print(second_num)

    # Handle division by zero
    if operation == operator.truediv and second_num == 0:
        raise ZeroDivisionError("Can't divide by zero")

    result = operation(first_num, second_num)
    print(str(result))


def str_to_num(input_string: "DoublyLinkedList", num_map: dict) -> int:
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
):
    for char in data:
        if char not in number_map and char not in operator_map:
            raise ValueError("Character is not a number or operator. Exiting program.")


# ? could be done during the validate phase, to only iterate over the data once
# ? counterargument: separation of concerns, clean code
def parse_for_operators(
    data: "DoublyLinkedList", operator_map: dict, numbers: dict
) -> int:
    operator_index = None
    node: "Node"
    for index, node in enumerate(data):
        if node.data in operator_map and node.previous_node is not None:
            if node.previous_node.data in numbers and (
                node.next_node.data in numbers or node.next_node.data == "-"
            ):
                operator_index = index
    return operator_index


class DoublyLinkedList:
    # ? use setters instead of direct assignment ?

    def __init__(self, head: "Node" = None):
        self.head = head
        self.length = 0 if head is None else 1
        self.tail = head

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next_node
        return current.data

    def split(self, index: int) -> tuple["DoublyLinkedList", "DoublyLinkedList"]:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        position = 0
        current_node = self.head
        second_list = DoublyLinkedList()

        if index == self.length - 1:  # splitting at tail, second list is empty
            return self, second_list

        while current_node:
            if position == index:
                if current_node.previous_node is None:  # splitting at head
                    second_list.head = self.head
                    second_list.tail = self.tail
                    second_list.length = self.length

                    self.head = None
                    self.tail = None
                    self.length = 0
                    break

                # not splitting at head
                second_list.head = current_node
                second_list.tail = self.tail
                second_list.length = self.length - position

                # next step nulls the reference in memory
                first_list_new_tail = current_node.previous_node
                second_list.head.previous_node = None

                # update original list
                self.tail = first_list_new_tail
                self.tail.next_node = None
                self.length = position
                break

            current_node = current_node.next_node
            position += 1
        return self, second_list

    def pop(self, index: int) -> "Node | None":
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        current_node = self.head
        position = 0

        while current_node:
            if position == index:
                if current_node.previous_node is None:  # check for head
                    self.head = current_node.next_node
                    if self.head:  # at least one element remains in the list
                        self.head.previous_node = None  # update head pointer
                    else:  # empty list
                        self.tail = None

                elif current_node.next_node is None:  # popping the tail
                    self.tail = current_node.previous_node
                    self.tail.next_node = None  # update tail pointer

                else:
                    current_node.next_node.previous_node = current_node.previous_node
                    current_node.previous_node.next_node = current_node.next_node

                # clean up the removed node
                current_node.previous_node = None
                current_node.next_node = None
                self.length -= 1
                return current_node
            current_node = current_node.next_node
            position += 1
        return None

    def push(self, data: object) -> None:
        new_node = Node(data)
        new_node.next_node = self.head
        new_node.previous_node = None

        if self.head is None:
            self.tail = new_node
        else:
            self.head.previous_node = new_node
        self.head = new_node
        self.length += 1

    def append(self, data: object) -> None:
        new_node = Node(data)

        if self.head is None:
            new_node.previous_node = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def recursive_reverse(self):
        if self.head is None:
            # empty list
            # ? raise ValueError instead?
            return

        def _recursive_helper(current_node: "Node"):
            current_node.next_node, current_node.previous_node = (
                current_node.previous_node,
                current_node.next_node,
            )

            # base case, at the end of list
            if current_node.previous_node is None:  # next_node before swappping
                self.tail = self.head
                self.head = current_node
                return

            _recursive_helper(current_node.previous_node)  # next_node before swapping

        _recursive_helper(self.head)

    def iterative_reverse(self):
        if self.head is None:
            # empty list
            # ? raise ValueError instead?
            return

        current_node = self.head
        while current_node:
            current_node.next_node, current_node.previous_node = (
                current_node.previous_node,
                current_node.next_node,
            )
            current_node = current_node.previous_node  # next_node before swapping

        self.head, self.tail = self.tail, self.head


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next_node = None
        self.previous_node = None


if __name__ == "__main__":
    main()
