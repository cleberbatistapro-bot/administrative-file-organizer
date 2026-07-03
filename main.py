from src.organizer.paths import ensure_directories_exist
from src.organizer.scanner import list_files
from src.organizer.mover import move_file
from src.organizer.reporter import generate_report
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Organizador de Arquivos Administrativos.")
    parser.add_argument("--input", default="data/input", help="Pasta de entrada")
    parser.add_argument("--output", default="data/output", help="Pasta de saída")
    args = parser.parse_args()
    input_dir = Path(args.input)
    output_dir = Path(args.output)
    print("=== Organizador de Arquivos ===")
    print()

    ensure_directories_exist(output_dir)

    files = list_files(input_dir)
    total = len(files)

    if total == 0:
        print("Nenhum arquivo encontrado em 'input/'.")
        return
    
    print(f"Arquivos encontrados: {total}")
    print()
    results =[]
    for file in files:
        result = move_file(file,output_dir)
        results.append(result)
        print(f" Movido: {file.name}")

    generate_report(results, total, output_dir)
    print(f"Concluído! {total} arquivo(s) organizado(s).")


if __name__ == "__main__":
    main()

