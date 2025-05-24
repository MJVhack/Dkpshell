def dkpupdate():
  print(f"{Colors.CYAN}[DKP Shell] : Mise à jour en cours...{Colors.RESET}")
  try:
    base_repo_url = "https://raw.githubusercontent.com/MJVhack/Dkpshell/main"
    local_script = os.path.realpath(__file__)
    tools_dir = "tools"

    # 📦 Liste des fichiers à mettre à jour
    files_to_update = [
      "dkpshell.py",  # C’est ton "main"
      "tools/__init__.py",
      "tools/Colors.py",
      "tools/Dkp_msfvenom.py",
      "tools/OsintMenu.py",
      "tools/Raid_Discord.py"# ajoute ici tous tes scripts dans tools/
      ]

      for file in files_to_update:
        url = f"{base_repo_url}/{file}"
        local_path = os.path.join(os.getcwd(), file)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

      print(f"{Colors.YELLOW}→ Téléchargement : {file}{Colors.RESET}")
      urllib.request.urlretrieve(url, local_path)
      print(f"{Colors.GREEN}[✓] Mis à jour : {file}{Colors.RESET}")

      # 📂 Copier vers /usr/local/bin (si applicable)
      bin_path = "/usr/local/bin/dkp"
      if os.path.exists(bin_path) or os.access(os.path.dirname(bin_path), os.W_OK):
        shutil.copy(local_script, bin_path)
        os.chmod(bin_path, 0o755)
        print(f"{Colors.GREEN}[✓] Script copié dans {bin_path}{Colors.RESET}")
      else:
        print(f"{Colors.YELLOW}[!] Pas de permission pour écrire dans {bin_path}. Skipped.{Colors.RESET}")

      # 🔄 Redémarrer le shell automatiquement
      print(f"{Colors.CYAN}[DKP Shell] : Redémarrage du shell...{Colors.RESET}")
      python_exe = sys.executable
      os.execv(python_exe, [python_exe, local_script])

    except Exception as e:
      print(f"{Colors.RED}[Erreur] : La mise à jour a échoué : {e}{Colors.RESET}")
    continue

def check_stability():
  update_url = "https://raw.githubusercontent.com/MJVhack/Dkpshell/refs/heads/main/dkpshell.py"
  try:
      with urllib.request.urlopen(update_url) as response:
      remote_code = response.read().decode("utf-8")

      stable_match = re.search(r'__stable__\s*=\s*(True|False)', remote_code)

      if stable_match:
          is_stable = stable_match.group(1) == "True"
          status = f"{Colors.GREEN}stable{Colors.RESET}" if is_stable else f"{Colors.YELLOW}instable{Colors.RESET}"
          print(f"{Colors.CYAN}[INFO] La version distante est : {status}")
      else:
          print(f"{Colors.RED}[Erreur] Clé '__stable__' non trouvée dans le script distant.{Colors.RESET}")

  except Exception as e:
      print(f"{Colors.RED}[Erreur] Impossible de vérifier la stabilité distante : {e}{Colors.RESET}")

def check_update():
    try:
        url = "https://raw.githubusercontent.com/MJVhack/Dkpshell/main/dkpshell.py"
        with urllib.request.urlopen(url) as response:
            remote_code = response.read().decode("utf-8")
        
        # Cherche la version dans le fichier distant
        match = re.search(r'__version__\s*=\s*"(\d+\.\d+)"', remote_code)
        if match:
            remote_version = match.group(1)
            if remote_version > __version__:
                print(f"{Colors.MAGENTA}[DKP Shell] : Une mise à jour est disponible ({__version__} → {remote_version}){Colors.RESET}")
                print(f"{Colors.CYAN}➜ Lance la commande `dkpupdate` pour mettre à jour{Colors.RESET}")
                check_stability()
    except Exception as e:
        print(f"{Colors.RED}[DKP Shell] : Échec de vérification de mise à jour : {e}\033[0m")

def install_all():
    os.system("pip install -U Pyreadline3")
    print(f"{Colors.GREEN}Pyreadline3 succesful installed")
    os.system("pip install -U discord.py")
    print(f"{Colors.GREEN}Discord.py succesful installed")
    os.system("sudo apt install sherlock")
    print(f"{Colors.GREEN}Sherlock succeful installed{Colors.RESET}")
    os.system("pipx install linkook")
    print(f"{Colors.GREEN}Linkook succeful installed{Colors.RESET}")
    os.system("git clone https://github.com/megadose/holehe.git && cd holehe/ && python3 setup.py install")
    print(f"{Colors.GREEN}Holehe succeful installed{Colors.RESET}")
    os.system("sudo apt install nmap")
    print(f"{Colors.GREEN}Nmap succesful installed{Colors.RESET}")
    os.system("sudo apt install sqlmap")
    print(f"{Colors.GREEN}Sqlmap succesful installed{Colors.RESET}")
    os.system("pip install discord.py")
    print(f"{Colors.GREEN}Discord.py succcesful installed{Colors.RESET}")


