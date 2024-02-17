from evdev import InputDevice, ecodes
import asyncio
import matplotlib.pyplot as plt
import signal
import numpy as np
from scipy.interpolate import make_interp_spline
from typing import Any
from abc import ABC, abstractmethod


class AbstractPenPressureInput(ABC):
    @abstractmethod
    async def monitor_event(self) -> None:
        pass

    @abstractmethod
    def monitor_pressure(self) -> list[int] | None:
        pass


class PenPressureInput(AbstractPenPressureInput):
    def __init__(self, device_path: str) -> None:
        self.device_path = device_path
        self.device = InputDevice(device_path)
        self.pen_pressures: list[int] = []

    async def monitor_event(self) -> None:
        async for event in self.device.async_read_loop():
            if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_PRESSURE:
                # Store pen pressure
                self.pen_pressures.append(event.value)

                # Display pen pressure
                print(f"Pen Pressure: {event.value}")

    def monitor_pressure(self) -> list[int] | None:
        try:
            print(
                f"Monitoring pen pressure on {self.device.name} (event device: {self.device_path})"
            )

            # Ensure the program can be interrupted with Ctrl+C
            loop = asyncio.get_event_loop()
            stop_event = asyncio.Event()
            for signame in ("SIGINT", "SIGTERM"):
                loop.add_signal_handler(getattr(signal, signame), stop_event.set)

            # Start monitoring events
            asyncio.ensure_future(self.monitor_event())

            try:
                # Run the event loop until the stop event is set
                loop.run_until_complete(stop_event.wait())
            except KeyboardInterrupt:
                pass  # Ignore KeyboardInterrupt here, as it is used to stop the loop

            return self.pen_pressures

        except FileNotFoundError:
            print(f"Error: Device not found at {self.device_path}")
            return None


def reproduce_bspline_and_save(x_values: Any, y_values: Any, filename: Any) -> None:
    # Generate a B-Spline curve with a variable number of control points
    num_points = min(5, len(x_values) - 1)
    tck = make_interp_spline(x_values, y_values, k=num_points)
    x_bspline = np.linspace(min(x_values), max(x_values), 1000)
    y_bspline = tck(x_bspline)

    # Create and save the B-Spline curve graph
    plt.plot(x_bspline, y_bspline, color="red", label="B-Spline Curve")
    plt.legend()
    plt.savefig(filename)  # Save the graph as a PNG file
    print(f"\nB-Spline Curve graph saved as {filename}")


def write_bspline_to_file(x_values: Any, y_values: Any, filename: Any) -> None:
    # Write B-Spline curve coordinates to a file in the desired format
    with open(filename, "w") as file:
        file.write("tabletPressureCurve=")
        for x, y in zip(x_values, y_values):
            file.write(f"{x:.6f},{y:.6f};")

    print(f"\nB-Spline Curve coordinates saved to {filename}")


def create_pressure_graph(pen_pressures: Any) -> None:
    if pen_pressures is not None:
        # Calculate the cumulative frequency for each pressure value
        unique_pressures, frequencies = np.unique(pen_pressures, return_counts=True)
        cumulative_frequencies = np.cumsum(frequencies)

        # Scale both X and Y axes to the range [0, 1]
        scaled_pressures = unique_pressures / max(unique_pressures)
        scaled_frequencies = cumulative_frequencies / max(cumulative_frequencies)

        # Create a cumulative line graph
        plt.plot(
            scaled_pressures, scaled_frequencies, color="blue", label="Original Data"
        )
        plt.title("Scaled Cumulative Pressure Frequency")
        plt.xlabel("Scaled Pen Pressure (0-1)")
        plt.ylabel("Scaled Cumulative Frequency (0-1)")
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        # Reproduce the cumulative line graph using a B-Spline curve
        filename = "graph.png"
        reproduce_bspline_and_save(scaled_pressures, scaled_frequencies, filename)

        # Write B-Spline curve coordinates to a file in the desired format
        krita_settings_filename = "pen_pressure.txt"
        write_bspline_to_file(
            scaled_pressures, scaled_frequencies, krita_settings_filename
        )


def run(pressure_input: AbstractPenPressureInput) -> None:
    # Monitor pen pressure
    pen_pressures = pressure_input.monitor_pressure()

    # Create and display the pressure graph
    if pen_pressures:
        create_pressure_graph(pen_pressures)


def main() -> None:
    # Specify the correct event device path for your pen input device
    # You can find the path using 'ls /dev/input/' or 'evtest'
    device_path = (
        "/dev/input/event13"  # Replace 'event13' with the correct event device
    )

    pressure_input = PenPressureInput(device_path)

    run(pressure_input)


if __name__ == "__main__":
    main()
