# Fichiers extraits

Ce dossier contient les fichiers extraits et reconstruits pendant la résolution du challenge.

## challenge_message.png

**Source** : Données extraites de `ExFilTr4T1oN.pcap`
**Méthode** : Reconstruction via `extract_png_from_pcap.py`
**Contenu** : Message du challenge avec l'URL de la plateforme web

### Message contenu :
```
Lors de la dernière semaine de ma mission, mes investigations m'ont mené vers une plateforme web : http://54.174.169.185:3000/

Elle présentait une faille... je ne me souviens plus exactement laquelle, mais tu devrais pouvoir la détecter sans trop de difficulté.

Dans le fichier /root/r00t.txt, une trace de mon passage t'attend.

Bonne chance.
```

## ecotech_binary

**Source** : `/usr/bin/ecotech` sur le serveur cible
**Méthode** : Extraction via command injection (`base64 /usr/bin/ecotech`)
**Type** : Binaire ELF 64-bit LSB pie executable
**Taille** : 16544 bytes
**Analyse** : IDA Pro pour reverse engineering

### Informations du binaire :
- **Permissions** : SUID (Set User ID)
- **Architecture** : x86-64
- **Type** : Dynamically linked
- **Build ID** : 5b000556dde7deaca9c6fcc3a772fc7dc950a229

### Logique découverte :
- Attend 2 arguments : `./ecotech <fichier> <mot_de_passe>`
- Mot de passe : `ec0T3cH060925_MAVA!`
- Fichier doit commencer par `/root/`
- Lit et affiche le contenu du fichier si les conditions sont remplies

## Utilisation

Ces fichiers sont utilisés pour :
1. **challenge_message.png** : Découvrir l'URL cible et comprendre l'objectif
2. **ecotech_binary** : Analyser avec IDA Pro pour comprendre la logique d'exploitation

## Extraction

Pour extraire ces fichiers :

```bash
# Extraire l'image
python3 ../scripts/extract_png_from_pcap.py

# Extraire le binaire
python3 ../scripts/extract_ecotech_binary.py
```
