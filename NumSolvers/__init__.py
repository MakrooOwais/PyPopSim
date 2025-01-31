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
        name (str): The name of the numerical method to retrieve. Options are:
            - 'FwdEuler': Requires kwargs 'tmin', 'tmax', and 'h'.
            - 'ModEuler': Requires kwargs 'tmin', 'tmax', 'h', and 'eps'.
            - 'RK2': Requires kwargs 'tmin', 'tmax', and 'h'.
            - 'RK4': Requires kwargs 'tmin', 'tmax', and 'h'.
        **kwargs: Additional keyword arguments to pass to the method constructor.

    Returns:
        Method: An instance of the requested numerical method.
    """
    options = ['FwdEuler', 'ModEuler', 'RK2', 'RK4']
    if name not in options:
        raise ValueError(f"Method '{name}' is not recognized. Available options are: {options}")
    return eval(name)(**kwargs)
