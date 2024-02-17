from abc import ABC, abstractmethod


class AbstractPenPressureInput(ABC):
    @abstractmethod
    async def monitor_event(self) -> None:
        pass

    @abstractmethod
    def monitor_pressure(self) -> list[int] | None:
        pass
