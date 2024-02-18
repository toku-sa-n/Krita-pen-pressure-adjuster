from .abstract import AbstractNormalizedPressureInput
from ..raw.abstract import AbstractRawPenPressureInput
from datatypes.normalized.base import Normalized
from datatypes.normalized.normalized_pressure import NormalizedPressure


class NormalizedPressureInput(AbstractNormalizedPressureInput):
    def __init__(self, pressure_input: AbstractRawPenPressureInput) -> None:
        self.pressure_input = pressure_input

    def monitor_pressure(self) -> list[NormalizedPressure] | None:
        pen_pressures = self.pressure_input.monitor_pressure()

        if pen_pressures:
            # Normalize the pen pressures to the range [0, 1]
            normalized_pressures = [
                NormalizedPressure(
                    Normalized(
                        (x.pressure - x.min_pressure)
                        / (x.max_pressure - x.min_pressure)
                    )
                )
                for x in pen_pressures
            ]
            return normalized_pressures
        else:
            return None
