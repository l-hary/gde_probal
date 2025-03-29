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
    #! operator.le, operator.ge not supported
    print(
        """"Provide two numbers separated by a valid operator. The number can be negative.
    Valid operators: +, -, * , /, <, >, =, <=, >="""
    )
    nums = input("Input goes here: ")

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
        "<": operator.lt,
        ">": operator.gt,
        "=": operator.eq,
        # "<=": operator.le, #! FIX, current solution looks at Node.next_node
        # ">=": operator.ge,
    }


class LinkedList:

    def __init__(self, head: "Node" = None):
        self.head = head
        self.length = 0 if head is None else 1

    def push(self, data: object) -> None:
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.length += 1

    def recursive_reverse(self):
        if self.head is None:
            # empty list
            # ? raise ValuError instead?
            return

        def _recursive_helper(current_node: "Node", previous_node: "Node"):
            if current_node.next_node is None:  # base case, end of list
                self.head = current_node
                current_node.set_next_node(previous_node)
                return

            next_node = current_node.next_node  # store the original next node
            current_node.set_next_node(previous_node)  # reverses link

            _recursive_helper(current_node=next_node, previous_node=current_node)

        _recursive_helper(self.head, None)

    def iterative_reverse(self):
        if self.head is None:
            # empty list
            # ? raise ValuError instead?
            return

        previous_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next_node  # store the original next node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node


class Node:
    def __init__(self, data: object = None):
        self.data = data
        self.next_node = None

    def set_next_node(self, next_node: "Node") -> None:
        self.next_node = next_node


if __name__ == "__main__":
    main()
