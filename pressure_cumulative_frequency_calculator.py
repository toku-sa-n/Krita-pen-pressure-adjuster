from abstract_pressure_cumulative_frequency_calculator import (
    AbstractPressureCumulativeFrequencyCalculator,
)
from normalized_pressure import NormalizedPressure
import numpy as np


class PressureCumulativeFrequencyCalculator(
    AbstractPressureCumulativeFrequencyCalculator
):
    def calculate_pressure_cumulative_frequency(
        self, pen_pressures: NormalizedPressure
    ) -> list[tuple[float, float]]:
        scaled_pressures, frequencies = np.unique(
            pen_pressures.pressures, return_counts=True
        )
        cumulative_frequencies = np.cumsum(frequencies)
        scaled_frequencies = cumulative_frequencies / max(cumulative_frequencies)

        return list(zip(scaled_pressures, scaled_frequencies))
