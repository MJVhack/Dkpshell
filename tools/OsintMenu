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
