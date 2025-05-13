#!/usr/bin/env python3
import os
import getpass
import shutil

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
BLUE = "\033[94m"
ORANGE = "\033[38;5;208m"

# Fonction pour détecter si root
def is_root():
    return os.geteuid() == 0

# Affichage ASCII Art
ascii_art = fr"""{CYAN}
<!-- .------------------------------------------------------------------------------------------------. -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |     ________    ____  __.__________    _________  ___ ___  ___________.____     .____          | -->
<!-- |     \______ \  |    |/ _|\______   \  /   _____/ /   |   \ \_   _____/|    |    |    |         | -->
<!-- |      |    |  \ |      <   |     ___/  \_____  \ /    ~    \ |    __)_ |    |    |    |         | -->
<!-- |      |    `   \|    |  \  |    |      /        \\    Y    / |        \|    |___ |    |___      | -->
<!-- |     /_______  /|____|__ \ |____|     /_______  / \___|_  / /_______  /|_______ \|_______ \     | -->
<!-- |             \/         \/                    \/        \/          \/         \/        \/     | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- |                                                                                                | -->
<!-- '------------------------------------------------------------------------------------------------' -->
                                           BY DKP
{RESET}
"""
os.system("clear")
print(ascii_art)
print(f"{YELLOW}💡 Tips: Lancer en sudo pour accéder à toutes les fonctionnalités.\n{RESET}")

# État Root
if is_root():
    print(f"{GREEN}[État] : ✅ Rooted{RESET}")
else:
    print(f"{RED}[État] : ❌ No Rooted{RESET}")

# Texte de prompt
custom_prompt = input("\n[?] Texte pour le prompt du shell (ex: DKP{㉿ ) (ajoute un espace à la fin) : ")
print("")
# Ajouter au PATH
print(f"{YELLOW}💡 Tips: Redire 'yes' updatera la copie du script se trouvant dans le /bin")
add_to_path = input(f"{YELLOW}\n[?] Voulez-vous ajouter ce script/update à /usr/local/bin (nécessite sudo) ? (yes/no) : ").lower()

if add_to_path == "yes":
    script_path = os.path.realpath(__file__)
    target_path = "/usr/local/bin/dkpshell"
    try:
        shutil.copy(script_path, target_path)
        os.chmod(target_path, 0o755)
        print(f"{GREEN}[+] Script copié dans {target_path} ✅{RESET}")
    except PermissionError:
        print(f"{ORANGE}[!] Permission refusée. Relancez en sudo pour l'ajouter au PATH.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Erreur lors de la copie : {e}{RESET}")

# Déclenchement du shell
if is_root():
	start = input(f"{RED}\nTapez 'start' pour lancer le DKP Shell : {RESET}").strip().lower()
else:
	start = input(f"{MAGENTA}\nTapez 'start' pour lancer le DKP Shell : {RESET}").strip().lower()

# Prompt shell personnalisé
def shell():
    user = getpass.getuser()
    root_state = "{ROOTED}" if is_root() else "{USER}"
    try:
        while True:
            print("")
            shell_input = input(f"{BLUE}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
            print(f"{YELLOW}")
            os.system(shell_input)
    except KeyboardInterrupt:
        print(f"{GREEN}\n[DKP Shell]: Fermeture.{RESET}")
        exit()

if start == "start":
    shell()
else:
    print(f"{CYAN}[Script]: Fin du script.{RESET}")
