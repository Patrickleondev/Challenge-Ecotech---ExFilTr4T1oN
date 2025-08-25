# Challenge Ecotech - ExFilTr4T1oN

## Description

Ce challenge de type CTF (Capture The Flag) implique l'analyse d'une capture réseau, l'extraction de données cachées, et l'exploitation d'une plateforme web pour obtenir un accès root et récupérer le flag.

## Contexte personnel

J'ai eu l'opportunité de participer à ce challenge grâce à Charles qui m'a invité. Malgré la pression de la journée, cette expérience m'a permis d'apprendre énormément sur les techniques d'exploitation web, l'analyse de captures réseau, et le reverse engineering de binaires. C'était un excellent exercice pratique qui a renforcé mes compétences en sécurité informatique.

## Fichiers fournis

- `ExFilTr4T1oN.pcap` - Capture réseau contenant des données exfiltrées
- `Get your free ticket !.pdf` - Description du challenge

## Objectif

Accéder au fichier `/root/r00t.txt` sur la plateforme web cible et récupérer le flag.

## Structure du repository

```
Ecotech/
├── README.md                    # Ce fichier
├── SOLUTION.md                  # Solution détaillée étape par étape
├── ExFilTr4T1oN.pcap           # Capture réseau (données exfiltrées)
├── Get your free ticket !.pdf  # Description du challenge
├── scripts/
│   ├── extract_png_from_pcap.py # Script de reconstruction d'image PNG
│   ├── test_upload.py          # Script de test d'upload
│   ├── test_lfi.py             # Script de test LFI
│   ├── command_injection_exploit.py  # Exploitation command injection
│   ├── find_suid_files.py      # Recherche de fichiers SUID
│   ├── analyze_ecotech_binary.py     # Analyse du binaire SUID
│   ├── extract_ecotech_binary.py     # Extraction du binaire
│   └── execute_ecotech_correctly.py  # Exploitation finale
├── extracted/
│   ├── challenge_message.png   # Image reconstruite avec le message
│   └── ecotech_binary          # Binaire extrait pour analyse
└── docs/
    └── challenge_description.md # Description détaillée du challenge
```

## Prérequis

- Python 3.13 (ce que moi meme j'ai utilisé)
- Wireshark ou tcpdump pour l'analyse de capture
- un outil pour l'analyse de binaires
- Outils de pentest web, vous en connaissez plus que moi

## Démarrage rapide

1. Analyser la capture réseau `ExFilTr4T1oN.pcap`
2. Extraire et reconstruire l'image PNG
3. Découvrir l'URL de la plateforme web
4. Énumérer les vulnérabilités
5. Exploiter la command injection
6. Analyser le binaire SUID
7. Récupérer le flag

## Flag obtenu

```
oozons{V0us_4v3Z_GagNe_UN_7ickeT_GR47UIT_RRRENdez_v0uS_p0UR_L3_EcoTECH_PARTYYYYYY_L3_06_08_2025}
```

## Techniques utilisées

- Analyse de capture réseau
- Reconstruction de fichiers corrompus
- Énumération web
- Local File Inclusion (LFI)
- Command injection
- Privilege escalation via binaires SUID
- Reverse engineering
- Exploitation de binaires

## Remerciements

Un grand merci à Charles pour m'avoir invité à participer à ce challenge. Cette expérience a été très enrichissante et m'a permis de mettre en pratique mes connaissances en sécurité informatique dans un contexte réaliste.



Ce repository est fourni à des fins éducatives uniquement.
