from abc import ABC, abstractmethod

from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.pressure import NormalizedPressure


class AbstractKritaSettingsWriter(ABC):
    @abstractmethod
    def write_settings(
        self,
        filename: str,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
