from datetime import datetime



def generate_report(results, total, output_dir):
    """Gera um arquivo .txt com o relatório de execução."""
    timestamp = datetime.now().strftime("Y%m%d_%H%M%S")
    report_name = f"relatorio_{timestamp}.txt"
    report_path = output_dir / report_name
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("Relatório de Execução\n")
        f.write(f"Data: {datetime.now().strftime('%d%m%Y %H:%M:%S')}\n")
        f.write(f"Total de arquivos processados: {total}\n")
        f.write("\n")
        f.write("Arquivos movidos:\n")
        for result in results:
            f.write(f" {result['original']} -> {result['destination']}\n")
            if result["renamed"]:
                f.write(f"  (Renomeado por duplicata)\n")
