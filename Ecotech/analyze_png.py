#!/usr/bin/env python3
"""
Script pour analyser le PNG et chercher des données cachées.
"""

from PIL import Image
import struct
import binascii

def analyze_png():
    """Analyse le PNG pour chercher des données cachées"""
    
    try:
        # Ouvrir l'image
        img = Image.open('fixed_image.png')
        print(f"✓ Image ouverte avec succès!")
        print(f"Format: {img.format}")
        print(f"Mode: {img.mode}")
        print(f"Taille: {img.size}")
        print(f"Info: {img.info}")
        
        # Analyser les pixels pour chercher des patterns
        print("\n=== Analyse des pixels ===")
        pixels = list(img.getdata())
        print(f"Nombre de pixels: {len(pixels)}")
        
        # Chercher des patterns dans les bits de poids faible
        print("\n=== Analyse des bits de poids faible ===")
        lsb_data = []
        for pixel in pixels[:100]:  # Analyser les 100 premiers pixels
            if isinstance(pixel, tuple):
                for color in pixel:
                    lsb_data.append(color & 1)
            else:
                lsb_data.append(pixel & 1)
        
        # Convertir les LSB en bytes
        lsb_bytes = []
        for i in range(0, len(lsb_data), 8):
            if i + 7 < len(lsb_data):
                byte = 0
                for j in range(8):
                    byte |= lsb_data[i + j] << j
                lsb_bytes.append(byte)
        
        print(f"Premiers bytes LSB: {lsb_bytes[:20]}")
        
        # Chercher des patterns ASCII
        lsb_text = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in lsb_bytes[:50]])
        print(f"Premiers caractères LSB: {lsb_text}")
        
        # Analyser les métadonnées
        print("\n=== Métadonnées ===")
        for key, value in img.info.items():
            print(f"{key}: {value}")
        
        # Chercher des chunks PNG cachés
        print("\n=== Analyse des chunks PNG ===")
        with open('fixed_image.png', 'rb') as f:
            data = f.read()
        
        # Chercher des chunks PNG
        chunks = []
        offset = 8  # Skip PNG header
        while offset < len(data):
            if offset + 8 > len(data):
                break
            length = struct.unpack('>I', data[offset:offset+4])[0]
            chunk_type = data[offset+4:offset+8].decode('ascii', errors='ignore')
            chunks.append((chunk_type, length, offset))
            offset += 8 + length + 4  # length + type + data + crc
        
        print("Chunks PNG trouvés:")
        for chunk_type, length, offset in chunks:
            print(f"  {chunk_type}: {length} bytes à l'offset {offset}")
            
            # Analyser les chunks suspects
            if chunk_type not in ['IHDR', 'IDAT', 'IEND', 'PLTE']:
                print(f"    Chunk suspect trouvé: {chunk_type}")
                chunk_data = data[offset+8:offset+8+length]
                print(f"    Données: {chunk_data[:50]}")
                
                # Chercher du texte dans les chunks suspects
                try:
                    text = chunk_data.decode('utf-8', errors='ignore')
                    if any(keyword in text.lower() for keyword in ['flag', 'ctf', 'secret', 'hidden']):
                        print(f"    ⚠ TEXTE SUSPECT TROUVÉ: {text}")
                except:
                    pass
        
        # Chercher des données après la fin du PNG
        print("\n=== Données après la fin du PNG ===")
        png_end = data.find(b'IEND')
        if png_end != -1:
            png_end += 8  # IEND + CRC
            if png_end < len(data):
                trailing_data = data[png_end:]
                print(f"Données après PNG: {len(trailing_data)} bytes")
                print(f"Premiers bytes: {trailing_data[:50]}")
                
                # Chercher du texte
                try:
                    text = trailing_data.decode('utf-8', errors='ignore')
                    if text.strip():
                        print(f"Texte trouvé: {text[:200]}")
                except:
                    pass
        
    except Exception as e:
        print(f"Erreur lors de l'analyse: {e}")

if __name__ == "__main__":
    analyze_png()
