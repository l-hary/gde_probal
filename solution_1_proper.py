def main() -> None:
    string_to_solve = input("Enter two numbers separated by an arithmetic operator: ")

    # TODO
    # hash map implementation
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
    valid_operators = ["+", "-", "/", "*"]
    original_input, operator_loc = validate_and_build_list(
        string_to_solve, num_map, valid_operators
    )
    operator = original_input[operator_loc]

    # input is reversed when filling up the LL,
    second_num, first_num = original_input.bisect(operator_loc)

    # reverse to original values after bisecting the original linked list
    # ? check whether inserting at the end is more efficient instead of reversing
    first_num.reverse()
    second_num.reverse()


def validate_and_build_list(string_to_solve, num_map, valid_operators):
    original_input = LinkedList()
    operator_loc = 0

    for index, char in enumerate(string_to_solve):
        if char not in valid_operators and char not in num_map.keys():
            raise ValueError("Character is not a number or operator. Exiting program.")
        if char in valid_operators:
            if index == 0:
                raise (
                    ValueError(
                        "First character is an operator, not a number. Exiting program."
                    )
                )
            if operator_loc == 0:
                operator_loc = index
            else:
                raise ValueError("More than one operators given. Exiting program.")
        original_input.insert_at_beginning(char)
    return original_input, operator_loc


def calculate_sum() -> None:
    "Use powers of 10 with index of element"
    pass


class LinkedList:
    """Linked lists are comprised of Nodes."""

    def __init__(self):
        self.head = None
        self.length = 0

    # TODO
    def __repr__(self):
        pass

    # TODO
    def __str__(self):
        pass

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.length

    def insert_at_beginning(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def bisect(
        self, index: int, keep_separator: bool = False
    ) -> tuple["LinkedList", "LinkedList"]:
        position = 0
        current_node = self.head
        previous_node = None
        second_list = LinkedList()

        while current_node:
            if position == index:
                if previous_node is None:
                    if keep_separator:
                        second_list.head = current_node
                    else:
                        second_list.head = current_node.next
                    self.head = None
                else:
                    if keep_separator:
                        previous_node.next = None
                        second_list.head = current_node
                    else:
                        previous_node.next = None
                        second_list.head = current_node.next
                return (self, second_list)
            previous_node = current_node
            current_node = current_node.next
            position += 1

    def find(self, item: any) -> int:
        current_node = self.head
        position = 0

        while current_node and current_node.data != item:
            current_node = current_node.next
            position += 1

        if current_node is None:
            raise ValueError("Item not found in list.")
        return position

    def reverse(self):
        def _helper(current_node, previous_node):
            if current_node.next is None:
                self.head = current_node
                current_node.next = previous_node
                return

            next_node = current_node.next
            current_node.next = previous_node

            _helper(next_node, current_node)

        if self.head == None:
            return
        _helper(self.head, None)


class Node:
    """Each node should contain data and a reference to the next node at a minimum."""

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, next) -> None:
        self.next = next


if __name__ == "__main__":
    main()
