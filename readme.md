# PyPopSim

PyPopSim is a Python library for simulating various population dynamics models using different numerical methods. The library provides a flexible framework for implementing custom population models through inheritance.

## Features

- Multiple numerical solving methods (Forward Euler, Modified Euler, RK2, RK4)
- Pre-implemented population models (Continuous Growth, Logistic Growth, SIR, SIS, Prey-Predator, etc.)
- Easy extensibility for custom population models
- Plotting utilities for visualization

## Creating Custom Population Models

You can create your own population model by inheriting from the `PopModel` base class. Here's a step-by-step guide:

### 1. Basic Structure

```python
from PopModels.model import PopModel
import numpy as np

class YourModel(PopModel):
    def __init__(self, params..., method, tmin, tmax, h, eps=1e-10):
        # Initialize initial conditions as numpy array
        X0 = np.array([...])  # Your initial conditions
        
        # Call parent constructor
        super().__init__(method, X0, tmin, tmax, h, eps)
        
        # Store your model parameters
        self.param1 = param1
        self.param2 = param2
        # ...

    def diff(self, x, t):
        # Define your differential equations
        # x: current state vector
        # t: current time
        return np.array([
            # Your equations here
        ])
```

### 2. Example Implementation

Here's an example of implementing a simple exponential growth model:

```python
class ExponentialGrowth(PopModel):
    def __init__(self, N0, r, method, tmin, tmax, h, eps=1e-10):
        super().__init__(method, N0, tmin, tmax, h, eps)
        self.r = r  # growth rate

    def diff(self, x, t):
        return np.array([self.r * x[0]])
```

### 3. Usage Example

```python
# Create and solve your model
model = ExponentialGrowth(
    N0=100,        # initial population
    r=0.1,         # growth rate
    method="RK4",  # numerical method
    tmin=0,        # start time
    tmax=100,      # end time
    h=0.1          # time step
)

# Get solution
t, solution = model.solve()
```

## Key Points for Implementation

1. **Initial Conditions**:
   - Must be converted to numpy array in `__init__`
   - For single-variable models: `np.array([initial_value])`
   - For multi-variable models: `np.array([value1, value2, ...])`

2. **Differential Equations**:
   - Implement in the `diff(self, x, t)` method
   - `x`: Current state vector (numpy array)
   - `t`: Current time (float)
   - Return: numpy array of same dimension as state vector

3. **Available Numerical Methods**:
   - "FwdEuler": Forward Euler method
   - "ModEuler": Modified Euler method
   - "RK2": 2nd order Runge-Kutta
   - "RK4": 4th order Runge-Kutta

## Example: Implementing a Predator-Prey Model

The Lotka-Volterra predator-prey model is already implemented in the library:

```python
class PreyPred(PopModel):
    def __init__(self, X0, alpha, beta, delta, gamma, method, tmin, tmax, h, eps=1e-10):
        super().__init__(method, X0, tmin, tmax, h, eps)
        self.alpha = alpha  # prey growth rate
        self.beta = beta    # predation rate
        self.delta = delta  # predator growth rate
        self.gamma = gamma  # predator death rate

    def diff(self, x, _):
        return np.array([
            self.alpha * x[0] - self.beta * x[0] * x[1],  # prey equation
            self.delta * x[0] * x[1] - self.gamma * x[1]   # predator equation
        ])
```

Usage:
```python
# Initial conditions: 100 prey, 20 predators
X0 = np.array([100, 20])

model = PreyPred(
    X0=X0,
    alpha=0.1,   # prey growth rate
    beta=0.02,   # predation rate
    delta=0.02,  # predator growth rate
    gamma=0.4,   # predator death rate
    method="RK4",
    tmin=0,
    tmax=100,
    h=0.1
)

t, solution = model.solve()
```

## Contributing

Feel free to contribute by:
1. Adding new population models
2. Implementing additional numerical methods
3. Improving documentation
4. Reporting bugs
5. Suggesting features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.