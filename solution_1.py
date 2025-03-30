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
    print(
        """"Provide two numbers separated by a valid operator. The number can be negative.
    Valid operators: +, -, * , /, <, >, =, <=, >="""
    )
    string_to_solve = input("Input goes here: ")

    number_map = {
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
        "<": operator.lt,
        ">": operator.gt,
        "=": operator.eq,
    }
    validate_input(string_to_solve, number_map, operator_map)

    original_ll = DoublyLinkedList()
    for i in string_to_solve:
        original_ll.append(i)

    print(parse_for_operators(original_ll, operator_map, number_map))
    print(check_for_negatives(original_ll, operator_map, number_map))


def validate_input(
    data: str,
    number_map: dict,
    operator_map: dict,
):
    for char in data:
        if char not in number_map and char not in operator_map:
            raise ValueError("Character is not a number or operator. Exiting program.")


def check_for_negatives(data: "DoublyLinkedList", operators: dict, numbers: dict):
    first_is_negative = False
    second_is_negative = False
    operator = None

    for index, node in enumerate(data):
        if node.data == "-":
            if node.previous_node == None and node.next_node.data in numbers:
                first_is_negative = True
            elif (
                node.previous_node.data in operators and node.next_node.data in numbers
            ):
                second_is_negative = True
    return first_is_negative, second_is_negative


# ? could be done during the validate phase, to only iterate over the data once
# ? counterargument: separation of concerns, clean code
def parse_for_operators(
    data: "DoublyLinkedList", operator_map: dict, numbers: dict
) -> dict:
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

    def bisect(
        self, index: int, pop=True
    ) -> tuple["DoublyLinkedList", "DoublyLinkedList"]:
        if index < 0 or index >= self.length - 1:
            raise IndexError("Index out of range")

        position = 0
        current_node = self.head
        second_list = DoublyLinkedList()

        while current_node:
            if position == index:
                if current_node.previous_node == None:  # splitting at head
                    if pop:
                        second_list.head = current_node.next_node  # pop head node
                        # originally points to self.head
                        second_list.head.previous_node = None
                    else:
                        second_list.head = current_node  # reassign head node
                    # clean up
                    self.head = None
                    self.tail = None
                    self.length = 0
                    second_list.length = 1

                else:
                    if pop:
                        second_list.head = current_node.next_node
                        # -1 to account for pop removing an element
                        second_list.length = self.length - position - 1
                    else:
                        second_list.head = current_node
                        second_list.length = self.length - position

                    # clean up
                    second_list.tail = self.tail  # inherits the original tail
                    self.tail = current_node.previous_node
                    self.length = position
                    current_node.previous_node.next_node = None
                    second_list.head.previous_node = None
                return (self, second_list)
        current_node = current_node.next_node
        position += 1

    def pop(self, index) -> "Node":
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        current_node = self.head
        position = 0

        while current_node:
            if position == index:
                if current_node.previous_node == None:  # check for head
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

            if current_node.previous_node is None:  # next_node before swappping
                self.tail = self.head
                self.head = current_node
                return

            _recursive_helper(current_node.previous_node)  # next_node before swapping

        _recursive_helper(self.head)

    def iterative_reverse(self):
        if self.head is None:
            # empty list
            # ? raise ValuError instead?
            return

        current_node = self.head

        while current_node:
            next = current_node.next_node
            current_node.next_node = current_node.previous_node
            current_node.previous_node = next
            current_node = next

        self.head, self.tail = self.tail, self.head


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next_node = None
        self.previous_node = None


if __name__ == "__main__":
    main()
