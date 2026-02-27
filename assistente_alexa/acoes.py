import subprocess
import os
import webbrowser
import shutil

def encontrar_programa(nomes: list) -> str:
    for nome in nomes:
        caminho = shutil.which(nome)
        if caminho:
            return caminho
    return None

def encontrar_em_possiveis(possiveis: list) -> str:
    for p in possiveis:
        if os.path.exists(p):
            return p
    return None

PROGRAMAS = {
    "chrome": (
        ["chrome", "google-chrome", "chromium"],    
        [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
        ]
    ),
    "brave": (
        ["brave", "brave-browser"],
        [
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
            os.path.expanduser(r"~\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe")
        ]
    ),
    "firefox": (
        ["firefox"],
        [
            r"C:\Program Files\Mozilla Firefox\firefox.exe",
            r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        ]
    ),
    "spotify": (
        ["spotify"],
        [
            os.path.expanduser(r"~\AppData\Roaming\Spotify\Spotify.exe"),
            r"C:\Program Files\Spotify\Spotify.exe",
        ]
    ),
    "word": (["winword"], []),
    "excel": (["excel"], []),
    "vs code": (["code"], []),
    "vscode": (["code"], []),
}

PROGRAMAS_SIMPLES = {
    "bloco de notas": "notepad.exe",
    "calculadora": "calc.exe",
    "arquivos": "explorer.exe",
    "paint": "mspaint.exe",
}

SITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "gmail": "https://mail.google.com",
    "whatsapp": "https://web.whatsapp.com",
    "sigaa": "https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do",
    "github": "https://github.com",
    "netflix": "https://netflix.com",
    "instagram": "https://instagram.com",
}

def executar(comando: str) -> str:
    print(f"COMANDO RECEBIDO: '{comando}'")
    comando = comando.lower().strip()

    for chave, (nomes, possiveis) in PROGRAMAS.items():
        if chave in comando:
            caminho = encontrar_programa(nomes) or encontrar_em_possiveis(possiveis)
            if caminho:
                subprocess.Popen(caminho)
                return f"Abrindo o {chave.capitalize()}"
            return f"{chave.capitalize()} não encontrado no seu PC"

    for chave, exe in PROGRAMAS_SIMPLES.items():
        if chave in comando:
            subprocess.Popen(exe)
            return f"Abrindo o {chave.capitalize()}"

    for chave, url in SITES.items():
        if chave in comando:
            webbrowser.open(url)
            return f"Abrindo o {chave.capitalize()}"

    if "desligar" in comando:
        os.system("shutdown /s /t 10")
        return "Desligando o computador em 10 segundos"

    if "reiniciar" in comando:
        os.system("shutdown /r /t 10")
        return "Reiniciando o computador em 10 segundos"

    if "cancelar desligamento" in comando:
        os.system("shutdown /a")
        return "Desligamento cancelado"

    return "Não sei executar esse comando ainda"