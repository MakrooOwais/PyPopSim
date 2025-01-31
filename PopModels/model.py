"""
This module defines the PopModel class for simulating population models using various numerical methods.
"""

import numpy as np
from typing import Union, List, Optional
from NumSolvers import get_method, Method


class PopModel:
    """_summary_
    This class provides a framework for simulating population models using various numerical methods.
    Subclasses should implement the `diff` method to define the specific differential equation governing the population model.
    """    
    def __init__(
        self,
        method: Union[str, Method],
        f0: Union[int, float, np.ndarray, List[Union[int, float]], None] = None,
        tmin: Union[float, None] = None,
        tmax: Union[float, None] = None,
        h: Optional[float] = 1e-2,
        eps: Optional[float] = 1e-10,
    ):
        """
        Initializes the population model with the given numerical method and parameters.

        Args:
            method (Union[str, Method]): The numerical method to use for solving the model.
            f0 (Union[int, float, np.ndarray, List[Union[int, float]], None], optional): Initial value(s) of the population. Defaults to None.
            tmin (Union[float, None], optional): The start time for the simulation. Defaults to None.
            tmax (Union[float, None], optional): The end time for the simulation. Defaults to None.
            h (Optional[float], optional): The step size for the numerical method. Defaults to 1e-2.
            eps (Optional[float], optional): The tolerance for the numerical method (if applicable). Defaults to 1e-10.
        """
        if isinstance(method, Method):
            self.method = method
        else:
            if isinstance(f0, (int, float)):
                f0 = np.array([f0])

            args = {"f": self.diff, "f0": f0, "tmin": tmin, "tmax": tmax, "h": h}
            if method == "ModEuler":
                args["eps"] = eps

            self.method = get_method(method, **args)
        self.h = h
        self.f0 = f0

        self.tmin, self.tmax = tmin, tmax
        self.range = np.arange(tmin, tmax, h)

    def diff(self, x: np.ndarray, t: np.ndarray) -> np.ndarray:
        """
        Computes the derivative of the population model.

        This function should be implemented by subclasses to define the specific
        differential equation governing the population model.

        Args:
            x (np.ndarray): The current state of the population.
            t (np.ndarray): The current time.

        Returns:
            np.ndarray: The computed derivative of the population.
        """
        pass

    def solve(self):
        """
        Solves the population model using the specified numerical method.

        Returns:
            np.ndarray: The solution of the population model over the specified time range.
        """
        return self.method.solve()
