#!/usr/bin/env python3
cmd_for_config = "dkpconfig"
import os
import getpass
import shutil
import urllib.request
try:
    import readline
except ImportError:
    import pyreadline3 as readline

import atexit
import sys
import rlcompleter
import subprocess
import re
try:
    import discord
    from discord.ext import commands
except ImportError:
    print(f"Discord.py is not installed, use {cmd_for_config} -installall")
import asyncio
from tools import 


__version__ = "4.4"
__stable__ = False

prompt_color = BLUE

def check_stability():
    update_url = "https://raw.githubusercontent.com/MJVhack/MJVhack/refs/heads/main/dkpshell.py"

    try:
        with urllib.request.urlopen(update_url) as response:
            remote_code = response.read().decode("utf-8")

        stable_match = re.search(r'__stable__\s*=\s*(True|False)', remote_code)

        if stable_match:
            is_stable = stable_match.group(1) == "True"
            status = f"{GREEN}stable{RESET}" if is_stable else f"{YELLOW}instable{RESET}"
            print(f"{CYAN}[INFO] La version distante est : {status}")
        else:
            print(f"{RED}[Erreur] Clé '__stable__' non trouvée dans le script distant.{RESET}")

    except Exception as e:
        print(f"{RED}[Erreur] Impossible de vérifier la stabilité distante : {e}{RESET}")


def check_update():
    try:
        url = "https://raw.githubusercontent.com/MJVhack/MJVhack/main/dkpshell.py"
        with urllib.request.urlopen(url) as response:
            remote_code = response.read().decode("utf-8")
        
        # Cherche la version dans le fichier distant
        match = re.search(r'__version__\s*=\s*"(\d+\.\d+)"', remote_code)
        if match:
            remote_version = match.group(1)
            if remote_version > __version__:
                print(f"{MAGENTA}[DKP Shell] : Une mise à jour est disponible ({__version__} → {remote_version}){RESET}")
                print(f"{CYAN}➜ Lance la commande `dkpupdate` pour mettre à jour{RESET}")
                check_stability()
    except Exception as e:
        print(f"{RED}[DKP Shell] : Échec de vérification de mise à jour : {e}\033[0m")
        

histfile = os.path.expanduser("~/.dkpshell_history")
readline.read_history_file(histfile) if os.path.exists(histfile) else None
atexit.register(readline.write_history_file, histfile)



dkp_commands = [
    f"{cmd_for_config} -color red"
    f"{cmd_for_config} -color green"
    f"{cmd_for_config} -color yellow"
    f"{cmd_for_config} -color cyan"
    f"{cmd_for_config} -color magenta"
    f"{cmd_for_config} -color white"
    f"{cmd_for_config} -color bold"
    f"{cmd_for_config} -color blue"
    f"{cmd_for_config} -color orange"
    f"{cmd_for_config.replace('config', 'update')}"
    f"{cmd_for_config}"
    f"{cmd_for_config} --help"
    f"{cmd_for_config} -restartshell"
    f"{cmd_for_config} -exit"
]


readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set show-all-if-ambiguous off")
readline.parse_and_bind("set completion-query-items 100")
readline.set_completer_delims(" \t\n")

readline.set_completion_display_matches_hook(
    lambda substitution, matches, longest_match_length:
        print("\n" + "\n".join(matches))
)

def completer(text, state):
    # Ligne complète tapée jusqu’à maintenant
    current_line = readline.get_line_buffer()

    # Suggestions contenant le texte n'importe où
    matches = [cmd for cmd in dkp_commands if text in cmd]

    if state < len(matches):
        # Supprime la ligne tapée et la remplace par la suggestion entière
        readline.delete_text(0, len(current_line))
        readline.insert_text(matches[state])
        readline.redisplay()
        return matches[state]
    else:
        return None

readline.set_completer(completer)

def color_config():
    print(f'''{RED}RED 
{GREEN}GREEN
{YELLOW}YELLOW 
{CYAN}CYAN 
{MAGENTA}MAGENTA 
{RESET}RESET 
{BOLD}BOLD 
{BLUE}BLUE 
{ORANGE}ORANGE ''')
    print("mettait EXACTEMENT le nom des variables")
    A_color = input("")
    B_color = input("")
    C_color = input("")
    D_color = input("")
    E_color = input("")
    shell_input1 = input(f"{A_color}┌──({B_color}{custom_prompt}{C_color}{root_state}{D_color}{user})-[{E_color}~]\n└─[ {RESET}")

# Fonction pour détecter si root
def is_root():
    return os.geteuid() == 0


def install_all():
    os.system("pip install -U Pyreadline3")
    print(f"{GREEN}Pyreadline3 succesful installed")
    os.system("pip install -U discord.py")
    print(f"{GREEN}Discord.py succesful installed")
    os.system("sudo apt install sherlock")
    print(f"{GREEN}Sherlock succeful installed{RESET}")
    os.system("pipx install linkook")
    print(f"{GREEN}Linkook succeful installed{RESET}")
    os.system("git clone https://github.com/megadose/holehe.git && cd holehe/ && python3 setup.py install")
    print(f"{GREEN}Holehe succeful installed{RESET}")
    os.system("sudo apt install nmap")
    print(f"{GREEN}Nmap succesful installed{RESET}")
    os.system("sudo apt install sqlmap")
    print(f"{GREEN}Sqlmap succesful installed{RESET}")
    os.system("pip install discord.py")
    print(f"{GREEN}Discord.py succcesful installed{RESET}")

updlist = f"""{YELLOW}NEW ADD{BLUE}
--------------3.0--------------------
[+] add '{cmd_for_config} -installall', '{cmd_for_config.replace("config", "tool")} -e RaidDiscordBD', '{cmd_for_config} -updlist'
    [*]{cmd_for_config} -installall: Avant pour installer les modules, il fallait lancer Osint Menu, plus maintenant. Desormais meme les modules pour {MAGENTA}[dkpshell.py]{BLUE} sont installer et update via {cmd_for_config} -installall
    [*]{cmd_for_config.replace("config", "tool")} -e RaidDiscordBD: Permet de lancer le nnouveau module 'raid_discord' V1 avec IMPERATIVEMENT un token de bot DISCORD
    [*]{cmd_for_config} -updlist: réaffiche ce que vous lisez maintenant
[+]add 'The Update list'
    [*]The Update List: Ce que vous lisez maintenant
[!] point:
    [*]'{cmd_for_config} -color config' est toujours en maintenance et pour un bon moment
    [*]'Le tab est toujours bugué et va être supprimer dans la nouvelle mise a jour
    [*]L'Update List sera reset que tout les 2 update MAJEURES (2.0 -> 2.1: non majeure; 2.0 -> 3.0: majeure) entre temps seulement des choses seront RAJOUTER a l'Update List
    [*]Le bug des commandes hors dkp qui crash est réglé (retour a une version antérieur)
-----------------3.5--------------
[!]bugs:
    [*]Bug de la commande '{cmd_for_config.replace("config", "tool")} -e RaidDiscordBD', un enfer.
----------3.8----------------
[!]bugs:
    [*]bug a cause de gemini, très difficile
------------3.9----------
[!]bugs
     [*]Resolu le bug des variables dans raid_discord
----------4.1------------
[+]add 'stable' and '{cmd_for_config} -stable' and '{cmd_for_config} -version'
    [*]Permet de savoir si la prochaine update est vraiment utilisable (sans bug ou seulement d'affichage) nou instable (surement non verifié ou bugué)
    [*]'{cmd_for_config} -stable' permet de savoir si la prochaine version (si y'en a une disponible) est stable
    [*]'{cmd_for_config} -version' affiche votre version actuelle
    """
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
                                           version : {__version__}

{updlist}
{RESET}
"""
os.system("clear")
print(ascii_art)
check_update()
print("")
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




def shell():
    global prompt_color
    user = getpass.getuser()
    root_state = "{ROOTED}" if is_root() else "{USER}"
    try:
        while True:
            print("")
            shell_input = input(f"{prompt_color}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
            print("")
            if shell_input in [f"{cmd_for_config}", f"{cmd_for_config} --help"]:
                print(f"{MAGENTA}DKPSHELL help")
                print("")
                print(f"{MAGENTA}{cmd_for_config} -colorlist {RESET}")
                print(f"{MAGENTA}{cmd_for_config.replace('config', 'update')}{RESET}")
                print(f"{MAGENTA}{cmd_for_config.replace('config', 'tool')}{RESET}")
                print(f"{MAGENTA}{cmd_for_config} -restartshell")
                print(f"{MAGENTA}{cmd_for_config} -exit")
                print(f"{MAGENTA}{cmd_for_config} -updlist")
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
                 prompt_color = RED
                 continue
            elif shell_input in [f"{cmd_for_config} -color green"]:
                 prompt_color = GREEN
                 continue
            elif shell_input in [f"{cmd_for_config} -color yellow"]:
                 prompt_color = YELLOW
                 continue
            elif shell_input in [f"{cmd_for_config} -color cyan"]:
                 prompt_color = CYAN
                 continue
            elif shell_input in [f"{cmd_for_config} -color magenta"]:
                 prompt_color = MAGENTA
                 continue
            elif shell_input in [f"{cmd_for_config} -color white"]:
                 prompt_color = WHITE
                 continue
            elif shell_input in [f"{cmd_for_config} -color bold"]:
                 prompt_color = BOLD
                 continue
            elif shell_input in [f"{cmd_for_config} -color blue"]:
                 prompt_color = BLUE
                 continue
            elif shell_input in [f"{cmd_for_config} -color orange"]:
                 prompt_color = ORANGE
                 continue
            elif shell_input in [f"{cmd_for_config.replace("config", "tool")} -e RaidDiscordBD"]:
                raid_discord()

            elif shell_input in [f"{cmd_for_config} -installall"]:
                install_all()
                
                
            elif shell_input in [f"{cmd_for_config} -restartshell"]:
                print(f"{YELLOW}[DKP Shell] : Redémarrage du shell...{RESET}")
                python_exe = sys.executable  # Chemin vers l'interpréteur Python
                script_path = os.path.realpath(__file__)  # Chemin vers le script courant
                os.execv(python_exe, [python_exe, script_path])  # Relance le script

            
            elif shell_input in [f"{cmd_for_config} -exit"]:
                print(f"{GREEN}[DKP Shell] : Fermeture{RESET}")
                sys.exit(0)

            elif shell_input in [f"{cmd_for_config.replace('config', 'tool')} --help",f"{cmd_for_config.replace('config', 'tool')}" ]:
                print(f"{MAGENTA}LIST")
                print("")
                print("[OSINT MENU]: dkptool -e OsintMenu")
                print("[RAID DISCORD BY BOT DISCORD]: dkptool -e RaidDiscordBD")
                print("")

            elif shell_input == f"{cmd_for_config.replace('config', 'tool')} -e MenuOsint":
                OsintMenu()

            elif shell_input == f"{cmd_for_config} -color config":
                print(f"{ORANGE}Cette option a été momontanément désactiver.")

            elif shell_input == f"{cmd_for_config} -updlist":
                print(updlist)

            elif shell_input == f"{cmd_for_config} -version":
                print(__version__)

            elif shell_input == f"{cmd_for_config} -stable":
                check_stability()
                
            elif shell_input == f"{cmd_for_config.replace('config', 'update')}":
                print(f"{CYAN}[DKP Shell] : Mise à jour en cours...{RESET}")
                try:
                    # Variables
                    update_url = "https://raw.githubusercontent.com/MJVhack/MJVhack/refs/heads/main/dkpshell.py"  # 🔁 Modifie ici
                    local_script = os.path.realpath(__file__)
                    bin_path = "/usr/local/bin/dkp"  # ou '~/bin/dkp' selon où tu le copies

                    # Télécharger nouvelle version
                    urllib.request.urlretrieve(update_url, local_script)
                    print(f"{GREEN}[✓] Script local mis à jour : {local_script}{RESET}")

                    # Copier vers /usr/local/bin (accès global)
                    if os.path.exists(bin_path) or os.access(os.path.dirname(bin_path), os.W_OK):
                        shutil.copy(local_script, bin_path)
                        os.chmod(bin_path, 0o755)
                        print(f"{GREEN}[✓] Script copié dans {bin_path}{RESET}")
                    else:
                        print(f"{YELLOW}[!] Pas de permission pour écrire dans {bin_path}. Skipped.{RESET}")

                    # Redémarrer le shell automatiquement
                    print(f"{CYAN}[DKP Shell] : Redémarrage du shell...{RESET}")
                    python_exe = sys.executable
                    os.execv(python_exe, [python_exe, local_script])
                    
                except Exception as e:
                    print(f"{RED}[Erreur] : La mise à jour a échoué : {e}{RESET}")
                continue

                

            else:
                print(f"{RED}Commande non reconnu en tant que commande {MAGENTA}[DKP]")
                print(f"{YELLOW}")
                os.system(shell_input)
            continue



    except KeyboardInterrupt:
        print(f"{GREEN}\n[DKP Shell]: Fermeture.{RESET}")
        exit()

if start == "start":
    shell()
else:
    print(f"{CYAN}[Script]: Fin du script.{RESET}")
