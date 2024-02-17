from abc import ABC, abstractmethod
from normalized_pressure import NormalizedPressure
from normalized_frequency import NormalizedFrequency


class AbstractKritaSettingsWriter(ABC):
    @abstractmethod
    def write_settings(
        self,
        filename: str,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
