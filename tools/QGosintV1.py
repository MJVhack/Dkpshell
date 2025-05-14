import subprocess
import os

def menu():
    print("\n=== QG OSINT - Interface Terminal BY SA |Timeline ===")
    print("[1] Sherlock (Username Search)")
    print("[2] Linkook (Social Link OSINT)")
    print("[3] Holehe (Email Verification)")
    print("[4] Nmap (Scan réseau)")
    print("[5] SQLMap (Injection SQL)")
    print("[0] Quitter")
    return input("Choisis une option > ")

def run_sherlock():
    username = input("Entrez le pseudo à chercher : ")
    subprocess.run(f'wsl bash -c "cd ~/sherlock/sherlock_project && python3 sherlock.py {username}"', shell=True)

def run_linkook():
    username = input("Entrez le pseudo à chercher (Linkook) : ")
    subprocess.run(f'wsl bash -c "~/.local/share/pipx/venvs/linkook/bin/linkook {username}"', shell=True)

def run_holehe():
    email = input("Entrez l'adresse email : ")
    subprocess.run(f'wsl bash -c "holehe {email}"', shell=True)

def run_nmap():
    target = input("Entrez l'adresse IP ou domaine : ")
    subprocess.run(f'wsl bash -c "nmap -sV -T4 -Pn --script vuln {target}"', shell=True)

def run_sqlmap():
    url = input("Entrez l'URL vulnérable (avec paramètre) : ")
    subprocess.run(f'wsl bash -c "sqlmap -u \\"{url}\\" --batch --level=3 --risk=2"', shell=True)

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
