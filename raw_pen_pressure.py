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

    pressures: list[int]
