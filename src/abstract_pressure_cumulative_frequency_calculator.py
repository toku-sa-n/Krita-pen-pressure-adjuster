from abc import ABC, abstractmethod

from datatypes.normalized.normalized_frequency import NormalizedFrequency
from datatypes.normalized.normalized_pressure import NormalizedPressure


class AbstractPressureCumulativeFrequencyCalculator(ABC):
    @abstractmethod
    def calculate_pressure_cumulative_frequency(
        self, pen_pressures: list[NormalizedPressure]
    ) -> list[tuple[NormalizedPressure, NormalizedFrequency]]:
        pass
