from abstract_normalized_pressure_input import AbstractNormalizedPressureInput
from abstract_pen_pressure_input import AbstractRawPenPressureInput
from normalized_pressure import NormalizedPressure


class NormalizedPressureInput(AbstractNormalizedPressureInput):
    def __init__(self, pressure_input: AbstractRawPenPressureInput) -> None:
        self.pressure_input = pressure_input

    def monitor_pressure(self) -> NormalizedPressure | None:
        pen_pressures = self.pressure_input.monitor_pressure()

        if pen_pressures:
            # Normalize the pen pressures to the range [0, 1]
            normalized_pressures = [
                (pressure - pen_pressures.min_pressure)
                / (pen_pressures.max_pressure - pen_pressures.min_pressure)
                for pressure in pen_pressures.pressures
            ]
            return NormalizedPressure(normalized_pressures)
        else:
            return None
