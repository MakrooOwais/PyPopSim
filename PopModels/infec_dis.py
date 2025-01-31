"""
This module contains the InfecDis class which models the spread of an infectious disease in a population using a simple compartmental model.

The model is defined by the differential equations:
    dS/dt = -beta * S * I
    dI/dt = beta * S * I
where:
    - S is the number of susceptible individuals
    - I is the number of infected individuals
    - beta is the transmission rate
"""

import numpy as np
from typing import Union, List, Optional

from .model import PopModel, Method


class InfecDis(PopModel):
    """
    InfecDis is a subclass of PopModel that models the spread of an infectious disease
    using a simple compartmental model.
    """

    def __init__(
        self,
        X0: Union[int, float, np.ndarray, List[Union[int, float]]],
        beta: float,
        method: Union[str, Method],
        tmin: Union[float, None] = None,
        tmax: Union[float, None] = None,
        h: Optional[float] = 1e-2,
        eps: Optional[float] = 1e-10,
    ):
        """
        Initialize the InfecDis model.

        Args:
            X0 (Union[int, float, np.ndarray, List[Union[int, float]]]): Initial state of the compartments.
            beta (float): Transmission rate of the disease.
            method (Union[str, Method]): Numerical method to use for solving the model.
            tmin (Union[float, None], optional): Minimum time for the simulation. Defaults to None.
            tmax (Union[float, None], optional): Maximum time for the simulation. Defaults to None.
            h (Optional[float], optional): Step size for the numerical method. Defaults to 1e-2.
            eps (Optional[float], optional): Tolerance for the numerical method. Defaults to 1e-10.
        """
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.beta = beta

    def diff(self, x: np.ndarray, _: np.ndarray) -> np.ndarray:
        """
        Compute the derivatives for the infectious disease model.

        Args:
            x (np.ndarray): Current state of the system [S, I].
            _ (np.ndarray): Time array (not used in this function).

        Returns:
            np.ndarray: Derivatives [dS/dt, dI/dt].
        """
        return np.array(
            [
                -self.beta * x[0] * x[1],
                self.beta * x[0] * x[1],
            ]
        )
