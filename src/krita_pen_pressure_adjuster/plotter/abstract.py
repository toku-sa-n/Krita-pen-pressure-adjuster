from abc import ABC, abstractmethod

from krita_pen_pressure_adjuster.datatypes.normalized.frequency import NormalizedFrequency
from krita_pen_pressure_adjuster.datatypes.normalized.pressure import NormalizedPressure


class AbstractGraphPlotter(ABC):
    @abstractmethod
    def plot_graph(
        self,
        filename: str,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
