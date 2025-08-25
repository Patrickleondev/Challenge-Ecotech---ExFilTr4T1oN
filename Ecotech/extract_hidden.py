#!/usr/bin/env python3
"""
Script pour extraire les données cachées du PNG.
"""

import base64
import struct
import binascii
import re

def extract_hidden_data():
    """Extrait les données cachées du PNG"""
    
    print("=== Extraction des données cachées ===")
    
    # Lire le fichier PNG
    with open('fixed_image.png', 'rb') as f:
        data = f.read()
    
    print(f"Taille du fichier: {len(data)} bytes")
    
    # 1. Vérifier la signature PNG
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        print("✓ Signature PNG valide")
    else:
        print("⚠ Signature PNG invalide")
    
    # 2. Analyser les chunks PNG
    print("\n=== Analyse des chunks PNG ===")
    chunks = []
    offset = 8  # Skip PNG header
    
    while offset < len(data):
        if offset + 8 > len(data):
            break
        try:
            length = struct.unpack('>I', data[offset:offset+4])[0]
            chunk_type = data[offset+4:offset+8].decode('ascii', errors='ignore')
            chunks.append((chunk_type, length, offset))
            offset += 8 + length + 4  # length + type + data + crc
        except:
            break
    
    print("Chunks trouvés:")
    for chunk_type, length, offset in chunks:
        print(f"  {chunk_type}: {length} bytes à l'offset {offset}")
    
    # 3. Chercher des chunks suspects
    print("\n=== Chunks suspects ===")
    for chunk_type, length, offset in chunks:
        if chunk_type not in ['IHDR', 'IDAT', 'IEND', 'PLTE']:
            print(f"Chunk suspect: {chunk_type}")
            chunk_data = data[offset+8:offset+8+length]
            print(f"  Données: {chunk_data[:100]}")
            
            # Essayer de décoder en texte
            try:
                text = chunk_data.decode('utf-8', errors='ignore')
                if text.strip():
                    print(f"  Texte: {text}")
            except:
                pass
    
    # 4. Chercher des données après IEND
    print("\n=== Données après IEND ===")
    iend_pos = data.find(b'IEND')
    if iend_pos != -1:
        iend_pos += 8  # IEND + CRC
        if iend_pos < len(data):
            trailing_data = data[iend_pos:]
            print(f"Données après IEND: {len(trailing_data)} bytes")
            print(f"Premiers bytes: {trailing_data[:100]}")
            
            # Essayer de décoder en base64
            try:
                decoded = base64.b64decode(trailing_data)
                print(f"Base64 décodé: {decoded[:100]}")
            except:
                pass
            
            # Essayer de décoder en texte
            try:
                text = trailing_data.decode('utf-8', errors='ignore')
                if text.strip():
                    print(f"Texte: {text}")
            except:
                pass
    
    # 5. Analyser les bits de poids faible des pixels
    print("\n=== Analyse LSB ===")
    try:
        # Chercher les données IDAT
        idat_chunks = [c for c in chunks if c[0] == 'IDAT']
        if idat_chunks:
            idat_data = b''
            for chunk_type, length, offset in idat_chunks:
                chunk_data = data[offset+8:offset+8+length]
                idat_data += chunk_data
            
            print(f"Données IDAT: {len(idat_data)} bytes")
            
            # Analyser les premiers bytes pour des patterns
            print(f"Premiers bytes IDAT: {idat_data[:50]}")
            
            # Chercher des patterns dans les bits de poids faible
            lsb_pattern = []
            for byte in idat_data[:100]:
                lsb_pattern.append(byte & 1)
            
            # Convertir en bytes
            lsb_bytes = []
            for i in range(0, len(lsb_pattern), 8):
                if i + 7 < len(lsb_pattern):
                    byte = 0
                    for j in range(8):
                        byte |= lsb_pattern[i + j] << j
                    lsb_bytes.append(byte)
            
            print(f"LSB bytes: {lsb_bytes[:20]}")
            
            # Chercher du texte dans les LSB
            lsb_text = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in lsb_bytes[:50]])
            print(f"LSB texte: {lsb_text}")
            
    except Exception as e:
        print(f"Erreur lors de l'analyse LSB: {e}")
    
    # 6. Chercher des patterns hexadécimaux
    print("\n=== Recherche de patterns hex ===")
    hex_patterns = re.findall(rb'[0-9a-fA-F]{8,}', data)
    for pattern in hex_patterns[:5]:
        print(f"Pattern hex: {pattern}")
        try:
            decoded = bytes.fromhex(pattern.decode())
            text = decoded.decode('utf-8', errors='ignore')
            if text.isprintable():
                print(f"  Texte: {text}")
        except:
            pass
    
    # 7. Chercher des chaînes de caractères
    print("\n=== Recherche de chaînes ===")
    strings = re.findall(rb'[A-Za-z0-9_\-]{4,}', data)
    for string in strings[:10]:
        try:
            text = string.decode('utf-8')
            if any(keyword in text.lower() for keyword in ['flag', 'ctf', 'secret', 'hidden', 'key']):
                print(f"Chaîne suspecte: {text}")
        except:
            pass

if __name__ == "__main__":
    extract_hidden_data()
