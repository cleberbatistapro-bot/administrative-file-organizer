import shutil

from src.organizer.paths import OUTPUT_DIR
from src.organizer.classifier import classify_file 

def move_file(file_path):
    """Move um arquivo para a subpasta de sua categoria, dentro de OUTPUT_DIR."""
    category = classify_file(file_path)
    category_dir = OUTPUT_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)

    destination = category_dir / file_path.name
    shutil.move(file_path, destination)
    