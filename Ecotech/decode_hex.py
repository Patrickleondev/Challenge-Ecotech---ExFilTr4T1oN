#!/usr/bin/env python3
"""
Script pour décoder le contenu hexadécimal des blocs PCAP
et reconstituer le message de l'agent.
"""

import re

def decode_hex_blocks():
    """Décode le contenu hexadécimal des blocs"""
    
    # Lire le fichier all_blocks.txt
    with open('all_blocks.txt', 'r') as f:
        content = f.read()
    
    # Extraire tous les blocs hexadécimaux
    hex_blocks = []
    for line in content.strip().split('\n'):
        if line.strip():
            hex_blocks.append(line.strip())
    
    print(f"Nombre de blocs trouvés: {len(hex_blocks)}")
    
    # Concaténer tous les blocs
    full_hex = ''.join(hex_blocks)
    print(f"Longueur totale du hex: {len(full_hex)} caractères")
    
    # Décoder le hex en bytes
    try:
        decoded_bytes = bytes.fromhex(full_hex)
        print(f"Longueur des bytes décodés: {len(decoded_bytes)}")
        
        # Essayer de décoder en UTF-8
        try:
            decoded_text = decoded_bytes.decode('utf-8')
            print("=== MESSAGE DÉCODÉ ===")
            print(decoded_text)
            
            # Chercher le flag oozons{}
            flag_match = re.search(r'oozons\{[^}]*\}', decoded_text)
            if flag_match:
                print(f"\n🎉 FLAG TROUVÉ: {flag_match.group()}")
            else:
                print("\n❌ Aucun flag oozons{} trouvé dans le texte décodé")
                
        except UnicodeDecodeError:
            print("❌ Impossible de décoder en UTF-8")
            print("Affichage des premiers bytes:")
            print(decoded_bytes[:100])
            
            # Essayer d'autres encodages
            for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
                try:
                    decoded_text = decoded_bytes.decode(encoding)
                    print(f"\n=== DÉCODÉ AVEC {encoding.upper()} ===")
                    print(decoded_text[:500])
                    break
                except UnicodeDecodeError:
                    continue
    
    except ValueError as e:
        print(f"❌ Erreur lors du décodage hex: {e}")
        print("Vérification du format hex...")
        
        # Vérifier si c'est du hex valide
        hex_pattern = re.compile(r'^[0-9a-fA-F]+$')
        if hex_pattern.match(full_hex):
            print("✅ Format hex valide")
        else:
            print("❌ Format hex invalide")
            print("Premiers caractères:", full_hex[:50])

if __name__ == "__main__":
    decode_hex_blocks()
