#!/usr/bin/python3
"""
Ce module génère des invitations personnalisées à partir d'un modèle et
d'une liste de participants. Les fichiers d'invitation sont nommés de
manière séquentielle et sont générés dans le répertoire courant.
"""

def generate_invitations(template, attendees):
    import os

    # Vérifier les types d'entrées
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Vérifier si le template est vide
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Vérifier si la liste des participants est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Processus de chaque participant
    for idx, attendee in enumerate(attendees, 1):
        content = template
        for key, value in attendee.items():
            placeholder = "{" + key + "}"
            content = content.replace(placeholder,
                                      str(value) if value else "N/A")

        # Remplacer les placeholders manquants par "N/A"
        content = content.replace("{name}",
                                  "N/A").replace("{event_title}", "N/A") \
                         .replace("{event_date}",
                                  "N/A").replace("{event_location}", "N/A")

        # Générer les fichiers de sortie
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(content)
