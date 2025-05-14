#!/usr/bin/env python3
import os
import getpass
import shutil
import urllib.request
import readline
import atexit
import sys


histfile = os.path.expanduser("~/.dkpshell_history")
readline.read_history_file(histfile) if os.path.exists(histfile) else None
atexit.register(readline.write_history_file, histfile)

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
cmd_for_config = "dkpconfig"
# Prompt shell personnalisé
def shell():
    user = getpass.getuser()
    root_state = "{ROOTED}" if is_root() else "{USER}"
    try:
        while True:
            print("")
            shell_input = input(f"{BLUE}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
            if shell_input in [f"{cmd_for_config}", f"{cmd_for_config} --help"]:
                print(f"{MAGENTA}DKPSHELL help")
                print("")
                print(f"{MAGENTA} {cmd_for_config} -colorlist {RESET}")
                print(f"{MAGENTA}{cmd_for_config.replace('config', 'update')}{RESET}")
                continue
            elif shell_input in [f"{cmd_for_config} -colorlist"]:
                 print(f'''{MAGENTA}DKPSHELL color
                 
                 RED = {cmd_for_config} -color red
                 GREEN = {cmd_for_config} -color green
                 YELLOW = {cmd_for_config} -color yellow
                 CYAN = {cmd_for_config} -color cyan
                 MAGENTA = {cmd_for_config} -color magenta
                 WHITE = {cmd_for_config} -color white
                 BOLD = {cmd_for_config} -color bold
                 BLUE = {cmd_for_config} -color blue
                 ORANGE = {cmd_for_config} -color orange''')
                 continue
            elif shell_input in [f"{cmd_for_config} -color red"]:
                 shell_input = input(f"{RED}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color green"]:
                 shell_input = input(f"{GREEN}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color yellow"]:
                 shell_input = input(f"{YELLOW}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color cyan"]:
                 shell_input = input(f"{CYAN}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color magenta"]:
                 shell_input = input(f"{MAGENTA}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color white"]:
                 shell_input = input(f"{RESET}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color bold"]:
                 shell_input = input(f"{BOLD}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color blue"]:
                 shell_input = input(f"{BLUE}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input in [f"{cmd_for_config} -color orange"]:
                 shell_input = input(f"{ORANGE}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
                 continue
            elif shell_input == f"{cmd_for_config.replace('config', 'update')}":
                print(f"{CYAN}[DKP Shell] : Mise à jour du script en cours...{RESET}")
                try:
                    # Remplace cette URL par celle de TON script brut
                    url = "https://raw.githubusercontent.com/MJVhack/MJVhack/refs/heads/main/dkpshell.py"
                    local_filename = os.path.realpath(__file__)
        

                    urllib.request.urlretrieve(url, local_filename)
        
                    print(f"{GREEN}[DKP Shell] : Script mis à jour avec succès !{RESET}")
                    print(f"{YELLOW}[DKP Shell] : Redémarre le script pour appliquer les changements.{RESET}")
                    sys.exit(0)
                
                except Exception as e:
                    print(f"{RED}[Erreur] : La mise à jour a échoué : {e}{RESET}")
                sys.exit(0)
                

            else:
                 print(f"{RED}Commande non reconnu")
            continue

            print(f"{YELLOW}")
            os.system(shell_input)


    except KeyboardInterrupt:
        print(f"{GREEN}\n[DKP Shell]: Fermeture.{RESET}")
        exit()

if start == "start":
    shell()
else:
    print(f"{CYAN}[Script]: Fin du script.{RESET}")
