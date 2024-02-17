from abstract_krita_settings_writer import AbstractKritaSettingsWriter


class KritaSettingsWriterToFile(AbstractKritaSettingsWriter):
    def write_settings(
        self, filename: str, coordinates: list[tuple[float, float]]
    ) -> None:
        with open(filename, "w") as file:
            file.write("tabletPressureCurve=")
            for x, y in coordinates:
                file.write(f"{x:.6f},{y:.6f};")

        print(f"\nB-Spline Curve coordinates saved to {filename}")
