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

def run_organizer(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    ensure_directories_exist(output_dir)

    files = list_files(input_dir)
    total = len(files)

    if total == 0:
        return {
            "total": 0,
            "movidos": 0,
            "nao_movidos": 0,
            "por_tipo": {},
            "resultados": []
        }

    results = []
    erros = 0
    for file in files:
        try:
            result = move_file(file, output_dir)
            results.append(result)
        except Exception as e:
            erros += 1

    generate_report(results, total, output_dir)

    por_tipo = {}
    for r in results:
        ext = Path(r["original"]).suffix.lower().lstrip(".")
        if not ext:
            ext = "outros"
        por_tipo[ext] = por_tipo.get(ext, 0) + 1

    return {
        "total": total,
        "movidos": len(results),
        "nao_movidos": erros,
        "por_tipo": por_tipo,
        "resultados": results
        }


if __name__ == "__main__":
    main()

