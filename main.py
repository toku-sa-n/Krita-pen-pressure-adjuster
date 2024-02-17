from evdev import InputDevice, ecodes
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from normalized_pressure import NormalizedPressure
from typing import Any, Callable
from abstract_normalized_pressure_input import AbstractNormalizedPressureInput
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
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass


class GraphPlotter(AbstractGraphPlotter):
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()

    def plot_graph(
        self,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        self.set_plot_properties()
        self.plot_original_data(frequencies)
        self.plot_bspline(frequencies)
        self.save_graph()

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

    def save_graph(self) -> None:
        self.fig.savefig("graph.png")
        print(f"\nGraph saved as graph.png")


def reproduce_bspline_and_save(
    coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]], filename: str
) -> None:
    GraphPlotter().plot_graph(coordinates)


def write_bspline_to_file(
    filename: str, coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]]
) -> None:
    krita_settings_writer = KritaSettingsWriterToFile()
    krita_settings_writer.write_settings(filename, coordinates)


def create_pressure_graph(pen_pressures: list[NormalizedPressure]) -> None:
    scaled_pressures_and_frequencies = (
        PressureCumulativeFrequencyCalculator().calculate_pressure_cumulative_frequency(
            pen_pressures
        )
    )

    scaled_pressures, scaled_frequencies = zip(*scaled_pressures_and_frequencies)

    # Create a cumulative line graph
    plt.plot(scaled_pressures, scaled_frequencies, color="blue", label="Original Data")
    plt.title("Scaled Cumulative Pressure Frequency")
    plt.xlabel("Scaled Pen Pressure (0-1)")
    plt.ylabel("Scaled Cumulative Frequency (0-1)")
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Reproduce the cumulative line graph using a B-Spline curve
    filename = "graph.png"
    reproduce_bspline_and_save(scaled_pressures_and_frequencies, filename)

    # Write B-Spline curve coordinates to a file in the desired format
    krita_settings_filename = "pen_pressure.txt"
    write_bspline_to_file(krita_settings_filename, scaled_pressures_and_frequencies)


def run(pressure_input: AbstractNormalizedPressureInput) -> None:
    # Monitor pen pressure
    pen_pressures = pressure_input.monitor_pressure()

    # Create and display the pressure graph
    if pen_pressures:
        create_pressure_graph(pen_pressures)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from", help="Input path")

    args = parser.parse_args()

    input_path = getattr(args, "from")

    pressure_input = EvdevPenPressureInput(input_path)
    normalized_pressure_input = NormalizedPressureInput(pressure_input)

    run(normalized_pressure_input)


if __name__ == "__main__":
    main()
