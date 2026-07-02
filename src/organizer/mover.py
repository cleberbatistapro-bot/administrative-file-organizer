import shutil
from datetime import datetime


from src.organizer.paths import OUTPUT_DIR
from src.organizer.classifier import classify_file 

def move_file(file_path):
    """Move um arquivo para a subpasta de sua categoria, dentro de OUTPUT_DIR."""
    category = classify_file(file_path)
    category_dir = OUTPUT_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    destination = category_dir / file_path.name

    renamed = False

    if destination.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%m%S")
        new_name = file_path.stem + "_" + timestamp + file_path.suffix
        destination = category_dir / new_name
        renamed = True

   
    shutil.move(file_path, destination)
    return{
        "original": file_path.name,
        "destination": category,
        "renamed": renamed
    }


    