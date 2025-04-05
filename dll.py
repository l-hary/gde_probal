"""
Doubly Linked List Implementation.

This module provides a doubly linked list data structure implementation with
various operations such as append, push, pop, split, and reverse. The implementation
consists of a DoublyLinkedList class and a Node class.

Classes:
    DoublyLinkedList: A doubly linked list implementation with various operations.
    Node: A node in the doubly linked list containing data and pointers to adjacent nodes.
"""


class DoublyLinkedList:
    """
    A doubly linked list implementation with various operations.

    This class implements a doubly linked list data structure where each node
    contains a reference to both the next and previous nodes, allowing for
    efficient traversal in both directions.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
        length (int): The number of nodes in the list.
    """

    def __init__(self, head: "Node" = None):
        """
        Initialize a new doubly linked list.

        Args:
            head (Node, optional): The first node of the list. Defaults to None.
        """
        self.head = head
        self.length = 0 if head is None else 1
        self.tail = head

    def __iter__(self):
        """
        Iterate through the nodes of the list.

        Yields:
            Node: Each node in the list, starting from the head.
        """
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def __getitem__(self, index):
        """
        Get the data of the node at the specified index.

        Args:
            index (int): The index of the node to access.

        Returns:
            object: The data of the node at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next_node
        return current.data

    def split(self, index: int) -> tuple["DoublyLinkedList", "DoublyLinkedList"]:
        """
        Split the list into two at the specified index.

        Args:
            index (int): The index at which to split the list.

        Returns:
            tuple[DoublyLinkedList, DoublyLinkedList]: A tuple containing the original list
                up to the index and a new list from the index onwards.

        Raises:
            IndexError: If the index is out of range.
        """
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
        """
        Remove and return the node at the specified index.

        Args:
            index (int): The index of the node to remove.

        Returns:
            Node | None: The removed node, or None if the list is empty.

        Raises:
            IndexError: If the index is out of range.
        """
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
        """
        Add a new node with the given data at the beginning of the list.

        Args:
            data (object): The data to store in the new node.
        """
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
        """
        Add a new node with the given data at the end of the list.

        Args:
            data (object): The data to store in the new node.
        """
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
        """
        Reverse the list recursively by swapping each node's next and previous pointers.

        This method changes the order of nodes in the list by recursively traversing
        the list and swapping the next_node and previous_node pointers for each node.

        Raises:
            ValueError: If the list is empty.
        """
        if self.head is None:
            raise ValueError("Cannot reverse an empty list.")

        def _recursive_helper(current_node: "Node"):
            """
            Helper function to recursively reverse the list.

            Args:
                current_node (Node): The current node being processed.
            """
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
        """
        Reverse the list iteratively by swapping each node's next and previous pointers.

        This method changes the order of nodes in the list by iteratively traversing
        the list and swapping the next_node and previous_node pointers for each node.

        Raises:
            ValueError: If the list is empty.
        """
        if self.head is None:
            raise ValueError("Cannot reverse an empty list.")

        current_node = self.head
        while current_node:
            current_node.next_node, current_node.previous_node = (
                current_node.previous_node,
                current_node.next_node,
            )
            current_node = current_node.previous_node  # next_node before swapping

        self.head, self.tail = self.tail, self.head


class Node:
    """
    A node in a doubly linked list.

    Each node contains data and references to both the next and previous nodes
    in the list, enabling efficient traversal in both directions.

    Attributes:
        data (object): The data stored in the node.
        next_node (Node): Reference to the next node in the list.
        previous_node (Node): Reference to the previous node in the list.
    """

    def __init__(self, data: object):
        """
        Initialize a new node with the given data.

        Args:
            data (object): The data to store in the node.
        """
        self.data = data
        self.next_node = None
        self.previous_node = None
