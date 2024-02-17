from dataclasses import dataclass


@dataclass(frozen=True)
class NormalizedPressure:
    """
    Normalized pen pressure data.

    This class contains the normalized pen pressure values, which are scaled
    to the range [0, 1].
    """

    pressures: list[float]
