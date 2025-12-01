from abc import ABC, abstractmethod

from krita_pen_pressure_adjuster.datatypes.raw.pressure import RawPenPressure


class AbstractRawPenPressureInput(ABC):
    @abstractmethod
    def monitor_pressure(self) -> list[RawPenPressure] | None:
        pass
