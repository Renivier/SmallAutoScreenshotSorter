from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
from datetime import datetime
import time


# Main screenshots folder
screenshots_dir = Path("Screenshots uwu")
screenshots_dir.mkdir(exist_ok=True)
class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix.lower() not in (".png", ".jpg"):
            return

        if not path.stem.startswith("Screenshot"):
            return
        time.sleep(0.2)
        print(f"Found screenshot: {path}")
        today = datetime.now().strftime("%Y-%m-%d")
        date_folder = screenshots_dir / today
        date_folder.mkdir(exist_ok=True)
        target = date_folder / path.name
        counter = 1
        while target.exists():
            target = date_folder / f"{path.stem}_{counter}{path.suffix}"
            counter += 1
        if not path.exists():
            return
        shutil.move(str(path), str(target))
watch_folder = Path.home() / "Downloads"  
observer = Observer()
handler = ScreenshotHandler()
observer.schedule(handler, str(watch_folder), recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()


class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        path = Path(event.src_path)