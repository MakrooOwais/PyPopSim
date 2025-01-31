"""
This module contains the base class structure for an ODE solving method.
"""

import numpy as np
from typing import Union, Callable, List


class Method:
    def __init__(
        self,
        f: Callable,
        f0: Union[int, float, np.ndarray, List[Union[int, float]]],
        tmin: float,
        tmax: float,
        h: float = 1e-2,
    ):
        """
        Initialize the Method solver.

        Args:
            f (Callable): The function to be solved.
            f0 (Union[float, np.ndarray]): The initial condition.
            tmin (float): The start time.
            tmax (float): The end time.
            h (float, optional): The step size. Defaults to 1e-2.
        """

        if isinstance(f0, (int, float)):
            f0 = np.array([f0])
        elif isinstance(f0, list):
            f0 = np.array(f0)

        self.f = f
        self.h = h
        self.f0 = f0
        
        self.res = [f0]

        self.tmin, self.tmax = tmin, tmax
        self.range = np.arange(tmin, tmax, h)

    def solve(self):
        """
        Solve the ODE using the specified method.

        Returns:
            np.ndarray: The solution array.
        """
        return np.zeros_like(self.range)
