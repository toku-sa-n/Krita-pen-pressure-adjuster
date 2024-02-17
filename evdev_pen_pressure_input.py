from evdev import InputDevice, ecodes
import asyncio
import signal
from typing import Any
from abstract_pen_pressure_input import AbstractPenPressureInput


class EvdevPenPressureInput(AbstractPenPressureInput):
    def __init__(self, device_path: str) -> None:
        self.device_path = device_path
        self.device = InputDevice(device_path)
        self.pen_pressures: list[int] = []

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

    async def monitor_event(self) -> None:
        async for event in self.device.async_read_loop():
            if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_PRESSURE:
                # Store pen pressure
                self.pen_pressures.append(event.value)

                # Display pen pressure
                print(f"Pen Pressure: {event.value}")

    # TODO: Get the actual min and max pressure values from the device
    def max_pressure(self) -> int:
        return 4095

    def min_pressure(self) -> int:
        return 0
