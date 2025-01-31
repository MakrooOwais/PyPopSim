from PopModels import get_pop_model
from plotter import PopulationPlotter

if __name__ == "__main__":
    model = get_pop_model(
        "ContGrowth", X0=40, k=0.25, method="RK4", tmin=0, tmax=10, h=1e-2
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["p"])
    plotter.plot()

    model = get_pop_model(
        "PreyPred",
        X0=[40, 9],
        alpha=0.1,
        beta=0.02,
        delta=0.01,
        gamma=0.1,
        method="ModEuler",
        tmin=0,
        tmax=100,
        h=1e-2,
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["Prey", "Pred"])
    plotter.plot()

    model = get_pop_model(
        "LogGrowth", X0=140, M=3540, r=-0.04, method="RK4", tmin=0, tmax=10, h=1e-2
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["p"])
    plotter.plot()

    model = get_pop_model(
        "InfecDis",
        X0=[999, 1],
        beta=0.00025,
        method="ModEuler",
        tmin=0,
        tmax=200,
        h=1e-2,
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["S", "I"])
    plotter.plot()

    model = get_pop_model(
        "SIS",
        X0=[999, 1],
        beta=0.00025,
        gamma=0.1,
        method="ModEuler",
        tmin=0,
        tmax=200,
        h=1e-2,
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["S", "I"])
    plotter.plot()

    model = get_pop_model(
        "SIR",
        X0=[999, 1, 0],
        beta=0.00025,
        gamma=0.1,
        method="ModEuler",
        tmin=0,
        tmax=200,
        h=1e-2,
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["S", "I", "R"])
    plotter.plot()

    model = get_pop_model(
        "Delay",
        X0=0.8,
        r=12,
        T=0.11,
        K=3,
        method="FwdEuler",
        tmin=0,
        tmax=30,
        h=0.05,
    )
    res = model.solve()

    plotter = PopulationPlotter(model.range, res, labels=["P"])
    plotter.plot()
