from abstract_krita_settings_writer import AbstractKritaSettingsWriter
from datatypes.normalized.frequency import NormalizedFrequency
from datatypes.normalized.pressure import NormalizedPressure


class KritaSettingsWriterToFile(AbstractKritaSettingsWriter):
    def write_settings(
        self,
        filename: str,
        coordinates: list[tuple[NormalizedPressure, NormalizedFrequency]],
    ) -> None:
        with open(filename, "w") as file:
            file.write("tabletPressureCurve=")
            for x, y in coordinates:
                file.write(f"{x:.6f},{y:.6f};")

            file.write("\n")

        print(f"\nB-Spline Curve coordinates saved to {filename}")
