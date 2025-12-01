from dataclasses import dataclass


@dataclass(frozen=True)
class RawPenPressure:
    """
    Raw pen pressure data.

    This class contains the minimum and maximum pressure values because the
    range of pressure values is implementation-specific.
    """

    min_pressure: int
    max_pressure: int

    pressure: int

    def __post_init__(self) -> None:
        if not self.min_pressure <= self.pressure <= self.max_pressure:
            raise ValueError(
                "Pressure value must be between min_pressure and max_pressure"
            )
