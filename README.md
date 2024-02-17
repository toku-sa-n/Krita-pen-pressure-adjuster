# Global pen pressure setting adjuster for Krita

## Usage

1. Clone this repository and `cd` into it.

    ```bash
    git clone https://github.com/toku-sa-n/Krita-pen-pressure-adjuster
    cd Krita-pen-pressure-adjuster
    ```

2. Run the script. You may need the root privilege to access the input device file.

    ```bash
    python src/main.py /dev/input/eventX
    ```

    where `/dev/input/eventX` is the path to the tablet input device file. You can find the path by running `evtest` and looking for the device name.

3. Use your pen to draw lines with different pressure levels. You don't need to draw with Krita. The script will collect the pressure data. Press `Ctrl+C` to finish the data collection. Note that few strokes will not be enough to generate a good pen pressure curve.

4. Two files will be generated: `graph.png` and `pen_pressure.txt`. The former contains a cumulative graph of the actual pen pressure and its frequency, and a B-Spline curve that approximates the graph. The latter contains the Krita configuration line for the pen pressure curve.     Overwrite the `tabletPressureCurve` line in the [`kritarc`](https://docs.krita.org/en/reference_manual/preferences.html) file with the line in `pen_pressure.txt`.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
