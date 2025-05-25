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
from tools import *


__version__ = "5.4"
__stable__ = True

prompt_color = Colors.BLUE

histfile = os.path.expanduser("~/.dkpshell_history")
readline.read_history_file(histfile) if os.path.exists(histfile) else None
atexit.register(readline.write_history_file, histfile)

# Fonction pour détecter si root
def is_root():
    return os.geteuid() == 0

updlist = f"""{Colors.YELLOW}NEW ADD{Colors.BLUE}
----------5.1------------
[+]add '{cmd_for_config.replace('config', 'tool')} -e DkpMsfvenom'
    [*]outil puissant utilisant METASPLOIT pour créer des payloads
    """
# Affichage ASCII Art
ascii_art = fr"""{Colors.CYAN}
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
{Colors.RESET}
"""
os.system("clear")
print(ascii_art)
check_update()
print("")
print(f"{Colors.YELLOW}💡 Tips: Lancer en sudo pour accéder à toutes les fonctionnalités.\n{Colors.RESET}")

# État Root
if is_root():
    print(f"{Colors.GREEN}[État] : ✅ Rooted{Colors.RESET}")
else:
    print(f"{Colors.RED}[État] : ❌ No Rooted{Colors.RESET}")

# Texte de prompt
custom_prompt = input("\n[?] Texte pour le prompt du shell (ex: DKP{㉿ ) (ajoute un espace à la fin) : ")
print("")
# Ajouter au PATH
print(f"{Colors.YELLOW}💡 Tips: Redire 'yes' updatera la copie du script se trouvant dans le /bin")
add_to_path = input(f"{Colors.YELLOW}\n[?] Voulez-vous ajouter ce script/update à /usr/local/bin (nécessite sudo) ? (yes/no) : ").lower()

if add_to_path == "yes":
    script_path = os.path.realpath(__file__)
    target_path = "/usr/local/bin/dkpshell"
    try:
        shutil.copy(script_path, target_path)
        os.chmod(target_path, 0o755)
        print(f"{Colors.GREEN}[+] Script copié dans {target_path} ✅{Colors.RESET}")
    except PermissionError:
        print(f"{Colors.ORANGE}[!] Permission refusée. Relancez en sudo pour l'ajouter au PATH.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Erreur lors de la copie : {e}{Colors.RESET}")


# Déclenchement du shell
if is_root():
        start = input(f"{Colors.RED}\nTapez 'start' pour lancer le DKP Shell : {Colors.RESET}").strip().lower()
else:
        start = input(f"{Colors.MAGENTA}\nTapez 'start' pour lancer le DKP Shell : {Colors.RESET}").strip().lower()

def shell():
    global prompt_color
    user = getpass.getuser()
    root_state = "{ROOTED}" if is_root() else "{USER}"
    try:
        while True:
            print("")
            shell_input = input(f"{prompt_color}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {Colors.RESET}")
            print("")
            if shell_input in [f"{cmd_for_config}", f"{cmd_for_config} --help"]:
                help_list()
                continue
            elif shell_input in [f"{cmd_for_config} -colorlist"]:
                 print(color_list)
                 continue
            elif shell_input in [f"{cmd_for_config} -color red"]:
                 prompt_color = Colors.RED
                 continue
            elif shell_input in [f"{cmd_for_config} -color green"]:
                 prompt_color = Colors.GREEN
                 continue
            elif shell_input in [f"{cmd_for_config} -color yellow"]:
                 prompt_color = Colors.YELLOW
                 continue
            elif shell_input in [f"{cmd_for_config} -color cyan"]:
                 prompt_color = Colors.CYAN
                 continue
            elif shell_input in [f"{cmd_for_config} -color magenta"]:
                 prompt_color = Colors.MAGENTA
                 continue
            elif shell_input in [f"{cmd_for_config} -color white"]:
                 prompt_color = Colors.WHITE
                 continue
            elif shell_input in [f"{cmd_for_config} -color bold"]:
                 prompt_color = Colors.BOLD
                 continue
            elif shell_input in [f"{cmd_for_config} -color blue"]:
                 prompt_color = Colors.BLUE
                 continue
            elif shell_input in [f"{cmd_for_config} -color orange"]:
                 prompt_color = Colors.ORANGE
                 continue
            elif shell_input in [f"{cmd_for_config.replace("config", "tool")} -e RaidDiscordBD"]:
                raid_discord()

            elif shell_input in [f"{cmd_for_config} -installall"]:
                install_all()
                
            elif shell_input in [f"{cmd_for_config.replace('config', 'tool')} -e DkpMsfvenom"]:
                gen_msfvenom()
            
            elif shell_input in [f"{cmd_for_config} -restartshell"]:
                restart_shell()
            
            elif shell_input in [f"{cmd_for_config} -exit"]:
                print(f"{Colors.GREEN}[DKP Shell] : Fermeture{Colors.RESET}")
                sys.exit(0)

            elif shell_input in [f"{cmd_for_config.replace('config', 'tool')} --help",f"{cmd_for_config.replace('config', 'tool')}" ]:
                print(f"{Colors.MAGENTA}LIST")
                print("")
                print("[OSINT MENU]: dkptool -e OsintMenu")
                print("[RAID DISCORD BY BOT DISCORD]: dkptool -e RaidDiscordBD")
                print("[Dkp Msfvenom]: dkptool -e DkpMsfvenom")
                print(f"{Colors.RESET}")

            elif shell_input == f"{cmd_for_config.replace('config', 'tool')} -e OsintMenu":
                OsintMenu()

            elif shell_input == f"{cmd_for_config} -color config":
                print(f"{Colors.ORANGE}Cette option a été momontanément désactiver.")

            elif shell_input == f"{cmd_for_config} -updlist":
                print(updlist)

            elif shell_input == f"{cmd_for_config} -version":
                print(__version__)

            elif shell_input == f"{cmd_for_config} -stable":
                check_stability()
                
            elif shell_input == f"{cmd_for_config.replace('config', 'update')}":
                dkpupdate()
            else:
                print(f"{Colors.RED}Commande non reconnu en tant que commande {Colors.MAGENTA}[DKP]")
                print(f"{Colors.YELLOW}")
                os.system(shell_input)
            continue



    except KeyboardInterrupt:
        print(f"{Colors.GREEN}\n[DKP Shell]: Fermeture.{Colors.RESET}")
        exit()

if start == "start":
    shell()
else:
    print(f"{Colors.CYAN}[Script]: Fin du script.{Colors.RESET}")
