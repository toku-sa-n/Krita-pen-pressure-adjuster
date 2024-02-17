from abstract_normalized_pressure_input import AbstractNormalizedPressureInput
from abstract_pen_pressure_input import AbstractRawPenPressureInput


class NormalizedPressureInput(AbstractNormalizedPressureInput):
    def __init__(self, pressure_input: AbstractRawPenPressureInput) -> None:
        self.pressure_input = pressure_input

    def monitor_pressure(self) -> list[float] | None:
        pen_pressures = self.pressure_input.monitor_pressure()

        if pen_pressures:
            # Normalize the pen pressures to the range [0, 1]
            min_pressure = pen_pressures.min_pressure
            max_pressure = pen_pressures.max_pressure
            normalized_pressures = [
                (pressure - min_pressure) / (max_pressure - min_pressure)
                for pressure in pen_pressures.pressures
            ]
            return normalized_pressures
        else:
            return None
