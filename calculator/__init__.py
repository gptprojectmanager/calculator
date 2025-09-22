"""
Calculator Package

A Python calculator module providing basic arithmetic operations through
both programmatic interface and command-line interface.

This package contains:
- operations: Core arithmetic functions (add, subtract, multiply, divide)
- cli: Command-line interface for interactive calculator usage

Example:
    >>> from calculator import operations
    >>> operations.add(2, 3)
    5

    >>> from calculator.cli import main
    >>> main()  # Starts interactive calculator
"""

from . import operations
from . import cli

__version__ = "1.0.0"
__author__ = "Calculator Development Team"

# Expose main operations at package level for convenience
from .operations import add, subtract, multiply, divide

__all__ = [
    'operations',
    'cli',
    'add',
    'subtract',
    'multiply',
    'divide'
]