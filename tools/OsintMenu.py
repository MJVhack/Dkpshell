from .Colors import * 
import subproces

def OsintMenu():


    def menu():
        print(f"{Colors.MAGENTA}\n=== QG OSINT - Interface Terminal BY SA |Timeline ===")
        print("")
        print(f"{Colors.YELLOW}Lancez en sudo pour installer les modules{Colors.RESET}")
        print("")
        print(f"{Colors.BLUE}[1] Sherlock (Username Search)")
        print(f"[2] Linkook (Social Link OSINT)")
        print(f"[3] Holehe (Email Verification)")
        print(f"[4] Nmap (Scan réseau)")
        print(f"[5] SQLMap (Injection SQL)")
        print(f"[0] Quitter{Colors.RESET}")
        return input(f"{Colors.ORANGE}Choisis une option > {Colors.RESET}")

    def run_sherlock():
        username = input(f"{Colors.CYAN}Entrez le pseudo à chercher : ")
        subprocess.run(f'cd ~/sherlock/sherlock_project && python3 sherlock.py {username}', shell=True)

    def run_linkook():
        username = input(f"{Colors.CYAN}Entrez le pseudo à chercher (Linkook) : ")
        subprocess.run(f'~/.local/share/pipx/venvs/linkook/bin/linkook {username}', shell=True)

    def run_holehe():
        email = input(f"{Colors.CYAN}Entrez l'adresse email : ")
        subprocess.run(f'holehe {email}', shell=True)

    def run_nmap():
        target = input(f"{Colors.CYAN}Entrez l'adresse IP ou domaine : ")
        subprocess.run(f'nmap -sV -T4 -Pn --script vuln {target}', shell=True)

    def run_sqlmap():
        url = input(f"{Colors.CYAN}Entrez l'URL vulnérable (avec paramètre) : ")
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
