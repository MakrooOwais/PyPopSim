"""
This module provides numerical solvers for differential equations.
"""

from .fwdeul import *
from .modeul import *
from .rk2 import *
from .rk4 import *

from .method import Method


def get_method(name: str, **kwargs) -> Method:
    """
    Retrieves an instance of the requested numerical method.

    Args:
        name (str): The name of the numerical method to retrieve.
        **kwargs: Additional keyword arguments to pass to the method constructor.

    Returns:
        Method: An instance of the requested numerical method.
    """
    return eval(name)(**kwargs)
