import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Union, Iterable


class PopulationPlotter:
    def __init__(self, xval: Iterable, data: Iterable, labels: List[str] = []):
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
