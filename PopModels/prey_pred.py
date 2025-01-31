"""
This module contains the PreyPred class which models the dynamics of prey and predator populations using differential equations.

The PreyPred model is defined by the differential equations:
    dx/dt = alpha * x - beta * x * y
    dy/dt = delta * x * y - gamma * y
where:
    - x is the population of prey
    - y is the population of predators
    - alpha is the growth rate of prey
    - beta is the rate at which predators destroy prey
    - delta is the growth rate of predators per prey eaten
    - gamma is the death rate of predators
"""

import numpy as np
from typing import Union, List, Optional

from .model import PopModel, Method


class PreyPred(PopModel):
    """
    A class to model prey-predator dynamics using differential equations.
    """

    def __init__(
        self,
        X0: Union[int, float, np.ndarray, List[Union[int, float]]],
        alpha: float,
        beta: float,
        delta: float,
        gamma: float,
        method: Union[str, Method],
        tmin: Union[float, None] = None,
        tmax: Union[float, None] = None,
        h: Optional[float] = 1e-2,
        eps: Optional[float] = 1e-10,
    ):
        """
        Initialize the PreyPred model with initial conditions and parameters.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial population values for prey and predator.
            alpha (float): Growth rate of prey.
            beta (float): Rate at which predators destroy prey.
            delta (float): Growth rate of predators per prey eaten.
            gamma (float): Death rate of predators.
            method (Union[str, Method]): Numerical method to use for solving the differential equations.
            tmin (Union[float, None], optional): Minimum time value for the simulation. Defaults to None.
            tmax (Union[float, None], optional): Maximum time value for the simulation. Defaults to None.
            h (Optional[float], optional): Step size for the numerical method. Defaults to 1e-2.
            eps (Optional[float], optional): Tolerance for the numerical method. Defaults to 1e-10.
        """
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.gamma = gamma

    def diff(self, x: np.ndarray, _: np.ndarray) -> np.ndarray:
        """
        Compute the derivatives for the PreyPred model.

        Args:
            x (np.ndarray): State vector [prey population, predator population].
            _ (np.ndarray): Time vector (not used in this model).

        Returns:
            np.ndarray: Derivatives [dx/dt, dy/dt].
        """
        return np.array(
            [
                self.alpha * x[0] - self.beta * x[0] * x[1],
                self.delta * x[0] * x[1] - self.gamma * x[1],
            ]
        )
