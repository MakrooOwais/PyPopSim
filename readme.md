# PyPopSim

A Python library for simulating population dynamics using various numerical methods. PyPopSim provides a flexible framework for implementing and solving different population models, from simple exponential growth to complex predator-prey systems.

[![PyPI version](https://badge.fury.io/py/pypopsim.svg)](https://badge.fury.io/py/pypopsim)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

Install PyPopSim using pip:

```bash
pip install pypopsim <THIS IS A WORK-IN-PROGRESS>
```

## Quick Start

```python
from pypopsim.PopModels import PreyPred
import numpy as np

# Initialize a predator-prey model
model = PreyPred(
    X0=np.array([100, 20]),  # Initial populations: 100 prey, 20 predators
    alpha=0.1,   # prey growth rate
    beta=0.02,   # predation rate
    delta=0.02,  # predator growth rate
    gamma=0.4,   # predator death rate
    method="RK4",
    tmin=0,
    tmax=100,
    h=0.1
)

# Solve the system
t, solution = model.solve()
```

## Features

-   **Multiple Numerical Methods**

    -   Forward Euler
    -   Modified Euler
    -   RK2 (2nd order Runge-Kutta)
    -   RK4 (4th order Runge-Kutta)

-   **Pre-implemented Population Models**

    -   Continuous Growth
    -   Logistic Growth
    -   SIR (Susceptible-Infected-Recovered)
    -   SIS (Susceptible-Infected-Susceptible)
    -   Prey-Predator (Lotka-Volterra)
    -   Delayed Population Growth
    -   Infectious Disease Models

-   **Easy Model Creation**

    -   Inherit from base PopModel class
    -   Define your differential equations
    -   Ready to solve!

    ## Creating Your Own Model

    PyPopSim makes it easy to implement custom population models:

    ```python
    from pypopsim.PopModels import PopModel
    import numpy as np

    class CustomModel(PopModel):
        def __init__(self, N0, param1, param2, method, tmin, tmax, h, eps=1e-10):
            super().__init__(method, N0, tmin, tmax, h, eps)
            self.param1 = param1
            self.param2 = param2

        def diff(self, x, t):
            # Define your differential equations
            return np.array([
                # Your equations here
            ])
    ```

    ## Creating Your Own Method

    To create your own numerical method, inherit from the `NumericalMethod` base class and implement the `step` function:

    ```python
    from pypopsim.NumSolvers import NumericalMethod
    import numpy as np

    class FwdEuler(NumericalMethod):
        def __init__(
            self,
            f: Callable,
            f0: Union[int, float, np.ndarray, List[Union[int, float]]],
            tmin: float,
            tmax: float,
            h: float = 1e-2,
        ):
            super().__init__(f, f0, tmin, tmax, h)


        def solve(self):
            f = self.f
            h = self.h

            for i in tqdm(self.range[1:]):
                self.res.append(self.res[-1] + h * f(self.res[-1], i - h))

            return self.res
    ```

Then, you can use your custom method in your models:

```python
from pypopsim.PopModels import PreyPred
import numpy as np

# Initialize a predator-prey model with the custom method
model = PreyPred(
    X0=np.array([100, 20]),
    alpha=0.1,
    beta=0.02,
    delta=0.02,
    gamma=0.4,
    method=CustomMethod(),
    tmin=0,
    tmax=100,
    h=0.1
)

# Solve the system
t, solution = model.solve()
```

### Base Class: PopModel

```python
class PopModel:
    def __init__(
        self,
        method: str,          # Numerical method to use
        f0: Union[float, np.ndarray],  # Initial conditions
        tmin: float,         # Start time
        tmax: float,         # End time
        h: float = 1e-2,     # Time step
        eps: float = 1e-10,  # Error tolerance (for ModEuler)
    ):
        ...

    def diff(self, x, t):
        """
        Define your differential equations here.

        Args:
            x: Current state vector
            t: Current time

        Returns:
            numpy.ndarray: Rate of change for each variable
        """
        pass

    def solve(self):
        """
        Solve the system of equations.

        Returns:
            tuple: (time_points, solution)
        """
        ...
```

## Visualization

PyPopSim includes a `PopulationPlotter` class for easy visualization of population dynamics:

```python
from pypopsim import PopulationPlotter

class PopulationPlotter:
    def __init__(self, xval: Iterable, data: Iterable, labels: List[str] = []):
        """
        Initialize the population plotter.

        Args:
            xval: Iterable of x-axis values (usually time points)
            data: Iterable of y-axis values (population data)
            labels: Optional list of labels for multiple populations
        """
        self.xval = xval
        self.data = data
        self.labels = labels

    def plot(
        self,
        title: str = "Population Trends",
        xlabel: str = "Time",
        ylabel: str = "Population",
        save_path: Union[str, Path, None] = None,
    ):
        """
        Create and display the population plot.

        Args:
            title: Plot title (default: "Population Trends")
            xlabel: X-axis label (default: "Time")
            ylabel: Y-axis label (default: "Population")
            save_path: Optional path to save the plot (str or Path object)
        """
```

### Example Usage

```python
from pypopsim import PopulationPlotter
from pypopsim.PopModels import PreyPred
import numpy as np

# Create and solve a predator-prey model
model = PreyPred(
    X0=np.array([100, 20]),
    alpha=0.1, beta=0.02,
    delta=0.02, gamma=0.4,
    method="RK4",
    tmin=0, tmax=100, h=0.1
)

t, solution = model.solve()

# Create a population plot
plotter = PopulationPlotter(
    xval=t,
    data=solution,
    labels=['Prey', 'Predator']
)

# Display and save the plot
plotter.plot(
    title="Predator-Prey Dynamics",
    xlabel="Time (days)",
    ylabel="Population Size",
    save_path="predator_prey_plot.png"
)
```

### Multiple Population Visualization

```python
# Compare different initial conditions
model1 = PreyPred(X0=np.array([100, 20]), ...)
model2 = PreyPred(X0=np.array([150, 30]), ...)

t1, sol1 = model1.solve()
t2, sol2 = model2.solve()

# Plot prey populations
plotter = PopulationPlotter(
    xval=[t1, t2],
    data=[sol1[:, 0], sol2[:, 0]],
    labels=['Initial:100', 'Initial:150']
)

plotter.plot(title="Prey Population Comparison")
```

## Examples

### Predator-Prey System

```python
from pypopsim.PopModels import PreyPred
import numpy as np
import matplotlib.pyplot as plt

# Create model
model = PreyPred(
    X0=np.array([100, 20]),
    alpha=0.1, beta=0.02,
    delta=0.02, gamma=0.4,
    method="RK4",
    tmin=0, tmax=100, h=0.1
)

# Solve
t, solution = model.solve()

# Plot
plt.plot(t, solution[:, 0], label='Prey')
plt.plot(t, solution[:, 1], label='Predator')
plt.legend()
plt.show()
```

## Dependencies

-   NumPy >= 1.19.0
-   Matplotlib >= 3.3.0
-   Seaborn >= 0.11.0

## Development

To contribute to PyPopSim:

1. Clone the repository:

```bash
git clone https://github.com/MakrooOwais/PyPopSim.git
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use PyPopSim in your research, please cite:

```bibtex
@software{pypopsim2025,
  author = {Owais Makroo},
  title = {PyPopSim: A Python Library for Population Dynamics Simulation},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/MakrooOwais/PyPopSim}
}
```
