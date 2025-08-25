# Description du Challenge Ecotech

## Contexte

Lors de la dernière semaine de ma mission, mes investigations m'ont mené vers une plateforme web : `http://54.174.169.185:3000/`

Elle présentait une faille... je ne me souviens plus exactement laquelle, mais tu devrais pouvoir la détecter sans trop de difficulté.

Dans le fichier `/root/r00t.txt`, une trace de mon passage t'attend.

Bonne chance.

## Informations clés

- **Plateforme cible** : http://54.174.169.185:3000/
- **Objectif** : Accéder au fichier `/root/r00t.txt`
- **Type de challenge** : Web + Privilege Escalation
- **Difficulté** : Moyenne

## Points de départ

1. **Capture réseau** : Le fichier `ExFilTr4T1oN.pcap` contient des données exfiltrées
2. **Image cachée** : Les données de la capture contiennent une image PNG corrompue
3. **Message caché** : L'image reconstruite contient les informations du challenge

## Étapes suggérées

1. Analyser la capture réseau pour extraire les données
2. Reconstruire l'image PNG corrompue
3. Lire le message dans l'image
4. Accéder à la plateforme web
5. Énumérer les vulnérabilités
6. Exploiter les failles découvertes
7. Élever les privilèges
8. Accéder au fichier `/root/r00t.txt`

## Indices

- Le nom du fichier `ExFilTr4T1oN.pcap` est en leetspeak pour "Exfiltration"
- Le fichier `/root/r00t.txt` est également en leetspeak pour "root.txt"
- La vulnérabilité est "facile à détecter"
- Il faut "une trace de passage" dans le fichier cible
