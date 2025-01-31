from .model import PopModel


class LogGrowth(PopModel):
    def __init__(self, X0, M, r, method, tmin, tmax, h, eps=None):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.m = M
        self.r = r

    def diff(self, x, _):
        return self.r * x * (1 - (x / self.m))
