from typing import Callable
from abstract_bspline_curve_reproducer import AbstractBSplineCurveReproducer
from scipy.interpolate import make_interp_spline
from normalized_pressure import NormalizedPressure
from normalized_frequency import NormalizedFrequency


class BSplineCurveReproducer(AbstractBSplineCurveReproducer):
    def reproduce_bspline_and_save(
        self,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> Callable[[float], float]:
        f: Callable[[float], float] = make_interp_spline(*zip(*coordinates))
        return f
