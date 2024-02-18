import matplotlib.pyplot as plt
import numpy as np

from abstract_graph_plotter import AbstractGraphPlotter
from bspline_generator import BSplineGenerator
from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.normalized_pressure import NormalizedPressure


class GraphPlotter(AbstractGraphPlotter):
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()

    def plot_graph(
        self,
        filename: str,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        self.set_plot_properties()
        self.plot_original_data(frequencies)
        self.plot_bspline(frequencies)
        self.save_graph(filename)

    def set_plot_properties(self) -> None:
        self.ax.set_title("Scaled Cumulative Pressure Frequency")
        self.ax.set_xlabel("Scaled Pen Pressure (0-1)")
        self.ax.set_ylabel("Scaled Cumulative Frequency (0-1)")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)

    def plot_original_data(
        self,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        x_values, y_values = zip(*frequencies)

        self.ax.plot(x_values, y_values, color="blue", label="Original Data")
        self.ax.legend()

    def plot_bspline(
        self,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        x_values, _ = zip(*frequencies)

        bspline_f = BSplineGenerator().reproduce_bspline_and_save(frequencies)
        x_bspline = np.linspace(min(x_values), max(x_values), 1000)
        y_bspline = bspline_f(x_bspline)

        self.ax.plot(x_bspline, y_bspline, color="red", label="B-Spline Curve")
        self.ax.legend()

    def save_graph(self, filename: str) -> None:
        self.fig.savefig(filename)
        print(f"\nGraph saved as graph.png")
