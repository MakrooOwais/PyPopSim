from .model import PopModel
import numpy as np


class PreyPred(PopModel):
    def __init__(self, X0, alpha, beta, delta, gamma, method, tmin, tmax, h, eps=1e-10):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.gamma = gamma

    def diff(self, x, _):
        return np.array(
            [
                self.alpha * x[0] - self.beta * x[0] * x[1],
                self.delta * x[0] * x[1] - self.gamma * x[1],
            ]
        )
