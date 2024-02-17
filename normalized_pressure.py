from dataclasses import dataclass


@dataclass(frozen=True)
class NormalizedPressure:
    """
    Normalized pen pressure data.

    This class contains the normalized pen pressure values, which are scaled
    to the range [0, 1].
    """

    pressure: float

    def __post_init__(self) -> None:
        if not 0 <= self.pressure <= 1:
            raise ValueError("Pressure value must be between 0 and 1")
