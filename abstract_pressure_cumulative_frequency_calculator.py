from abc import ABC, abstractmethod
from normalized_pressure import NormalizedPressure


class AbstractPressureCumulativeFrequencyCalculator(ABC):
    @abstractmethod
    def calculate_pressure_cumulative_frequency(
        self, pen_pressures: list[NormalizedPressure]
    ) -> list[tuple[float, float]]:
        pass
