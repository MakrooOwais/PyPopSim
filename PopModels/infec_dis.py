from .model import PopModel
import numpy as np


class InfecDis(PopModel):
    def __init__(self, X0, beta, method, tmin, tmax, h, eps=1e-10):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.beta = beta

    def diff(self, x, _):
        return np.array(
            [
                -self.beta * x[0] * x[1],
                self.beta * x[0] * x[1],
            ]
        )
