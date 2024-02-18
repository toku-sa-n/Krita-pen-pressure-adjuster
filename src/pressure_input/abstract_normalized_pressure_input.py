from abc import ABC, abstractmethod

from normalized_pressure import NormalizedPressure


class AbstractNormalizedPressureInput(ABC):
    """An abstract base class for normalized pressure input."""

    @abstractmethod
    def monitor_pressure(self) -> list[NormalizedPressure] | None:
        """
        Monitor the pressure and return a list of normalized pressure values.

        The list of float values should be normalized to the range [0, 1].
        """
        pass
