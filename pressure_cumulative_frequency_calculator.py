from abstract_pressure_cumulative_frequency_calculator import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from normalized_pressure import NormalizedPressure
from normalized_frequency import NormalizedFrequency
import numpy as np


class PressureCumulativeFrequencyCalculator(
    AbstractPressureCumulativeFrequencyCalculator
):
    def calculate_pressure_cumulative_frequency(
        self, pen_pressures: list[NormalizedPressure]
    ) -> list[tuple[float, NormalizedFrequency]]:
        pressures = list(map(lambda x: x.value, pen_pressures))

        scaled_pressures, frequencies = np.unique(pressures, return_counts=True)
        cumulative_frequencies = np.cumsum(frequencies)
        scaled_frequencies = cumulative_frequencies / max(cumulative_frequencies)

        normalized_frequencies = list(map(NormalizedFrequency, scaled_frequencies))

        return list(zip(scaled_pressures, normalized_frequencies))
