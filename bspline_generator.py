from typing import Callable

from scipy.interpolate import make_interp_spline

from abstract_bspline_generator import AbstractBSplineGenerator
from normalized_frequency import NormalizedFrequency
from normalized_pressure import NormalizedPressure


class BSplineGenerator(AbstractBSplineGenerator):
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        f: Callable[[float], float] = make_interp_spline(*zip(*coordinates))
        return f
