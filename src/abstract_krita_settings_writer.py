from abc import ABC, abstractmethod

from normalized_frequency import NormalizedFrequency
from normalized_pressure import NormalizedPressure


class AbstractKritaSettingsWriter(ABC):
    @abstractmethod
    def write_settings(
        self,
        filename: str,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
