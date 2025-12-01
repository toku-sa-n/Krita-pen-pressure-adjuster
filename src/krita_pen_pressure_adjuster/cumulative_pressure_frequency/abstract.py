from abc import ABC, abstractmethod

from krita_pen_pressure_adjuster.datatypes.normalized.frequency import NormalizedFrequency
from krita_pen_pressure_adjuster.datatypes.normalized.pressure import NormalizedPressure


class AbstractPressureCumulativeFrequencyCalculator(ABC):
    @abstractmethod
    def calculate_pressure_cumulative_frequency(
        self, pen_pressures: list[NormalizedPressure]
    ) -> list[tuple[NormalizedPressure, NormalizedFrequency]]:
        pass
