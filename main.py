from evdev import InputDevice, ecodes
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from normalized_pressure import NormalizedPressure
from typing import Any, Callable
from abstract_normalized_pressure_input import AbstractNormalizedPressureInput
from abstract_pressure_cumulative_frequency_calculator import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from abstract_krita_settings_writer import AbstractKritaSettingsWriter
from evdev_pen_pressure_input import EvdevPenPressureInput
from normalized_pressure_input import NormalizedPressureInput
from krita_settings_writer_to_file import KritaSettingsWriterToFile
from pressure_cumulative_frequency_calculator import (
    PressureCumulativeFrequencyCalculator,
)
import argparse
from normalized_frequency import NormalizedFrequency
from abc import ABC, abstractmethod
from bspline_generator import BSplineGenerator


class AbstractGraphPlotter(ABC):
    @abstractmethod
    def plot_graph(
        self,
        filename: str,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass


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


def write_bspline_to_file(
    filename: str, coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]]
) -> None:
    krita_settings_writer = KritaSettingsWriterToFile()
    krita_settings_writer.write_settings(filename, coordinates)


def run(
    pressure_input: AbstractNormalizedPressureInput,
    freq_calculator: AbstractPressureCumulativeFrequencyCalculator,
    graph_plotter: AbstractGraphPlotter,
    config_writer: AbstractKritaSettingsWriter,
) -> None:
    # Monitor pen pressure
    pen_pressures = pressure_input.monitor_pressure()

    # Create and display the pressure graph
    if pen_pressures:
        pressure_freq = freq_calculator.calculate_pressure_cumulative_frequency(
            pen_pressures
        )

        graph_plotter.plot_graph("graph.png", pressure_freq)

        config_writer.write_settings("pen_pressure.txt", pressure_freq)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from", help="Input path")

    args = parser.parse_args()

    input_path = getattr(args, "from")

    pressure_input = EvdevPenPressureInput(input_path)
    normalized_pressure_input = NormalizedPressureInput(pressure_input)

    freq_calculator = PressureCumulativeFrequencyCalculator()

    graph_plotter = GraphPlotter()
    config_writer = KritaSettingsWriterToFile()

    run(normalized_pressure_input, freq_calculator, graph_plotter, config_writer)


if __name__ == "__main__":
    main()
