from abc import ABC, abstractmethod
from normalized_pressure import NormalizedPressure
from normalized_frequency import NormalizedFrequency


class AbstractGraphPlotter(ABC):
    @abstractmethod
    def plot_graph(
        self,
        filename: str,
        frequencies: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
