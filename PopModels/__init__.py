"""
This module initializes various population models and provides a factory function to retrieve a specific model by name.
"""

from .cont_growth import *
from .log_growth import *
from .prey_pred import *
from .infec_dis import *
from .sis import *
from .sir import *
from .delay import *

from .model import PopModel


def get_pop_model(name: str, **kwargs) -> PopModel:
    """
    Retrieves a population model by its name.

    Args:
        name (str): The name of the population model class to instantiate. Options are:
            - `ContGrowth`: Requires kwargs `initial_population` and `growth_rate`.
            - `LogGrowth`: Requires kwargs `initial_population`, `carrying_capacity`, and `growth_rate`.
            - `PreyPred`: Requires kwargs `prey_initial`, `predator_initial`, `prey_birth_rate`, `predation_rate`, `predator_efficiency`, and `predator_death_rate`.
            - `InfecDis`: Requires kwargs `initial_susceptible`, `initial_infected`, `initial_recovered`, `transmission_rate`, and `recovery_rate`.
            - `SIS`: Requires kwargs `initial_susceptible`, `initial_infected`, `transmission_rate`, and `recovery_rate`.
            - `SIR`: Requires kwargs `initial_susceptible`, `initial_infected`, `initial_recovered`, `transmission_rate`, and `recovery_rate`.
            - `Delay`: Requires kwargs `initial_population`, `growth_rate`, and `delay`.
        **kwargs: Additional keyword arguments to pass to the model's constructor.

    Returns:
        PopModel: An instance of the specified population model.
    """
    options = ["ContGrowth", "LogGrowth", "PreyPred", "InfecDis", "SIS", "SIR", "Delay"]

    if name not in options:
        raise ValueError(
            f"Invalid model name '{name}'. Available options are: {', '.join(options)}"
        )

    return eval(name)(**kwargs)
