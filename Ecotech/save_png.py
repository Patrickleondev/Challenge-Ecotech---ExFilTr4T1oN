#!/usr/bin/env python3
"""
Script pour sauvegarder le contenu PNG decode dans un fichier image.
"""

def save_png_from_result():
    """Sauvegarde le contenu PNG decode dans un fichier image"""
    
    # Lire le fichier resultat_decode.txt
    with open('resultat_decode.txt', 'r') as f:
        png_content = f.read().strip()
    
    print(f"Longueur du contenu PNG: {len(png_content)} caracteres")
    
    # Sauvegarder dans un fichier PNG
    with open('decoded_image.png', 'w') as f:
        f.write(png_content)
    
    print("Image PNG sauvegardee dans 'decoded_image.png'")
    print("Vous pouvez maintenant ouvrir ce fichier pour voir l'image decodee.")

if __name__ == "__main__":
    save_png_from_result()
