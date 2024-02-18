import argparse
import sys

from scipy.interpolate import make_interp_spline

from abstract_graph_plotter import AbstractGraphPlotter
from abstract_krita_settings_writer import AbstractKritaSettingsWriter
from pressure_input.normalized.abstract import (
    AbstractNormalizedPressureInput,
)
from abstract_pressure_cumulative_frequency_calculator import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from pressure_input.raw.evdev import EvdevPenPressureInput
from graph_plotter import GraphPlotter
from krita_settings_writer_to_file import KritaSettingsWriterToFile
from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.pressure import NormalizedPressure
from pressure_input.normalized.impl import NormalizedPressureInput
from pressure_cumulative_frequency_calculator import (
    PressureCumulativeFrequencyCalculator,
)


def run(
    pressure_input: AbstractNormalizedPressureInput,
    freq_calculator: AbstractPressureCumulativeFrequencyCalculator,
    graph_plotter: AbstractGraphPlotter,
    config_writer: AbstractKritaSettingsWriter,
) -> None:
    pen_pressures = pressure_input.monitor_pressure()

    if pen_pressures:
        pressure_freq = freq_calculator.calculate_pressure_cumulative_frequency(
            pen_pressures
        )

        graph_plotter.plot_graph("graph.png", pressure_freq)

        config_writer.write_settings("pen_pressure.txt", pressure_freq)


def main() -> None:
    input_path = (
        sys.argv[1] if len(sys.argv) > 1 else sys.exit("No input path provided.")
    )

    pressure_input = EvdevPenPressureInput(input_path)
    normalized_pressure_input = NormalizedPressureInput(pressure_input)

    freq_calculator = PressureCumulativeFrequencyCalculator()

    graph_plotter = GraphPlotter()
    config_writer = KritaSettingsWriterToFile()

    run(normalized_pressure_input, freq_calculator, graph_plotter, config_writer)


if __name__ == "__main__":
    main()
