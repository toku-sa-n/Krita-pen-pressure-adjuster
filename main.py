from evdev import InputDevice, ecodes
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from normalized_pressure import NormalizedPressure
from typing import Any
from abstract_normalized_pressure_input import AbstractNormalizedPressureInput
from evdev_pen_pressure_input import EvdevPenPressureInput
from normalized_pressure_input import NormalizedPressureInput
from krita_settings_writer_to_file import KritaSettingsWriterToFile
from pressure_cumulative_frequency_calculator import (
    PressureCumulativeFrequencyCalculator,
)
import argparse


def reproduce_bspline_and_save(coordinates: Any, filename: Any) -> None:
    x_values, y_values = zip(*coordinates)

    # Generate a B-Spline curve with a variable number of control points
    num_points = min(5, len(x_values) - 1)

    # FIXME: Why do we specify `k`?
    tck = make_interp_spline(x_values, y_values, k=num_points)
    x_bspline = np.linspace(min(x_values), max(x_values), 1000)
    y_bspline = tck(x_bspline)

    # Create and save the B-Spline curve graph
    plt.plot(x_bspline, y_bspline, color="red", label="B-Spline Curve")
    plt.legend()
    plt.savefig(filename)  # Save the graph as a PNG file
    print(f"\nB-Spline Curve graph saved as {filename}")


def write_bspline_to_file(
    filename: str, coordinates: list[tuple[float, float]]
) -> None:
    krita_settings_writer = KritaSettingsWriterToFile()
    krita_settings_writer.write_settings(filename, coordinates)


def create_pressure_graph(pen_pressures: NormalizedPressure) -> None:
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

    coordinates = list(zip(scaled_pressures, scaled_frequencies))

    # Reproduce the cumulative line graph using a B-Spline curve
    filename = "graph.png"
    reproduce_bspline_and_save(coordinates, filename)

    # Write B-Spline curve coordinates to a file in the desired format
    krita_settings_filename = "pen_pressure.txt"
    write_bspline_to_file(krita_settings_filename, coordinates)


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
