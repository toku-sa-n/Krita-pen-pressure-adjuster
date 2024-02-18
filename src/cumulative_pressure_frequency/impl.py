import numpy as np

from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.pressure import NormalizedPressure

from .abstract import AbstractPressureCumulativeFrequencyCalculator


class PressureCumulativeFrequencyCalculator(
    AbstractPressureCumulativeFrequencyCalculator
):
    def calculate_pressure_cumulative_frequency(
        self, pen_pressures: list[NormalizedPressure]
    ) -> list[tuple[NormalizedPressure, NormalizedFrequency]]:
        pressures = list(map(lambda x: x.value, pen_pressures))

        scaled_pressures, frequencies = np.unique(pressures, return_counts=True)
        cumulative_frequencies = np.cumsum(frequencies)
        scaled_frequencies = cumulative_frequencies / max(cumulative_frequencies)

        normalized_pressures = list(map(NormalizedPressure, scaled_pressures))
        normalized_frequencies = list(map(NormalizedFrequency, scaled_frequencies))

        return list(zip(normalized_pressures, normalized_frequencies))
