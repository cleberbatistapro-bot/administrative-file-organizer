FILE_CATEGORIES = {
    ".pdf":  "PDF",
    ".doc":  "Word",
    ".docx": "Word",
    ".txt":  "Texto",
    ".png":  "Imagens",
    ".jpg":  "Imagens",
    ".jpeg": "Imagens",
    ".gif":  "Imagens",
    ".bmp":  "Imagens",
    ".webp": "Imagens",
    ".csv":  "Planilhas",
    ".xls":  "Planilhas",
    ".xlsx": "Planilhas",
    ".zip":  "Compactados",
    ".rar":  "Compactados",
    ".7z":   "Compactados",
}

def classify_file(file_path):
    """Recebe um arquivo e retorna sua categoria."""
    extension = file_path.suffix.lower()
    return FILE_CATEGORIES.get(extension, "Outros")