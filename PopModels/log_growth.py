"""
This module contains the LogGrowth class which models the logistic growth of a population.

The logistic growth model is defined by the differential equation:
    dx/dt = r * x * (1 - x / M)
where:
    - x is the population size
    - r is the intrinsic growth rate
    - M is the carrying capacity of the environment
"""

import numpy as np
from typing import Union, List, Optional

from .model import PopModel, Method


class LogGrowth(PopModel):
    """
    Logistic Growth Model
    """
    def __init__(
        self,
        X0: Union[int, float, np.ndarray, List[Union[int, float]]],
        M: float,
        r: float,
        method: Union[str, Method],
        tmin: Union[float, None] = None,
        tmax: Union[float, None] = None,
        h: Optional[float] = 1e-2,
        eps: Optional[float] = 1e-10,
    ):
        """
        Initialize the Logistic Growth Model.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial population size.
            M (float): Carrying capacity of the environment.
            r (float): Intrinsic growth rate.
            method (Union[str, Method]): Numerical method to use for solving the differential equation.
            tmin (Union[float, None], optional): Minimum time value. Defaults to None.
            tmax (Union[float, None], optional): Maximum time value. Defaults to None.
            h (Optional[float], optional): Step size for the numerical method. Defaults to 1e-2.
            eps (Optional[float], optional): Tolerance for the numerical method. Defaults to 1e-10.
        """
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.m = M
        self.r = r

    def diff(self, x: np.ndarray, _: np.ndarray) -> np.ndarray:
        """
        Compute the derivative for the logistic growth model.

        Args:
            x (np.ndarray): Population size.
            _ (np.ndarray): Time vector (not used in this model).

        Returns:
            np.ndarray: Derivative dx/dt.
        """
        return self.r * x * (1 - (x / self.m))
