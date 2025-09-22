"""
Calculator Command Line Interface

This module provides a command-line interface for the calculator,
allowing users to perform arithmetic operations interactively.

The CLI supports:
- Interactive mode for continuous calculations
- Single command execution
- Input validation and error handling
- User-friendly prompts and messages

Example:
    $ python -m calculator.cli
    Welcome to Calculator!
    Enter 'quit' to exit.
    > 5 + 3
    8
    > 10 / 2
    5.0
    > quit
    Goodbye!
"""

import sys
import re
from typing import Optional, Tuple
from .operations import add, subtract, multiply, divide


def parse_expression(expression: str) -> Optional[Tuple[float, str, float]]:
    """
    Parse a mathematical expression string.

    Args:
        expression: String containing a mathematical expression (e.g., "5 + 3")

    Returns:
        Tuple of (first_number, operator, second_number) if valid, None otherwise

    Example:
        >>> parse_expression("5 + 3")
        (5.0, '+', 3.0)
        >>> parse_expression("invalid")
        None
    """
    # Remove whitespace and match pattern: number operator number
    pattern = r'^(-?\d*\.?\d+)\s*([+\-*/])\s*(-?\d*\.?\d+)$'
    match = re.match(pattern, expression.strip())

    if match:
        try:
            num1 = float(match.group(1))
            operator = match.group(2)
            num2 = float(match.group(3))
            return (num1, operator, num2)
        except ValueError:
            return None
    return None


def calculate(num1: float, operator: str, num2: float) -> float:
    """
    Perform calculation based on operator.

    Args:
        num1: First number
        operator: Mathematical operator (+, -, *, /)
        num2: Second number

    Returns:
        Result of the calculation

    Raises:
        ValueError: If operator is not supported
        ZeroDivisionError: If dividing by zero

    Example:
        >>> calculate(5, '+', 3)
        8.0
        >>> calculate(10, '/', 2)
        5.0
    """
    operations_map = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    if operator not in operations_map:
        raise ValueError(f"Unsupported operator: {operator}")

    return operations_map[operator](num1, num2)


def print_welcome():
    """Print welcome message and usage instructions."""
    print("Welcome to Calculator!")
    print("Enter mathematical expressions like: 5 + 3, 10 / 2, etc.")
    print("Supported operations: + (add), - (subtract), * (multiply), / (divide)")
    print("Enter 'quit' or 'exit' to close the calculator.")
    print("-" * 50)


def print_goodbye():
    """Print goodbye message."""
    print("Thank you for using Calculator. Goodbye!")


def interactive_mode():
    """
    Run the calculator in interactive mode.

    Continuously prompts user for expressions until they choose to quit.
    Handles input validation and error reporting.
    """
    print_welcome()

    while True:
        try:
            user_input = input("> ").strip()

            # Check for quit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print_goodbye()
                break

            # Skip empty input
            if not user_input:
                continue

            # Parse and calculate
            parsed = parse_expression(user_input)
            if parsed is None:
                print("Error: Invalid expression format. Please use: number operator number")
                print("Example: 5 + 3")
                continue

            num1, operator, num2 = parsed
            result = calculate(num1, operator, num2)
            print(f"{result}")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled. Enter 'quit' to exit.")
        except EOFError:
            print("\nGoodbye!")
            break


def main():
    """
    Main entry point for the calculator CLI.

    Can be called directly or used as a module:
    - python -m calculator.cli
    - from calculator.cli import main; main()
    """
    try:
        interactive_mode()
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()