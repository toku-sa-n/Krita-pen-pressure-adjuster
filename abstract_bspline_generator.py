from abc import ABC, abstractmethod
from typing import Callable
from normalized_pressure import NormalizedPressure
from normalized_frequency import NormalizedFrequency


class AbstractBSplineGenerator(ABC):
    @abstractmethod
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        pass
