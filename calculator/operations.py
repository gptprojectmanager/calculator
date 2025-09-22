"""
Calculator Operations Module

This module contains the core arithmetic operations for the calculator.
All functions accept numeric input and return numeric results.

Functions:
    add(a, b): Returns the sum of a and b
    subtract(a, b): Returns the difference of a and b
    multiply(a, b): Returns the product of a and b
    divide(a, b): Returns the quotient of a and b

Example:
    >>> from calculator.operations import add, subtract
    >>> add(10, 5)
    15
    >>> subtract(10, 5)
    5
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.

    Args:
        a: The first number
        b: The second number

    Returns:
        The sum of a and b

    Example:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.7)
        6.2
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract two numbers.

    Args:
        a: The first number (minuend)
        b: The second number (subtrahend)

    Returns:
        The difference of a and b

    Example:
        >>> subtract(10, 3)
        7
        >>> subtract(5.5, 2.3)
        3.2
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Args:
        a: The first number
        b: The second number

    Returns:
        The product of a and b

    Example:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Divide two numbers.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient of a and b

    Raises:
        ZeroDivisionError: If b is zero

    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 3)
        2.3333333333333335
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b