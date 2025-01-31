"""
This module contains the Delay class which models population growth with a time delay in the feedback mechanism.

The Delay model is defined by the differential equation:
    dx/dt = r * x * (1 - (x(t - T) / K))
where:
    - x is the population size
    - r is the growth rate
    - T is the time delay
    - K is the carrying capacity
"""

import numpy as np
from typing import Union, List

from .model import PopModel, Method


class Delay(PopModel):
    """
    The Delay class models population growth with a time delay in the feedback mechanism.
    """

    def __init__(
        self,
        X0: Union[int, float, np.ndarray, List[Union[int, float]]],
        r: float,
        T: float,
        K: float,
        method: Union[str, Method],
        tmin: Union[float, None],
        tmax: Union[float, None],
        h: Union[float, None],
        eps=1e-10,
    ):
        """
        Initialize the Delay model.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial population.
            r (float): Growth rate.
            T (float): Time delay.
            K (float): Carrying capacity.
            method (Union[str, Method]): Numerical method for solving the differential equation.
            tmin (Union[float, None]): Minimum time value.
            tmax (Union[float, None]): Maximum time value.
            h (Union[float, None]): Step size.
            eps (float, optional): Tolerance for numerical method. Defaults to 1e-10.
        """
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.r = r
        self.t = T
        self.k = K

    def diff(self, x: np.ndarray, t: np.ndarray) -> np.ndarray:
        """
        Compute the derivative for the Delay model.

        Args:
            x (np.ndarray): Current population size.
            t (np.ndarray): Current time.

        Returns:
            np.ndarray: Derivative dx/dt.
        """ 
        return (
            self.r
            * x
            * (1 - (self.method.res[max(0, round((t - self.t) / self.h))] / self.k))
        )
