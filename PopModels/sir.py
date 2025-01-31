"""
This module contains the SIR class which models the spread of an infectious disease in a population.

The SIR model is defined by the differential equations:
    dS/dt = -beta * S * I
    dI/dt = beta * S * I - gamma * I
    dR/dt = gamma * I
where:
    - S is the number of susceptible individuals
    - I is the number of infectious individuals
    - R is the number of recovered individuals
    - beta is the transmission rate
    - gamma is the recovery rate
"""

import numpy as np
from typing import Union, List, Optional

from .model import PopModel, Method


class SIR(PopModel):
    def __init__(
        self,
        X0: Union[int, float, np.ndarray, List[Union[int, float]]],
        beta: float,
        gamma: float,
        method: Union[str, Method],
        tmin: Union[float, None] = None,
        tmax: Union[float, None] = None,
        h: Optional[float] = 1e-2,
        eps: Optional[float] = 1e-10,
    ):
        """
        Initialize the SIR model.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial state vector [S, I, R].
            beta (float): Transmission rate.
            gamma (float): Recovery rate.
            method (Union[str, Method]): Numerical method to use for solving the differential equations.
            tmin (Union[float, None], optional): Minimum time value. Defaults to None.
            tmax (Union[float, None], optional): Maximum time value. Defaults to None.
            h (Optional[float], optional): Step size for the numerical method. Defaults to 1e-2.
            eps (Optional[float], optional): Tolerance for the numerical method. Defaults to 1e-10.
        """
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.beta = beta
        self.gamma = gamma

    def diff(self, x: np.ndarray, _: np.ndarray) -> np.ndarray:
        """
        Compute the derivatives for the SIR model.

        Args:
            x (np.ndarray): State vector [S, I, R].
            _ (np.ndarray): Time vector (not used in this model).

        Returns:
            np.ndarray: Derivatives [dS/dt, dI/dt, dR/dt].
        """
        return np.array(
            [
                -self.beta * x[0] * x[1],
                self.beta * x[0] * x[1] - self.gamma * x[1],
                self.gamma * x[1],
            ]
        )
