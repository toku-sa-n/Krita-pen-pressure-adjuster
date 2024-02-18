from typing import Callable

from scipy.interpolate import make_interp_spline

from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.pressure import NormalizedPressure

from .abstract import AbstractBSplineGenerator


class BSplineGenerator(AbstractBSplineGenerator):
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        f: Callable[[float], float] = make_interp_spline(*zip(*coordinates))
        return f
