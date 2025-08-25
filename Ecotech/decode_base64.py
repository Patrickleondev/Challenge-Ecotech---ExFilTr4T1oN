#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

def decode_base64_image():
    """Décode l'image base64 et la sauvegarde"""
    
    # Lire le contenu hexadécimal décodé
    with open('all_blocks.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire la partie base64 (après "=== MESSAGE DÉCODÉ ===")
    if "=== MESSAGE DÉCODÉ ===" in content:
        base64_data = content.split("=== MESSAGE DÉCODÉ ===")[1].strip()
        print(f"Longueur des données base64: {len(base64_data)} caractères")
    else:
        print("❌ Impossible de trouver les données base64")
        return
    
    try:
        # Décoder base64
        image_data = base64.b64decode(base64_data)
        print(f"Longueur des données d'image décodées: {len(image_data)} bytes")
        
        # Sauvegarder l'image
        with open('decoded_image.png', 'wb') as f:
            f.write(image_data)
        
        print("✅ Image décodée et sauvegardée dans 'decoded_image.png'")
        print("🔍 Ouvrez cette image pour voir le contenu caché")
        
    except Exception as e:
        print(f"❌ Erreur lors du décodage: {e}")

if __name__ == "__main__":
    decode_base64_image()
