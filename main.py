from src.organizer.paths import ensure_directories_exist
from src.organizer.scanner import list_files
from src.organizer.mover import move_file
from src.organizer.reporter import generate_report

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
    results =[]
    for file in files:
        result = move_file(file)
        results.append(result)
        print(f" Movido: {file.name}")

    generate_report(results, total)
    print(f"Concluído! {total} arquivo(s) organizado(s).")


if __name__ == "__main__":
    main()

