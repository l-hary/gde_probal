def main() -> None:
    string_to_solve = input("Mit akarsz? ")

    # TODO
    # hash map implementation
    num_map = {"1": 1, "2": 2}
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    # TODO
    # input iteralasa operatorig, elso lista feltoltese elemekkel, operator tarolasa,
    # masodik lista feltoltese a maradek elemekkel
    # listak ertekenek szamolasa, matematikai muvelet elvegzese (if-elif-else,
    # vagy match-case)


def calculate_sum() -> None:
    "Use powers of 10 with index of element"
    pass


class LinkedList:
    """Linked lists are comprised of Nodes."""

    def __init__(self):
        self.head = None

    # TODO
    def __repr__(self):
        pass

    # TODO
    def __str__(self):
        pass

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def insert_at_beginning(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


class Node:
    """Each node should contain data and a reference to the next node at a minimum."""

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, next) -> None:
        self.next = next


if __name__ == "__main__":
    main()
