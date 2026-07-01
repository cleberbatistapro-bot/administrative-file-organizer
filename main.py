from src.organizer.paths import ensure_directories_exist
from src.organizer.scanner import list_files
from src.organizer.mover import move_file

def main():
    print("=== Organizador de Arquivos ===")
    print()

    ensure_directories_exist()

    files = list_files()
    total = len(files)

    if total == 0:
        print("Nenhum arquivo encontrado em 'input/'.")
        return
    
    print(f"Arquivos encontrados: {total}")
    print()

    for file in files:
        move_file(file)
        print(f" Movido: {file.name}")

    print()
    print(f"Concluído! {total} arquivo(s) organizado(s).")


if __name__ == "__main__":
    main()

