from abc import ABC, abstractmethod


class AbstractKritaSettingsWriter(ABC):
    @abstractmethod
    def write_settings(
        self, filename: str, coordinates: list[tuple[float, float]]
    ) -> None:
        pass
