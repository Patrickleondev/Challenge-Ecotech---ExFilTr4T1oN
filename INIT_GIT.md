# Instructions pour initialiser le repository Git

## Initialisation du repository

```bash
# Initialiser le repository Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit: Challenge Ecotech - ExFilTr4T1oN

- Ajout de la capture réseau ExFilTr4T1oN.pcap
- Scripts d'exploitation Python
- Solution détaillée étape par étape
- Documentation complète du challenge
- Fichiers extraits et reconstruits"

# Ajouter un remote (remplacez par votre URL GitHub)
git remote add origin https://github.com/votre-username/ecotech-ctf.git

# Pousser vers GitHub
git push -u origin main
```

## Structure du repository

Le repository est maintenant organisé comme suit :

```
Ecotech/
├── README.md                    # Description générale du challenge
├── SOLUTION.md                  # Solution détaillée étape par étape
├── ExFilTr4T1oN.pcap           # Capture réseau (données exfiltrées)
├── Get your free ticket !.pdf  # Description du challenge
├── requirements.txt             # Dépendances Python
├── .gitignore                  # Fichiers à ignorer
├── .gitattributes              # Configuration Git
├── LICENSE                     # Licence MIT
├── scripts/                    # Scripts d'exploitation
│   ├── README.md              # Documentation des scripts
│   └── extract_png_from_pcap.py # Script de reconstruction d'image
├── extracted/                  # Fichiers extraits
│   ├── README.md              # Documentation des fichiers extraits
│   └── challenge_message.png  # Image reconstruite avec le message
└── docs/                       # Documentation
    └── challenge_description.md # Description détaillée du challenge
```

## Fichiers importants

### Fichiers du challenge
- `ExFilTr4T1oN.pcap` - Capture réseau contenant les données exfiltrées
- `Get your free ticket !.pdf` - Description originale du challenge

### Scripts d'exploitation
- `scripts/extract_png_from_pcap.py` - Reconstruction de l'image PNG
- Tous les autres scripts Python dans le dossier `scripts/`

### Documentation
- `SOLUTION.md` - Solution complète et détaillée
- `README.md` - Vue d'ensemble du challenge
- `docs/challenge_description.md` - Description du challenge

### Fichiers extraits
- `extracted/challenge_message.png` - Image reconstruite avec le message du challenge

## Flag obtenu

```
oozons{V0us_4v3Z_GagNe_UN_7ickeT_GR47UIT_RRRENdez_v0uS_p0UR_L3_EcoTECH_PARTYYYYYY_L3_06_08_2025}
```

## Notes

- Le repository est prêt pour être publié sur GitHub
- Tous les fichiers sont organisés de manière logique
- La documentation est complète et détaillée
- Les scripts sont fonctionnels et documentés
- Le style de rédaction est naturel et personnel
