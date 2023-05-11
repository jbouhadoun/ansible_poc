#!/bin/bash
# Chemin du dossier contenant les scripts
#dossier_scripts="/var/tmp/dalles_detection/group"
# Fichier pour stocker les temps d'exécution
#fichier_temps="/var/tmp/dalles_detection_temps_group_.log"
# Parcourir tous les fichiers .sh dans le dossier
for script in $dossier_scripts/*.sh; 
    do
    # Récupérer le nom du script sans l'extension
    nom_script=$(basename "$script" .sh)
    # Lancer le script et mesurer le temps d'exécution
    temps=$( { time bash "$script"; } 2>&1 | grep "real" | awk '{print $2}' ) 
    echo "Script : $nom_script - Temps d'exécution : $temps" >> "$fichier_temps" 
done