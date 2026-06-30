FILE_CATEGORIES = {
    ".pdf": "Documentos",
    ".txt": "Documentos",
    ".docx": "Documentos",
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".csv": "Planilhas",
    ".xlsx": "Planilhas",
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",
}

def classify_file(file_path):
    """Recebe um arquivo e retorna sua categoria."""
    extension = file_path.suffix.lower()
    return FILE_CATEGORIES.get(extension, "Outros")
