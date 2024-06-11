import random

# Modèles de scénarios pour chaque sous-type de personnage
scenarios = {
    'Guerrier': {
        'Archer': [
            "En tant qu'archer agile, vous parcourez les vastes forêts à la recherche de cibles dignes.",
            "Vous êtes un archer redoutable, capable de toucher vos ennemis à des kilomètres de distance.",
            "Votre précision légendaire fait trembler vos ennemis, sachant qu'ils ne peuvent pas échapper à vos flèches mortelles."
        ],
        'Combattant': [
            "Vous êtes un combattant endurci, prêt à affronter n'importe quel ennemi qui se dresse sur votre chemin.",
            "En tant que combattant intrépide, vous cherchez toujours à améliorer vos compétences au combat.",
            "Votre force et votre détermination font de vous un adversaire redoutable sur le champ de bataille."
        ],
        'Chevalier': [
            "En tant que chevalier noble, vous défendez les innocents et combattez pour la justice.",
            "Votre code d'honneur vous guide dans vos actions, vous distinguant comme un véritable protecteur du royaume.",
            "Les gens vous regardent avec admiration et respect, sachant que vous êtes prêt à sacrifier votre vie pour le bien de tous."
        ]
    },
    'Sorcier': {
        'Maitre du Feu': [
            "En tant que maître du feu, vous avez le pouvoir de contrôler les flammes elles-mêmes.",
            "Votre magie de feu est redoutée dans tout le royaume, capable de réduire en cendres vos ennemis les plus puissants.",
            "Les flammes obéissent à votre volonté, ravageant tout sur leur passage et laissant la destruction dans leur sillage."
        ],
        'Maitre de l\'Eau': [
            "En tant que maître de l'eau, vous avez le pouvoir de manipuler les océans et les rivières à votre volonté.",
            "Votre magie de l'eau est inégalée, capable d'éteindre les flammes les plus dévastatrices et de guérir les blessures les plus graves.",
            "Les vagues se plient à votre commandement, obéissant à votre volonté et engloutissant ceux qui osent se mettre en travers de votre chemin."
        ],
        'Maitre de l\'Air': [
            "En tant que maître de l'air, vous avez le pouvoir de contrôler les vents et les tempêtes.",
            "Votre magie de l'air vous permet de voler dans les cieux et de déchaîner des tornades destructrices sur vos ennemis.",
            "Les éléments eux-mêmes vous reconnaissent comme leur maître, pliant à votre volonté et répondant à vos appels."
        ],
        'Maitre de la Terre': [
            "En tant que maître de la terre, vous avez le pouvoir de manipuler les éléments du sol sous vos pieds.",
            "Votre magie de la terre est capable de créer des tremblements de terre dévastateurs et de faire jaillir des montagnes de la terre.",
            "La terre elle-même vous obéit, se soumettant à votre volonté et se dressant comme une armée pour défendre votre cause."
        ]
    },
    'Voleur': {
        'Assassin': [
            "En tant qu'assassin furtif, vous opérez dans les ombres, éliminant vos cibles sans laisser de trace.",
            "Votre agilité et votre discrétion en font un assassin redoutable, capable de neutraliser n'importe quelle cible avec précision.",
            "Les ténèbres sont votre allié, vous permettant de disparaître sans laisser de trace après avoir accompli votre mission mortelle."
        ],
        'Cambrioleur': [
            "En tant que cambrioleur habile, vous avez le don de vous faufiler dans les endroits les mieux gardés et de dérober les trésors les plus précieux.",
            "Votre expertise en matière de crochetage de serrures et de désactivation de pièges vous permet de voler les richesses des plus grands seigneurs sans être détecté.",
            "Les coffres-forts et les trésors cachés s'ouvrent à votre commande, révélant leurs richesses aux yeux avides du voleur."
        ]
    }
}

# Ajout de rôles supplémentaires et de leurs scénarios
scenarios['Barbare'] = {
    'default': [
        "En tant que barbare sauvage, vous cherchez toujours le prochain combat pour prouver votre force et votre courage.",
        "Votre rage incontrôlable fait trembler vos ennemis, sachant qu'ils doivent affronter la fureur d'un véritable barbare.",
        "Les cris de guerre retentissent dans les plaines alors que vous chargez courageusement vers vos ennemis, prêt à tout sacrifier pour la victoire."
    ]
}

scenarios['Mage'] = {
    'default': [
        "En tant que mage puissant, vous étudiez les arts mystiques pour maîtriser les pouvoirs de l'arcane.",
        "Votre connaissance des sorts et des enchantements vous permet de manipuler la réalité elle-même, lançant des sorts dévastateurs sur vos ennemis.",
        "Les éclairs de votre magie illuminent le ciel alors que vous invoquez des tempêtes de feu et de glace pour détruire vos adversaires."
    ]
}

# Fonction pour générer un scénario aléatoire en fonction du type et du sous-type de personnage choisi
def generer_scenario(personnage):
    if personnage['type'] in scenarios:
        if personnage['sous_type'] in scenarios[personnage['type']]:
            return random.choice(scenarios[personnage['type']][personnage['sous_type']])
        else:
            return random.choice(scenarios[personnage['type']]['default'])
    else:
        return "Type de personnage non reconnu."

# Fonction principale du jeu
def jouer_jeu():
    print("Bienvenue dans le jeu de rôle !")
    nom = input("Choisissez un nom pour votre personnage : ")

    print("Choisissez le type de votre personnage :")
    print("1. Guerrier")
    print("2. Sorcier")
    print("3. Voleur")
    print("4. Barbare")
    print("5. Mage")

    choix_type = input("Entrez le numéro correspondant à votre choix : ")

    sous_types = {
        '1': ['Archer', 'Combattant', 'Chevalier'],
        '2': ['Maitre du Feu', 'Maitre de l\'Eau', 'Maitre de l\'Air', 'Maitre de la Terre'],
        '3': ['Assassin', 'Cambrioleur'],
        '4': ['default'],  # Un seul sous-type pour le barbare
        '5': ['default']   # Un seul sous-type pour le mage
    }

    if choix_type in sous_types:
        print(f"Vous avez choisi d'être un {choix_type}.")
        if choix_type != '4' and choix_type != '5':
            print("Choisissez le sous-type de votre personnage :")
            for i, sous_type in enumerate(sous_types[choix_type], start=1):
                print(f"{i}. {sous_type}")

            choix_sous_type = input("Entrez le numéro correspondant à votre choix : ")

            if choix_sous_type.isdigit() and 1 <= int(choix_sous_type) <= len(sous_types[choix_type]):
                personnage = {'nom': nom, 'type': ['Guerrier', 'Sorcier', 'Voleur', 'Barbare', 'Mage'][int(choix_type) - 1], 'sous_type': sous_types[choix_type][int(choix_sous_type) - 1]}
                print(f"{personnage['nom']} est un {personnage['sous_type']} {personnage['type']}.")
                print("Votre aventure commence maintenant :")
                print(generer_scenario(personnage))
            else:
                print("Choix invalide.")
        else:
            personnage = {'nom': nom, 'type': ['Guerrier', 'Sorcier', 'Voleur', 'Barbare', 'Mage'][int(choix_type) - 1], 'sous_type': sous_types[choix_type][0]}
            print(f"{personnage['nom']} est un {personnage['sous_type']} {personnage['type']}.")
            print("Votre aventure commence maintenant :")
            print(generer_scenario(personnage))
    else:
        print("Choix invalide.")

# Appel de la fonction principale
jouer_jeu()
