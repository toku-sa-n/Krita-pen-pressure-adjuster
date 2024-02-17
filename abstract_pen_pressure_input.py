from abc import ABC, abstractmethod
from raw_pen_pressure import RawPenPressure


class AbstractRawPenPressureInput(ABC):
    @abstractmethod
    def monitor_pressure(self) -> list[RawPenPressure] | None:
        pass
