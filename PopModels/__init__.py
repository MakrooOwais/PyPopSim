from .cont_growth import *
from .log_growth import *
from .prey_pred import *
from .infec_dis import *
from .sis import *
from .sir import *
from .delay import *

from .model import PopModel


def get_pop_model(name: str, **kwargs) -> PopModel:
    return eval(name)(**kwargs)
