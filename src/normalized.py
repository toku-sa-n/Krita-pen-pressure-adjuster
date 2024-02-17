from dataclasses import dataclass


@dataclass(frozen=True)
class Normalized:
    """
    An float value normalized to the range [0, 1].
    """

    value: float

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 1:
            raise ValueError("Value must be between 0 and 1")

    def __str__(self) -> str:
        return f"{self.value}"
