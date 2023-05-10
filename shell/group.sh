#!/bin/bash
# Créer les sous-dossiers "groupe1", "groupe2", ..., "groupe6"
cd /var/tmp/dalles_detection
for i in {1..6} 
do 
mkdir -p groupe$i 
done
# Compter le nombre total de fichiers dans le dossier courant
num_files=$(ls job*.sh| wc -l)
# Calculer le nombre de fichiers à copier dans chaque groupe
files_per_group=$(expr $num_files / 6)
# Copier les fichiers dans les sous-dossiers
for i in {1..5} 
do
    # Copier les fichiers dans le sous-dossier courant
    cp $(ls job*.sh| head -n $files_per_group) groupe$i/
    
    # Supprimer les fichiers déjà copiés
    rm $(ls job*.sh| head -n $files_per_group) 
done

cp $(ls job*.sh) groupe6/
    
 # Supprimer les fichiers déjà copiés
rm $(ls job*.sh) 