"""
This module contains the SIS class which models the spread of an infectious disease in a population using the Susceptible-Infected-Susceptible (SIS) model.

The SIS model is defined by the differential equations:
    dS/dt = -beta * S * I + gamma * I
    dI/dt = beta * S * I - gamma * I
where:
    - S is the number of susceptible individuals
    - I is the number of infected individuals
    - beta is the transmission rate
    - gamma is the recovery rate
"""

import numpy as np
from typing import Union, List, Optional

from .model import PopModel, Method

class SIS(PopModel):
    """
    SIS model for the spread of an infectious disease.

    This class models the spread of an infectious disease in a population using the Susceptible-Infected-Susceptible (SIS) model.
    """
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
        Initialize the SIS model.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial state of the system.
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
        Compute the derivatives for the SIS model.

        Args:
            x (np.ndarray): Current state of the system [S, I].
            _ (np.ndarray): Time array (not used in this function).

        Returns:
            np.ndarray: Derivatives [dS/dt, dI/dt].
        """        
        return np.array(
            [
                -self.beta * x[0] * x[1] + self.gamma * x[1],
                self.beta * x[0] * x[1] - self.gamma * x[1],
            ]
        )
