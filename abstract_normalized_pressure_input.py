from abc import ABC, abstractmethod


class AbstractNormalizedPressureInput(ABC):
    """An abstract base class for normalized pressure input."""

    @abstractmethod
    def monitor_pressure(self) -> list[float] | None:
        """
        Monitor the pressure and return a list of float values or None.

        The list of float values should be normalized to the range [0, 1].
        """
        pass
