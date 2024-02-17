from abc import ABC, abstractmethod


class AbstractKritaSettingsWriter(ABC):
    @abstractmethod
    def write_settings(
        self, filename: str, x_values: list[float], y_values: list[float]
    ) -> None:
        pass
