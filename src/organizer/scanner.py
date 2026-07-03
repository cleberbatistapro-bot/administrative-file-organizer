

def list_files(input_dir):
    """Retorna a lista de arquivos dentro da pasta de entrada."""
    return [item for item in input_dir.iterdir() if item.is_file()]

