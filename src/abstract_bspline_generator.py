from abc import ABC, abstractmethod
from typing import Callable

from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.normalized_pressure import NormalizedPressure


class AbstractBSplineGenerator(ABC):
    @abstractmethod
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        pass
