from pathlib import Path

# Caminho deste arquivo (paths.py)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

#Pastas de dados
DATA_DIR = ROOT_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

def ensure_directories_exist():
    """
    Garante que os diretórios de entrada e saída existam.
    Se não existirem, eles serão criados.
    """
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)



