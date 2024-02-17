from abc import ABC, abstractmethod


class AbstractPenPressureInput(ABC):
    @abstractmethod
    def monitor_pressure(self) -> list[int] | None:
        pass

    @abstractmethod
    def max_pressure(self) -> int:
        pass

    @abstractmethod
    def min_pressure(self) -> int:
        pass
