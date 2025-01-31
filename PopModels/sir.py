from .model import PopModel
import numpy as np


class SIR(PopModel):
    def __init__(self, X0, beta, gamma, method, tmin, tmax, h, eps=1e-10):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.beta = beta
        self.gamma = gamma

    def diff(self, x, _):
        return np.array(
            [
                -self.beta * x[0] * x[1],
                self.beta * x[0] * x[1] - self.gamma * x[1],
                self.gamma * x[1],
            ]
        )
