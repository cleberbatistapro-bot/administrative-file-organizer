# Organizador de Arquivos Administrativos

Programa de automação que organiza arquivos de uma pasta de entrada,
classifica cada um por tipo e move para subpastas de destino.
Ao final, gera um relatório da execução.

## Status do projeto

✅ Concluído — 10 fases entregues

## Funcionalidades

- Classifica arquivos por tipo: imagens, documentos, planilhas, PDFs, vídeos, áudios, código, arquivos compactados
- Move cada arquivo para a subpasta correta automaticamente
- Trata arquivos duplicados adicionando timestamp no nome
- Gera relatório de execução em .txt com data e hora
- Aceita pastas personalizadas via linha de comando

## Como usar

Instale o ambiente virtual e ative:
python -m venv .venv
.venv\Scripts\activate

Rode com as pastas padrão:
python main.py

Rode com pastas personalizadas:
python main.py --input C:\SuaPasta --output C:\Destino

## Estrutura do projeto

administrative-file-organizer/
├── docs/                     # documentação completa em .md e .pdf
├── src/organizer/
│   ├── paths.py              # caminhos e criação de pastas
│   ├── scanner.py            # leitura dos arquivos de entrada
│   ├── classifier.py         # classificação por tipo
│   ├── mover.py              # movimentação e duplicatas
│   └── reporter.py           # geração do relatório
├── data/
│   ├── input/                # pasta de entrada
│   └── output/               # pasta de saída organizada
└── main.py                   # orquestra todo o programa


## Tecnologias

- Python 3.x
- pathlib
- shutil
- argparse
- datetime

## Autor

Desenvolvido por Cleber Batista — OonaTech
Automação de processos administrativos para pequenas e médias empresas.