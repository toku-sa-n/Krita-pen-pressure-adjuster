from abc import ABC, abstractmethod
from typing import Callable

from krita_pen_pressure_adjuster.datatypes.normalized.frequency import NormalizedFrequency
from krita_pen_pressure_adjuster.datatypes.normalized.pressure import NormalizedPressure


class AbstractBSplineGenerator(ABC):
    @abstractmethod
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        pass
