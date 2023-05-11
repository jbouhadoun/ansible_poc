#!/bin/bash
# Limite de consommation de GPU en pourcentage
LIMIT=50
# Chemin du fichier de sortie
OUTPUT_FILE="/var/tmp/monitoring_gpu.txt" 
while true; 
do
    # Récupération de la consommation de la GPU et du nombre de processus en cours
    GPU_USAGE=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits) 
    PROCESS_COUNT=$(nvidia-smi --query-compute-apps=pid --format=csv,noheader | wc -l)
    # Vérification de la limite de consommation
    if (( GPU_USAGE >= LIMIT )); 
        then
        # Écriture des données dans le fichier de sortie
        echo "$(date) - GPU usage: ${GPU_USAGE}%, Process count: ${PROCESS_COUNT}" >> ${OUTPUT_FILE} 
    fi
    # Attente de 5 secondes avant de recommencer la boucle
    sleep 2 
done