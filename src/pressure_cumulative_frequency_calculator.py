import numpy as np

from abstract_pressure_cumulative_frequency_calculator import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from normalized_frequency import NormalizedFrequency
from normalized_pressure import NormalizedPressure


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
