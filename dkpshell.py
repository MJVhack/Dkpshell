#!/usr/bin/env python3
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



__version__ = "3.3"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
BLUE = "\033[94m"
ORANGE = "\033[38;5;208m"

prompt_color = str(BLUE)

def raid_discord():
    # INPUT UTILISATEUR
    token = input(f"{YELLOW}🔑 Entrez le token du bot Discord: ")
    noms_renommage_str = input("✏️ Entrez les noms pour renommer les salons (séparés par des virgules): ")
    noms_renommage = [n.strip() for n in noms_renommage_str.split(",") if n.strip()]

    nom_nouveaux_salons = input("📛 Nom des nouveaux salons à créer: ").strip()
    nombre_de_salons = int(input(f"🔢 Combien de nouveaux salons créer ? {RESET}"))

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{GREEN}✅ Connecté en tant que {bot.user}")
    
        guild_id_input = int(input(f"{BLUE}🆔 Entrez l'ID du serveur cible : "))
        guild = bot.get_guild(guild_id_input)
    
        if guild is None:
            print(f"{RED}❌ Le bot n'est pas dans ce serveur ou l'ID est invalide.")
            await bot.close()
            return

        print(f"{MAGENTA}🔗 Raid en cours sur le serveur: {guild.name} ({guild.id})")

        salons_texte = [c for c in guild.text_channels]
        ids = [c.id for c in salons_texte]
        print(f"{CYAN}🧾 Salons existants:", ids)

    # Renommage des salons
        for i, salon in enumerate(salons_texte):
            if i < len(noms_renommage):
                nouveau_nom = noms_renommage[i]
            else:
                nouveau_nom = f"{nom_nouveaux_salons}-{i}"
            try:
                await salon.edit(name=nouveau_nom)
                print(f"{GREEN}🔁 Salon renommé: {salon.name} -> {nouveau_nom}")
            except Exception as e:
                print(f"{ORANGE}⚠️ Erreur lors du renommage de {salon.name}: {e}")

    # Création de nouveaux salons
        for i in range(nombre_de_salons):
            try:
                await guild.create_text_channel(f"{nom_nouveaux_salons}-{i}")
                print(f"➕ Salon créé: {nom_nouveaux_salons}-{i}")
            except Exception as e:
                print(f"{RED}⚠️ Erreur création salon: {e}")

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
    except Exception as e:
        print(f"{RED}[DKP Shell] : Échec de vérification de mise à jour : {e}\033[0m")

histfile = os.path.expanduser("~/.dkpshell_history")
readline.read_history_file(histfile) if os.path.exists(histfile) else None
atexit.register(readline.write_history_file, histfile)

cmd_for_config = "dkpconfig"

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

def OsintMenu():


    def menu():
        print(f"{MAGENTA}\n=== QG OSINT - Interface Terminal BY SA |Timeline ===")
        print("")
        print(f"{YELLOW}Lancez en sudo pour installer les modules{RESET}")
        print("")
        print(f"{BLUE}[1] Sherlock (Username Search)")
        print(f"[2] Linkook (Social Link OSINT)")
        print(f"[3] Holehe (Email Verification)")
        print(f"[4] Nmap (Scan réseau)")
        print(f"[5] SQLMap (Injection SQL)")
        print(f"[0] Quitter{RESET}")
        return input(f"{ORANGE}Choisis une option > {RESET}")

    def run_sherlock():
        username = input(f"{CYAN}Entrez le pseudo à chercher : ")
        subprocess.run(f'cd ~/sherlock/sherlock_project && python3 sherlock.py {username}', shell=True)

    def run_linkook():
        username = input(f"{CYAN}Entrez le pseudo à chercher (Linkook) : ")
        subprocess.run(f'~/.local/share/pipx/venvs/linkook/bin/linkook {username}', shell=True)

    def run_holehe():
        email = input(f"{CYAN}Entrez l'adresse email : ")
        subprocess.run(f'holehe {email}', shell=True)

    def run_nmap():
        target = input(f"{CYAN}Entrez l'adresse IP ou domaine : ")
        subprocess.run(f'nmap -sV -T4 -Pn --script vuln {target}', shell=True)

    def run_sqlmap():
        url = input(f"{CYAN}Entrez l'URL vulnérable (avec paramètre) : ")
        subprocess.run(f'sqlmap -u "{url}" --batch --level=3 --risk=2', shell=True)

# Boucle principale
    while True:
        choice = menu()
        if choice == "1":
            run_sherlock()
        elif choice == "2":
            run_linkook()
        elif choice == "3":
            run_holehe()
        elif choice == "4":
            run_nmap()
        elif choice == "5":
            run_sqlmap()
        elif choice == "0":
            print("Fermeture du QG OSINT. Timeline By SA")
            break
        else:
            print("Choix invalide.")

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
[+] add '{cmd_for_config} -installall', '{cmd_for_config.replace("config", "tool")} -e RaidDiscordBD', '{cmd_for_config} -updlist'
    [*]{cmd_for_config} -installall: Avant pour installer les modules, il fallait lancer Osint Menu, plus maintenant. Desormais meme les modules pour {MAGENTA}[dkpshell.py]{BLUE} sont installer et update via {cmd_for_config} -installall
    [*]{cmd_for_config.replace("config", tool)} -e RaidDiscordBD: Permet de lancer le nnouveau module 'raid_discord' V1 avec IMPERATIVEMENT un token de bot DISCORD
    [*]{cmd_for_config} -updlist: réaffiche ce que vous lisez maintenant
[+]add 'The Update list'
    [*]The Update List: Ce que vous lisez maintenant
[!] point:
    [*]'{cmd_for_config} -color config' est toujours en maintenance et pour un bon moment
    [*]'Le tab est toujours bugué et va être supprimer dans la nouvelle mise a jour
    [*]L'Update List sera reset que tout les 2 update MAJEURES (2.0 -> 2.1: non majeure; 2.0 -> 3.0: majeure) entre temps seulement des choses seront RAJOUTER a l'Update List"""
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
                print(f"{MAGENTA}{cmd_for_config} -colorlist {RESET}")
                print(f"{MAGENTA}{cmd_for_config.replace('config', 'update')}{RESET}")
                print(f"{MAGENTA}{cmd_for_config.replace('config', 'tool')}{RESET}")
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
                 prompt_color = RESET
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
            elif shell_input in [f"{cmd_for_config.replace("config", "tool")} -e RaidDiscordBT"]:
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
                print("Cette option a été momontanément désactiver.")

            elif shell_input == f"{cmd_for_config} -updlist":
                print(updlist)
                
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
                shell_input = input(f"{prompt_color}┌──({custom_prompt}{root_state}{user})-[~]\n└─[ {RESET}")
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
