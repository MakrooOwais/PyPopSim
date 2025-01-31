from .model import PopModel


class Delay(PopModel):
    def __init__(self, X0, r, T, K, method, tmin, tmax, h, eps=1e-10):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.r = r
        self.t = T
        self.k = K

    def diff(self, x, t):
        # print(x, round((t - self.t) / self.h))
        return (
            self.r
            * x
            * (1 - (self.method.res[max(0, round((t - self.t) / self.h))] / self.k))
        )
