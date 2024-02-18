from abc import ABC, abstractmethod

from datatypes.normalized.normalized_frequency import NormalizedFrequency
from datatypes.normalized.normalized_pressure import NormalizedPressure


class AbstractGraphPlotter(ABC):
    @abstractmethod
    def plot_graph(
        self,
        filename: str,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
