from typing import Callable
from abstract_bspline_generator import AbstractBSplineGenerator
from scipy.interpolate import make_interp_spline
from normalized_pressure import NormalizedPressure
from normalized_frequency import NormalizedFrequency


class BSplineGenerator(AbstractBSplineGenerator):
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        f: Callable[[float], float] = make_interp_spline(*zip(*coordinates))
        return f
