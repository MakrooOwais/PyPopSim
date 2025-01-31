from .model import PopModel


class ContGrowth(PopModel):
    def __init__(self, X0, k, method, tmin, tmax, h, eps=None):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.k = k

    def diff(self, x, _):
        return self.k * x
