"""
This module contains an implementation of the modified Euler method
for solving ordinary differential equations (ODEs).
"""

import numpy as np
from tqdm import tqdm
from typing import Union, Callable, List

from .method import Method


class ModEuler(Method):
    def __init__(
        self,
        f: Callable,
        f0: Union[int, float, np.ndarray, List[Union[int, float]]],
        tmin: float,
        tmax: float,
        h: float = 1e-2,
        eps: float = 1e-10,
    ):
        """
        Initialize the ModEuler solver.

        Args:
            f (Callable): The function to be solved.
            f0 (Union[float, np.ndarray]): The initial condition.
            tmin (float): The start time.
            tmax (float): The end time.
            h (float, optional): The step size. Defaults to 1e-2.
            eps (float, optional): The tolerance for convergence. Defaults to 1e-10.
        """
        super().__init__(f, f0, tmin, tmax, h)
        self.eps = eps

    def solve(self):
        """
        Solve the differential equation using the modified Euler method.

        Returns:
            list: The solution of the differential equation at each time step.
        """
        f = self.f
        h = self.h

        for i in tqdm(self.range[1:]):
            y = self.res[-1] + h * f(self.res[-1], i)
            temp = self.res[-1] + (h / 2) * (f(self.res[-1], i - h) + f(y, i))
            while np.mean(y - temp) > self.eps:
                y = temp
                temp = self.res[-1] + (h / 2) * (f(self.res[-1], i - h) + f(y, i))

            self.res.append(y)

        return self.res


if __name__ == "__main__":
    # Example: Solve the differential equation dy/dt = y with initial condition y(0) = 1
    from matplotlib import pyplot as plt

    f = lambda y, t: y
    y0 = 1
    t0, t1 = 0, 10

    rk4 = ModEuler(f, y0, t0, t1)
    res = rk4.solve()

    # print(self.res)
    plt.plot(rk4.range, res)
    plt.plot(rk4.range, np.e**rk4.range)
    plt.show()

    # Example: Solve the system of differential equations
    # dx/dt = x - y, dy/dt = x + y with initial conditions x(0) = 1, y(0) = 0
    f = lambda u, t: np.array([u[0] - u[1], u[0] + u[1]])
    u0 = np.array([1, 0])
    t0, t1 = 0, 10

    rk4 = ModEuler(f, u0, t0, t1)
    res = rk4.solve()

    res = np.array(res)
    plt.plot(rk4.range, res[:, 0], label="x(t)")
    plt.plot(rk4.range, res[:, 1], label="y(t)")
    plt.plot(rk4.range, np.exp(rk4.range) * np.cos(rk4.range), "--", label="True x(t)")
    plt.plot(rk4.range, np.exp(rk4.range) * np.sin(rk4.range), "--", label="True y(t)")
    plt.legend()
    plt.show()
