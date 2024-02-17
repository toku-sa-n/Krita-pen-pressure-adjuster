import argparse

from scipy.interpolate import make_interp_spline

from abstract_graph_plotter import AbstractGraphPlotter
from abstract_krita_settings_writer import AbstractKritaSettingsWriter
from abstract_normalized_pressure_input import AbstractNormalizedPressureInput
from abstract_pressure_cumulative_frequency_calculator import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from evdev_pen_pressure_input import EvdevPenPressureInput
from graph_plotter import GraphPlotter
from krita_settings_writer_to_file import KritaSettingsWriterToFile
from normalized_frequency import NormalizedFrequency
from normalized_pressure import NormalizedPressure
from normalized_pressure_input import NormalizedPressureInput
from pressure_cumulative_frequency_calculator import (
    PressureCumulativeFrequencyCalculator,
)


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
