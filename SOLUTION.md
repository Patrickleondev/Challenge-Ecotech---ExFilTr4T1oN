# Solution Challenge Ecotech - ExFilTr4T1oN

## Introduction

Ce challenge nous amène à analyser une capture réseau, extraire des données cachées, et exploiter une plateforme web pour obtenir un accès root et récupérer le flag.

## Étape 1 : Analyse de la capture réseau

La première étape consiste à analyser le fichier `ExFilTr4T1oN.pcap`. Cette capture contient des données exfiltrées qui nous permettront de découvrir les informations nécessaires pour la suite.

En examinant la capture, on découvre qu'elle contient des données PNG corrompues. L'analyse des paquets révèle que les données sont fragmentées et nécessitent une reconstruction.

## Étape 2 : Extraction et reconstruction de l'image

Le script `extract_png_from_pcap.py` a été créé pour reconstruire l'image PNG à partir des données fragmentées dans la capture réseau. Ce script :

- Parse les paquets de la capture
- Extrait les données PNG
- Reconstruit l'image en corrigeant les en-têtes
- Sauvegarde l'image réparée

L'exécution de ce script produit `challenge_message.png`, qui contient les informations cruciales pour la suite du challenge.

<img width="1086" height="421" alt="image" src="https://github.com/user-attachments/assets/13a0f023-3184-4726-9533-f9a20ebfe6fa" />

## Étape 3 : Analyse de l'image extraite

L'image `challenge_message.png` contient le message suivant :

```
Lors de la dernière semaine de ma mission, mes investigations m'ont mené vers une plateforme web : http://54.174.169.185:3000/

Elle présentait une faille... je ne me souviens plus exactement laquelle, mais tu devrais pouvoir la détecter sans trop de difficulté.

Dans le fichier /root/r00t.txt, une trace de mon passage t'attend.

Bonne chance.
```

Cette information nous donne :
- L'URL de la plateforme web cible
- L'indication d'une vulnérabilité à découvrir
- L'objectif : accéder au fichier `/root/r00t.txt`

## Étape 4 : Énumération de la plateforme web

L'accès à `http://54.174.169.185:3000/` révèle une application web avec plusieurs pages :
- Page d'accueil
- Page d'upload de fichiers
- Page "À propos"

L'énumération des paramètres révèle une vulnérabilité de Local File Inclusion (LFI) sur le paramètre `file` qui accepte des chemins relatifs et absolus.

## Étape 5 : Découverte de la command injection

L'analyse de la fonctionnalité d'upload révèle une vulnérabilité critique : le nom du fichier uploadé (sans l'extension) est exécuté comme une commande bash.

Cette découverte est cruciale car elle nous permet d'exécuter des commandes arbitraires sur le serveur avec les privilèges de l'utilisateur web.

## Étape 6 : Énumération du système

Via la command injection, on découvre :
- L'utilisateur actuel : `appuser` (uid=999)
- Le répertoire de travail : `/app`
- L'existence du fichier `/root/r00t.txt` (accès refusé)
- La présence de binaires SUID dans `/app` : `gunzip` et `less`

## Étape 7 : Découverte du binaire SUID ecotech

La recherche de fichiers SUID révèle un binaire particulièrement intéressant : `/usr/bin/ecotech`. Ce binaire a un nom suspect et des permissions SUID, ce qui en fait une cible privilégiée pour l'élévation de privilèges.

L'exécution du binaire sans arguments ou avec des arguments incorrects retourne `zzzzZZZZZzzzzzzzzzzzz`, ce qui indique une logique de validation.

## Étape 8 : Extraction et analyse du binaire

Pour comprendre le fonctionnement du binaire, on l'extrait du système via la command injection :

```bash
base64 /usr/bin/ecotech
```

Le binaire extrait (16544 bytes) est analysé avec IDA Pro pour comprendre sa logique interne.

## Étape 9 : Reverse engineering avec IDA Pro

<img width="1080" height="607" alt="image" src="https://github.com/user-attachments/assets/bf08a8b6-2f48-41b0-83c9-a0b9d842f34c" />

L'analyse du binaire révèle sa logique :

```c
int main(int argc, const char **argv, const char **envp) {
    if (argc == 3) {
        if (!strcmp(argv[2], "ec0T3cH060925_MAVA!")) {
            if (!strncmp(argv[1], "/root/", strlen("/root/"))) {
                // Lire et afficher le contenu du fichier
                printf("=== Contenu de %s ===\n", argv[1]);
                // ... lecture du fichier ...
                puts("\n====================");
            } else {
                fprintf(stderr, "n0 n0 n0 n0 n0 n0 n0 n0 n0 n0 n0 n0 n0");
            }
        } else {
            fwrite("zzzzZZZZZzzzzzzzzzzzz", 1, 0x15, stderr);
        }
    }
}
```

Cette analyse révèle :
- Le binaire attend 2 arguments : `./ecotech <fichier> <mot_de_passe>`
- Le mot de passe : `ec0T3cH060925_MAVA!`
- Le fichier doit commencer par `/root/`
- Si les conditions sont remplies, il lit et affiche le contenu du fichier

## Étape 10 : Exploitation finale

Avec ces informations, on peut maintenant exécuter le binaire avec les bons arguments :

```bash
/usr/bin/ecotech /root/r00t.txt ec0T3cH060925_MAVA!
```

Cette commande, exécutée via la command injection, retourne le contenu du fichier `/root/r00t.txt` avec les privilèges root.

## Flag obtenu

```
oozons{V0us_4v3Z_GagNe_UN_7ickeT_GR47UIT_RRRENdez_v0uS_p0UR_L3_EcoTECH_PARTYYYYYY_L3_06_08_2025}
```

