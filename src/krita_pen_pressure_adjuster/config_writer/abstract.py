from abc import ABC, abstractmethod

from krita_pen_pressure_adjuster.datatypes.normalized.frequency import NormalizedFrequency
from krita_pen_pressure_adjuster.datatypes.normalized.pressure import NormalizedPressure


class AbstractKritaSettingsWriter(ABC):
    @abstractmethod
    def write_settings(
        self,
        filename: str,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        pass
