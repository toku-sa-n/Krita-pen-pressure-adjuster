# Repository Guidelines

## Project Structure
- `src/krita_pen_pressure_adjuster/`: main logic. `main.py` is the CLI entry exposed as `krita-pen-pressure-adjuster`; `pressure_input/` reads evdev data; `cumulative_pressure_frequency/` builds cumulative frequency; `bspline/` does interpolation; `plotter/` draws graphs; `config_writer/` outputs `pen_pressure.txt`.
- `examples/`: sample good/bad graphs.
- `pyproject.toml` / `uv.lock`: runtime deps (matplotlib, numpy, scipy, evdev) managed by uv.
- `mypy.ini`: `strict = True`; treat type hints as mandatory.

## Setup & Run
- Install deps: `uv sync` (Python 3.12 is the default via `.python-version`; `uv sync --python 3.11` works too and both are supported)
- Find device: `evtest` to locate tablet `/dev/input/eventX` (root often required).
- Run: `uv run krita-pen-pressure-adjuster /dev/input/eventX`  
  Produces `graph.png` and `pen_pressure.txt` in CWD. Stop with `Ctrl+C`.

## Build, Test, Dev
- Type check: `uv run --extra dev mypy src` (strict). Fix missing hints instead of silencing.
- Manual verification: run the command above on real hardware; no automated tests yet, so at least eyeball `graph.png` after changes.

## Coding Style & Naming
- Python 3.11+, PEP8-ish, 4-space indent.
- Use type hints everywhere; reuse `NormalizedPressure` / `NormalizedFrequency`.
- Snake_case for functions/files; abstract classes `AbstractFoo`, concretes `FooImpl` style, matching current modules.
- Keep functions small; start verbs like `plot_`, `calculate_`, `write_`.

## Testing Guidelines
- No unit tests yet. If adding, create `tests/` and prefer pytest; cover interpolation, normalization, and cumulative frequency math.
- Manual check idea: capture at least three pressure levels (light/medium/hard) and confirm the B-spline overlaps source data in `graph.png`.

## Commit & PR
- Commits and PR titles must follow Conventional Commits: `type(scope?): subject` (e.g., `feat(input): add pressure normalization test`, `fix(plotter): clamp x-range`). Keep subject ≤72 chars, present tense, no period.
- PR body should include: summary + motivation, repro/verification steps (commands run), linked issues, and screenshots of `graph.png` when visuals change.

## Language
- All repository content (code, comments, docstrings, docs, PR descriptions, commit messages) must be written in English.
- Chat responses should follow the current agent instructions for conversation style.

## Security & Device Notes
- evdev access may need root; use `sudo` carefully and avoid disturbing other input devices.
- `pen_pressure.txt` replaces `kritarc`’s `tabletPressureCurve`; back up `kritarc` before overwriting.
