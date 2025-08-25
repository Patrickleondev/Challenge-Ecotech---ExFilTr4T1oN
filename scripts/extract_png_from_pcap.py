#!/usr/bin/env python3
"""
Script pour corriger le PNG en décodant le base64 en binaire.
"""

import base64

def fix_png():
    """Corrige le PNG en décodant le base64 en binaire"""
    
    # Lire le fichier resultat_decode.txt
    with open('resultat_decode.txt', 'r') as f:
        base64_content = f.read().strip()
    
    print(f"Longueur du contenu base64: {len(base64_content)} caracteres")
    
    # Décoder le base64 en binaire
    try:
        binary_content = base64.b64decode(base64_content)
        print(f"Longueur du contenu binaire: {len(binary_content)} bytes")
        
        # Sauvegarder en binaire
        with open('fixed_image.png', 'wb') as f:
            f.write(binary_content)
        
        print("Image PNG corrigee sauvegardee dans 'fixed_image.png'")
        
        # Vérifier les premiers bytes pour confirmer que c'est un PNG
        if binary_content[:8] == b'\x89PNG\r\n\x1a\n':
            print("✓ Signature PNG valide detectee!")
        else:
            print("⚠ Signature PNG non detectee, mais le fichier a ete cree.")
            
    except Exception as e:
        print(f"Erreur lors du decodage: {e}")

if __name__ == "__main__":
    fix_png()
