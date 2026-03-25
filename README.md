# Automatic Screenshot Sorter 🖼️

A small Python automation tool that watches a folder and automatically organizes screenshots into date-based folders.

## Features

* Watches a folder in real-time for new files (using `watchdog`)
* Detects screenshots by name (`Screenshot*`) and file type (`.png`, `.jpg`)
* Creates daily folders inside `Screenshots` automatically
* Handles duplicates by appending `_1`, `_2`, etc.
* Lightweight and simple — just run and forget

## Usage

1. Install dependencies:

```bash
pip install watchdog
```

2. Update the `watch_folder` variable in `main.py` to the folder you want to watch (default is Desktop).

3. Run the script:

```bash
python main.py
```

4. Sit back while your screenshots get neatly organized.

## Notes

* Windows users: some screenshot tools save files in `Pictures/Screenshots` instead of Desktop. Update the path accordingly.
* The script handles multiple events per file gracefully, so duplicates won’t crash it.
* Designed for learning and small-scale automation — not a production-level tool.

## License

MIT License, do whatever you want, just don’t blame me if your cat steps on the keyboard.
