from flask import Flask, request, jsonify, send_from_directory
from main import run_organizer
import os
import zipfile
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime

app = Flask(__name__, static_folder="interface/static")


def get_area_trabalho():
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
              r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
        desktop = winreg.QueryValueEx(key, "Desktop")[0]
        winreg.CloseKey(key)
        return Path(desktop) / "Organizado"
    except Exception:
        return Path.home() / "Desktop" / "Organizado"


def criar_backup(input_dir):
    destino_backup = get_area_trabalho() / "Backups"
    destino_backup.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_path = destino_backup / f"backup_{timestamp}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in Path(input_dir).iterdir():
            if arquivo.is_file():
                zipf.write(arquivo, arquivo.name)
    return str(zip_path)


@app.route("/")
def index():
    return send_from_directory("interface", "index.html")


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("interface/static", filename)


@app.route("/selecionar-pasta", methods=["GET"])
def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", True)
    pasta = filedialog.askdirectory(title="Selecione a pasta a organizar")
    root.destroy()
    if not pasta:
        return jsonify({"pasta": ""})
    pasta_windows = pasta.replace("/", "\\")
    return jsonify({"pasta": pasta_windows})


@app.route("/organizar", methods=["POST"])
def organizar():
    dados = request.get_json()
    input_dir  = dados.get("input_dir", "")
    modo       = dados.get("modo", "1")
    fazer_backup = dados.get("backup", False)

    if not input_dir:
        return jsonify({"erro": "Nenhuma pasta informada."}), 400

    if not os.path.exists(input_dir):
        return jsonify({"erro": "Pasta não encontrada no computador."}), 400

    if modo == "2":
        output_dir = str(get_area_trabalho())
    else:
        output_dir = input_dir

    try:
        if fazer_backup:
            criar_backup(input_dir)

        resultado = run_organizer(input_dir, output_dir)
        resultado["output_dir"] = output_dir
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    import threading
    import webview

    def start_flask():
        app.run(debug=False, port=5000)

    t = threading.Thread(target=start_flask)
    t.daemon = True
    t.start()

    webview.create_window(
        "Organizador de Arquivos",
        "http://127.0.0.1:5000",
        width=900,
        height=700
    )
    webview.start()