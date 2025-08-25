# Scripts d'exploitation

Ce dossier contient tous les scripts Python utilisés pour résoudre le challenge Ecotech.

## Scripts principaux

### 1. extract_png_from_pcap.py
**Objectif** : Reconstruire l'image PNG corrompue à partir de la capture réseau
**Utilisation** : `python3 extract_png_from_pcap.py`
**Sortie** : `challenge_message.png`

### 2. test_upload.py
**Objectif** : Tester la fonctionnalité d'upload de fichiers
**Utilisation** : `python3 test_upload.py`
**Découverte** : Vulnérabilité de command injection

### 3. test_lfi.py
**Objectif** : Tester les vulnérabilités LFI (Local File Inclusion)
**Utilisation** : `python3 test_lfi.py`
**Découverte** : Paramètre `file` vulnérable

### 4. command_injection_exploit.py
**Objectif** : Exploiter la command injection via l'upload de fichiers
**Utilisation** : `python3 command_injection_exploit.py`
**Fonctionnalités** : Exécution de commandes arbitraires

### 5. find_suid_files.py
**Objectif** : Rechercher les fichiers SUID sur le système
**Utilisation** : `python3 find_suid_files.py`
**Découverte** : Binaire `/usr/bin/ecotech`

### 6. analyze_ecotech_binary.py
**Objectif** : Analyser le comportement du binaire SUID ecotech
**Utilisation** : `python3 analyze_ecotech_binary.py`
**Découverte** : Logique de validation du binaire

### 7. extract_ecotech_binary.py
**Objectif** : Extraire le binaire ecotech pour analyse avec IDA
**Utilisation** : `python3 extract_ecotech_binary.py`
**Sortie** : `ecotech_binary`

### 8. execute_ecotech_correctly.py
**Objectif** : Exploiter le binaire avec les bons arguments
**Utilisation** : `python3 execute_ecotech_correctly.py`
**Résultat** : Récupération du flag

## Scripts secondaires

### test_ssti.py
**Objectif** : Tester les vulnérabilités SSTI (Server-Side Template Injection)

### test_php_wrappers.py
**Objectif** : Tester les PHP wrappers pour contourner les protections

### extract_compressed_flag.py
**Objectif** : Tenter de décompresser le contenu `zzzzZZZZZzzzzzzzzzzzz`

### reverse_shell_attempts.py
**Objectif** : Tenter d'établir un reverse shell

## Ordre d'exécution recommandé

1. `extract_png_from_pcap.py` - Extraire l'image et découvrir l'URL
2. `test_upload.py` - Découvrir la command injection
3. `command_injection_exploit.py` - Obtenir un shell
4. `find_suid_files.py` - Découvrir le binaire SUID
5. `analyze_ecotech_binary.py` - Comprendre le binaire
6. `extract_ecotech_binary.py` - Extraire pour analyse IDA
7. `execute_ecotech_correctly.py` - Exploiter et récupérer le flag

## Configuration

Tous les scripts utilisent la variable `BASE_URL = "http://54.174.169.185:3000"` qui peut être modifiée si nécessaire.

## Dépendances

Installez les dépendances avec :
```bash
pip install -r ../requirements.txt
```

## Notes personnelles

Ces scripts ont été développés au fur et à mesure de la progression dans le challenge. Chaque script correspond à une étape spécifique de l'exploitation et permet de comprendre la méthodologie utilisée pour résoudre le challenge.
