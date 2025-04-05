import sys
import unittest
from pathlib import Path

# Add the parent directory to sys.path so we can import the dll module
sys.path.append(str(Path(__file__).parent.parent))

from dll import DoublyLinkedList, Node


class TestNode(unittest.TestCase):
    """Test cases for the Node class."""

    def test_node_initialization(self):
        """Test that a Node is properly initialized with data."""
        data = "test_data"
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertIsNone(node.next_node)
        self.assertIsNone(node.previous_node)


class TestDoublyLinkedList(unittest.TestCase):
    """Test cases for the DoublyLinkedList class."""

    def test_empty_initialization(self):
        """Test that an empty list is properly initialized."""
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(dll.length, 0)

    def test_initialization_with_node(self):
        """Test initialization with a node."""
        node = Node("test_data")
        dll = DoublyLinkedList(node)
        self.assertEqual(dll.head, node)
        self.assertEqual(dll.tail, node)
        self.assertEqual(dll.length, 1)

    def test_append(self):
        """Test appending nodes to the list."""
        dll = DoublyLinkedList()

        # Append to empty list
        dll.append("first")
        self.assertEqual(dll.head.data, "first")
        self.assertEqual(dll.tail.data, "first")
        self.assertEqual(dll.length, 1)

        # Append to non-empty list
        dll.append("second")
        self.assertEqual(dll.head.data, "first")
        self.assertEqual(dll.tail.data, "second")
        self.assertEqual(dll.length, 2)
        self.assertEqual(dll.head.next_node, dll.tail)
        self.assertEqual(dll.tail.previous_node, dll.head)

    def test_push(self):
        """Test pushing nodes to the beginning of the list."""
        dll = DoublyLinkedList()

        # Push to empty list
        dll.push("first")
        self.assertEqual(dll.head.data, "first")
        self.assertEqual(dll.tail.data, "first")
        self.assertEqual(dll.length, 1)

        # Push to non-empty list
        dll.push("second")
        self.assertEqual(dll.head.data, "second")
        self.assertEqual(dll.tail.data, "first")
        self.assertEqual(dll.length, 2)
        self.assertEqual(dll.head.next_node, dll.tail)
        self.assertEqual(dll.tail.previous_node, dll.head)

    def test_iteration(self):
        """Test iteration through the list."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third"]

        for item in data:
            dll.append(item)

        nodes = list(dll)
        self.assertEqual(len(nodes), 3)
        self.assertEqual([node.data for node in nodes], data)

    def test_getitem(self):
        """Test accessing items by index."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third"]

        for item in data:
            dll.append(item)

        # Test valid indices
        self.assertEqual(dll[0], "first")
        self.assertEqual(dll[1], "second")
        self.assertEqual(dll[2], "third")

        # Test out of range indices
        with self.assertRaises(IndexError):
            _ = dll[-1]
        with self.assertRaises(IndexError):
            _ = dll[3]

    def test_getitem_empty_list(self):
        """Test accessing items in an empty list."""
        dll = DoublyLinkedList()

        with self.assertRaises(IndexError):
            _ = dll[0]

    def test_pop(self):
        """Test popping nodes from the list."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third", "fourth"]

        for item in data:
            dll.append(item)

        # Pop from middle
        popped = dll.pop(1)
        self.assertEqual(popped.data, "second")
        self.assertEqual(dll.length, 3)
        self.assertEqual([node.data for node in dll], ["first", "third", "fourth"])

        # Pop from beginning
        popped = dll.pop(0)
        self.assertEqual(popped.data, "first")
        self.assertEqual(dll.length, 2)
        self.assertEqual(dll.head.data, "third")

        # Pop from end
        popped = dll.pop(1)
        self.assertEqual(popped.data, "fourth")
        self.assertEqual(dll.length, 1)
        self.assertEqual(dll.tail.data, "third")

        # Pop last element
        popped = dll.pop(0)
        self.assertEqual(popped.data, "third")
        self.assertEqual(dll.length, 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        # Test pop from empty list
        with self.assertRaises(IndexError):
            dll.pop(0)

    def test_split_in_middle(self):
        """Test splitting the list in the middle."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third", "fourth"]

        for item in data:
            dll.append(item)

        # Split at index 1 (the node with "second")
        first_list, second_list = dll.split(1)

        # Check first list - should contain only "first"
        self.assertEqual(first_list.length, 1)
        self.assertEqual([node.data for node in first_list], ["first"])
        self.assertEqual(first_list.head.data, "first")
        self.assertEqual(first_list.tail.data, "first")

        # Check second list - should contain "second", "third", "fourth"
        self.assertEqual(second_list.length, 3)
        self.assertEqual(
            [node.data for node in second_list], ["second", "third", "fourth"]
        )
        self.assertEqual(second_list.head.data, "second")
        self.assertEqual(second_list.tail.data, "fourth")

    def test_split_at_head(self):
        """Test splitting the list at the head."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third"]

        for item in data:
            dll.append(item)

        first_list, second_list = dll.split(0)

        # Check first list
        self.assertEqual(first_list.length, 0)
        self.assertIsNone(first_list.head)
        self.assertIsNone(first_list.tail)

        # Check second list
        self.assertEqual(second_list.length, 3)
        self.assertEqual([node.data for node in second_list], data)

    def test_split_at_tail(self):
        """Test splitting the list at the tail."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third"]

        for item in data:
            dll.append(item)

        first_list, second_list = dll.split(2)

        # Check first list (should contain all elements)
        self.assertEqual(first_list.length, 3)
        self.assertEqual([node.data for node in first_list], data)

        # Check second list (should be empty)
        self.assertEqual(second_list.length, 0)
        self.assertIsNone(second_list.head)
        self.assertIsNone(second_list.tail)

    def test_recursive_reverse(self):
        """Test recursively reversing the list."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third"]

        for item in data:
            dll.append(item)

        dll.recursive_reverse()

        # Check that the list is reversed
        self.assertEqual([node.data for node in dll], list(reversed(data)))
        self.assertEqual(dll.head.data, "third")
        self.assertEqual(dll.tail.data, "first")

        # Test reversing empty list
        empty_dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            empty_dll.recursive_reverse()

    def test_iterative_reverse(self):
        """Test iteratively reversing the list."""
        dll = DoublyLinkedList()
        data = ["first", "second", "third"]

        for item in data:
            dll.append(item)

        dll.iterative_reverse()

        # Check that the list is reversed
        self.assertEqual([node.data for node in dll], list(reversed(data)))
        self.assertEqual(dll.head.data, "third")
        self.assertEqual(dll.tail.data, "first")

        # Test reversing empty list
        empty_dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            empty_dll.iterative_reverse()


if __name__ == "__main__":
    unittest.main()
