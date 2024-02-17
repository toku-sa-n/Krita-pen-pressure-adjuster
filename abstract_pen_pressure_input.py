from abc import ABC, abstractmethod


class AbstractPenPressureInput(ABC):
    @abstractmethod
    def monitor_pressure(self) -> list[int] | None:
        pass
