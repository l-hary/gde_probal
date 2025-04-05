import sys
import unittest
from pathlib import Path
from unittest.mock import patch

# Add the parent directory to sys.path so we can import the main module
sys.path.append(str(Path(__file__).parent.parent))

from dll import DoublyLinkedList, Node
from main import main, parse_for_operators, str_to_num, validate_input


class TestMain(unittest.TestCase):
    """Tests for the main.py module."""

    def setUp(self):
        """Set up common test data."""
        self.num_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        self.operator_map = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "<": lambda a, b: 1 if a < b else -1 if a > b else 0,
            ">": lambda a, b: -1 if a < b else 1 if a > b else 0,
            "=": lambda a, b: 0 if a == b else 1 if a < b else -1,
        }

    def test_str_to_num_positive(self):
        """Test converting a linked list of digits to a positive number."""
        # Create a linked list with "123"
        dll = DoublyLinkedList()
        for char in "123":
            dll.append(char)

        result = str_to_num(dll, self.num_map)
        self.assertEqual(result, 123)

    def test_str_to_num_negative(self):
        """Test converting a linked list of digits to a negative number."""
        # Create a linked list with "-456"
        dll = DoublyLinkedList()
        for char in "-456":
            dll.append(char)

        result = str_to_num(dll, self.num_map)
        self.assertEqual(result, -456)

    def test_str_to_num_zero(self):
        """Test converting a linked list with "0" to the number 0."""
        dll = DoublyLinkedList()
        dll.append("0")

        result = str_to_num(dll, self.num_map)
        self.assertEqual(result, 0)

    def test_str_to_num_negative_zero(self):
        """Test converting a linked list with "-0" to the number 0."""
        dll = DoublyLinkedList()
        for char in "-0":
            dll.append(char)

        result = str_to_num(dll, self.num_map)
        self.assertEqual(result, 0)

    def test_validate_input_valid(self):
        """Test validating input with valid characters."""
        # Valid input with numbers and operators
        valid_inputs = [
            "123+456",
            "789-321",
            "42*56",
            "100/5",
            "10<20",
            "30>20",
            "15=15",
        ]

        for input_str in valid_inputs:
            # This should not raise an exception
            validate_input(input_str, self.num_map, self.operator_map)

    def test_validate_input_invalid(self):
        """Test validating input with invalid characters."""
        # Invalid input with characters not in maps
        invalid_inputs = ["abc", "123$456", "x+y", "10%2"]

        for input_str in invalid_inputs:
            with self.assertRaises(ValueError):
                validate_input(input_str, self.num_map, self.operator_map)

    def test_parse_for_operators_addition(self):
        """Test parsing for addition operator."""
        dll = DoublyLinkedList()
        for char in "123+456":
            dll.append(char)

        index = parse_for_operators(dll, self.operator_map, self.num_map)
        self.assertEqual(index, 3)  # "+ is at index 3"

    def test_parse_for_operators_subtraction(self):
        """Test parsing for subtraction operator."""
        dll = DoublyLinkedList()
        for char in "123-456":
            dll.append(char)

        index = parse_for_operators(dll, self.operator_map, self.num_map)
        self.assertEqual(index, 3)  # "- is at index 3"

    def test_parse_for_operators_negative_numbers(self):
        """Test parsing with negative numbers."""
        dll = DoublyLinkedList()
        for char in "-123+-456":
            dll.append(char)

        # The '+' operator should be found at index 4
        index = parse_for_operators(dll, self.operator_map, self.num_map)
        self.assertEqual(index, 4)

    def test_parse_for_operators_no_operator(self):
        """Test parsing when no valid operator exists."""
        dll = DoublyLinkedList()
        for char in "12345":
            dll.append(char)

        index = parse_for_operators(dll, self.operator_map, self.num_map)
        self.assertIsNone(index)

    def test_main_addition(self):
        """Test main function with addition operation."""
        with patch("builtins.input", return_value="123 + 456"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("579")

    def test_main_subtraction(self):
        """Test main function with subtraction operation."""
        with patch("builtins.input", return_value="123 - 456"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("-333")

    def test_main_multiplication(self):
        """Test main function with multiplication operation."""
        with patch("builtins.input", return_value="123 * 2"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("246")

    def test_main_division(self):
        """Test main function with division operation."""
        with patch("builtins.input", return_value="100 / 5"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("20.0")

    def test_main_division_by_zero(self):
        """Test main function with division by zero."""
        with patch("builtins.input", return_value="100 / 0"), self.assertRaises(
            ZeroDivisionError
        ):
            main()

    def test_main_less_than_true(self):
        """Test main function with less than operation (true case)."""
        with patch("builtins.input", return_value="5 < 10"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("1")  # 1 indicates true for < operator

    def test_main_less_than_false(self):
        """Test main function with less than operation (false case)."""
        with patch("builtins.input", return_value="10 < 5"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("-1")  # -1 indicates false for < operator

    def test_main_greater_than_true(self):
        """Test main function with greater than operation (true case)."""
        with patch("builtins.input", return_value="10 > 5"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("1")  # 1 indicates true for > operator

    def test_main_greater_than_false(self):
        """Test main function with greater than operation (false case)."""
        with patch("builtins.input", return_value="5 > 10"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("-1")  # -1 indicates false for > operator

    def test_main_equality_true(self):
        """Test main function with equality operation (true case)."""
        with patch("builtins.input", return_value="10 = 10"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("0")  # 0 indicates equality

    def test_main_equality_false(self):
        """Test main function with equality operation (false case)."""
        with patch("builtins.input", return_value="5 = 10"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            # For equality, 1 means first < second
            mock_print.assert_any_call("1")

    def test_main_with_spaces(self):
        """Test main function with input containing spaces."""
        with patch("builtins.input", return_value="  123   +  456  "), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("579")

    def test_main_with_negative_numbers(self):
        """Test main function with negative numbers."""
        with patch("builtins.input", return_value="-123 + -456"), patch(
            "builtins.print"
        ) as mock_print:
            main()
            mock_print.assert_any_call("-579")


if __name__ == "__main__":
    unittest.main()
