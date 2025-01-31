import numpy as np
from typing import Union
from NumSolvers import get_method


class PopModel:
    def __init__(
        self,
        method: str,
        f0: Union[float, np.ndarray],
        tmin: float,
        tmax: float,
        h: float = 1e-2,
        eps: float = 1e-10,
    ):
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

    def diff(self):
        return 0.0

    def solve(self):
        return self.method.solve()
