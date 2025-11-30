import sys

from krita_pen_pressure_adjuster.config_writer.abstract import (
    AbstractKritaSettingsWriter,
)
from krita_pen_pressure_adjuster.config_writer.file import KritaSettingsWriterToFile
from krita_pen_pressure_adjuster.cumulative_pressure_frequency.abstract import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from krita_pen_pressure_adjuster.cumulative_pressure_frequency.impl import (
    PressureCumulativeFrequencyCalculator,
)
from krita_pen_pressure_adjuster.datatypes.normalized.frequency import NormalizedFrequency
from krita_pen_pressure_adjuster.datatypes.normalized.pressure import NormalizedPressure
from krita_pen_pressure_adjuster.plotter.abstract import AbstractGraphPlotter
from krita_pen_pressure_adjuster.plotter.impl import GraphPlotter
from krita_pen_pressure_adjuster.pressure_input.normalized.abstract import (
    AbstractNormalizedPressureInput,
)
from krita_pen_pressure_adjuster.pressure_input.normalized.impl import (
    NormalizedPressureInput,
)
from krita_pen_pressure_adjuster.pressure_input.raw.evdev import EvdevPenPressureInput


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
