"""
This module contains the ContGrowth class which models continuous growth using a differential equation.

The continuous growth model is defined by the differential equation:
    dX/dt = k * X
where:
    - X is the population
    - k is the growth rate constant
"""

import numpy as np
from typing import Union, List, Any

from .model import PopModel, Method


class ContGrowth(PopModel):
    """
    A class to model continuous growth using a differential equation.
    """

    def __init__(
        self,
        X0: Union[int, float, np.ndarray, List[Union[int, float]]],
        k,
        method: Union[str, Method],
        tmin: float,
        tmax: float,
        h: float,
        eps: Union[float, None] = None,
    ):
        """
        Initialize the ContGrowth model.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial population.
            k (float): Growth rate constant.
            method (Union[str, Method]): Numerical method to use for solving the differential equation.
            tmin (float): Start time.
            tmax (float): End time.
            h (float): Step size.
            eps (Union[float, None], optional): Tolerance for numerical method. Defaults to None.
        """
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.k = k

    def diff(self, x: np.ndarray, _: Any) -> np.ndarray:
        """
        Compute the derivative for the continuous growth model.

        Args:
            x (np.ndarray): Current state of the system (population).
            _ (Any): Placeholder for time (not used in this function).

        Returns:
            np.ndarray: Derivative (rate of change of population).
        """
        return self.k * x
