import subprocess
import os
import webbrowser

def executar(comando: str) -> str:
    comando = comando.lower().strip()

    # Navegadores
    if "chrome" in comando:
        subprocess.Popen("chrome.exe")
        return "Abrindo o Chrome"

    if "brave" in comando:
        subprocess.Popen("brave.exe")
        return "Abrindo o Brave"

    # Programas
    if "bloco de notas" in comando:
        subprocess.Popen("notepad.exe")
        return "Abrindo o Bloco de Notas"

    if "calculadora" in comando:
        subprocess.Popen("calc.exe")
        return "Abrindo a calculadora"

    if "spotify" in comando:
        # Pega o nome do usuário automaticamente
        usuario = os.getenv("USERNAME")
        caminho = f"C:\\Users\\{usuario}\\AppData\\Roaming\\Spotify\\Spotify.exe"
        if os.path.exists(caminho):
            subprocess.Popen(caminho)
            return "Abrindo o Spotify"
        else:
            return "Spotify não encontrado no seu PC"

    # Sites
    if "youtube" in comando:
        webbrowser.open("https://youtube.com")
        return "Abrindo o YouTube"

    if "google" in comando:
        webbrowser.open("https://google.com")
        return "Abrindo o Google"
    
    if "sigaa" in comando:
        webbrowser.open("https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do;jsessionid=5A4D7E348DEB496483F90E553E9CB131.appdocker3-inst2")
        return "Abrindo o Sigaa"

    return "Não sei executar esse comando ainda"