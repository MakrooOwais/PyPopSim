"""
This module contains the PopulationPlotter class which is used to plot population trends over time.
"""

import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Union, Iterable


class PopulationPlotter:
    """
    A class used to plot population trends over time.

    Attributes
    ----------
    xval : Iterable
        An iterable containing the x-axis values (e.g., time points).
    data : Iterable
        An iterable containing the y-axis values (e.g., population data).
    labels : List[str]
        A list of labels for the data series.

    Methods
    -------
    plot(title="Population Trends", xlabel="Time", ylabel="Population", save_path=None)
        Plots the population data with the given title, x-axis label, y-axis label, and optional save path.
    """
    def __init__(self, xval: Iterable, data: Iterable, labels: List[str] = []):
        """
        Initializes the PopulationPlotter with x-axis values, y-axis values, and optional labels.

        Args:
            xval (Iterable): An iterable containing the x-axis values (e.g., time points).
            data (Iterable): An iterable containing the y-axis values (e.g., population data).
            labels (List[str], optional): A list of labels for the data series. Defaults to [].
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
        Plots the population data with the given title, x-axis label, y-axis label, and optional save path.

        Args:
            title (str, optional): The title of the plot. Defaults to "Population Trends".
            xlabel (str, optional): The label for the x-axis. Defaults to "Time".
            ylabel (str, optional): The label for the y-axis. Defaults to "Population".
            save_path (Union[str, Path, None], optional): The path to save the plot image. Defaults to None.
        """        
        plt.figure(figsize=(10, 6))
        if self.labels:
            plt.plot(self.xval, self.data, label=self.labels)
            plt.legend()
        else:
            plt.plot(self.xval, self.data)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if save_path:
            plt.savefig(save_path)
        plt.show()
