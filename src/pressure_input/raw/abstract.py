from abc import ABC, abstractmethod

from datatypes.raw.pressure import RawPenPressure


class AbstractRawPenPressureInput(ABC):
    @abstractmethod
    def monitor_pressure(self) -> list[RawPenPressure] | None:
        pass
