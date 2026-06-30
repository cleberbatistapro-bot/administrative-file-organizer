from src.organizer.paths import INPUT_DIR 

def list_files():
    """Retorna a lista de arquivos dentro da pasta de entrada."""
    return [item for item in INPUT_DIR.iterdir() if item.is_file()]

