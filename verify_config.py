#!/usr/bin/env python3
"""
Script de verificación de configuración para Lab 05
Ejecutar antes de abrir el notebook para verificar que todo esté configurado correctamente
"""

import os
from pathlib import Path

print("="*80)
print("VERIFICACIÓN DE CONFIGURACIÓN - LAB 05")
print("="*80)

# 1. Verificar que existe .env
env_file = Path(".env")
if not env_file.exists():
    print("\n❌ ERROR: No se encontró el archivo .env")
    print("   Crea un archivo .env en la raíz del proyecto con:")
    print("   AZURE_OPENAI_ENDPOINT=https://iki-genai-sandbox-resource.openai.azure.com/")
    print("   AZURE_OPENAI_API_KEY=tu-api-key-aqui")
    print("   AZURE_OPENAI_API_VERSION=2024-02-15-preview")
    print("   AZURE_OPENAI_DEPLOYMENT_GPT4=gpt-4o-mini")
    exit(1)

print("\n✓ Archivo .env encontrado")

# 2. Cargar .env manualmente
env_vars = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            env_vars[key] = value
            os.environ[key] = value

# 3. Verificar variables requeridas
required_vars = [
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_API_VERSION",
    "AZURE_OPENAI_DEPLOYMENT_GPT4"
]

missing_vars = []
for var in required_vars:
    if var not in env_vars or not env_vars[var]:
        missing_vars.append(var)
    else:
        # Mostrar valor (ocultar API key)
        value = env_vars[var]
        if "KEY" in var:
            display_value = value[:10] + "..." + value[-10:] if len(value) > 20 else "***"
        else:
            display_value = value
        print(f"✓ {var}: {display_value}")

if missing_vars:
    print(f"\n❌ ERROR: Faltan las siguientes variables:")
    for var in missing_vars:
        print(f"   - {var}")
    exit(1)

# 4. Verificar formato del endpoint
endpoint = env_vars["AZURE_OPENAI_ENDPOINT"]
if not endpoint.startswith("https://"):
    print(f"\n⚠️  ADVERTENCIA: El endpoint debería comenzar con https://")
if not endpoint.endswith("/"):
    print(f"\n⚠️  ADVERTENCIA: El endpoint debería terminar con /")

# 5. Intentar conexión de prueba
print("\n" + "="*80)
print("PRUEBA DE CONEXIÓN")
print("="*80)

try:
    import json
    import urllib.request
    
    url = f"{endpoint}openai/deployments/{env_vars['AZURE_OPENAI_DEPLOYMENT_GPT4']}/chat/completions?api-version={env_vars['AZURE_OPENAI_API_VERSION']}"
    
    data = {
        "messages": [{"role": "user", "content": "Test"}],
        "max_tokens": 5
    }
    
    headers = {
        "Content-Type": "application/json",
        "api-key": env_vars["AZURE_OPENAI_API_KEY"]
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    with urllib.request.urlopen(req, timeout=10) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(f"\n✅ CONEXIÓN EXITOSA")
        print(f"   Modelo: {result.get('model', 'N/A')}")
        print(f"   Tokens usados: {result['usage']['total_tokens']}")
        
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"\n❌ ERROR HTTP {e.code}:")
    print(f"   {error_body}")
    print("\n   Verifica:")
    print("   1. Que la API key sea correcta")
    print("   2. Que el endpoint sea correcto")
    print("   3. Que el deployment name sea correcto")
    exit(1)
    
except Exception as e:
    print(f"\n❌ ERROR DE CONEXIÓN:")
    print(f"   {type(e).__name__}: {e}")
    print("\n   Verifica:")
    print("   1. Que tengas conexión a internet")
    print("   2. Que el endpoint sea correcto")
    print("   3. Que no haya firewall bloqueando la conexión")
    exit(1)

print("\n" + "="*80)
print("✅ CONFIGURACIÓN CORRECTA - LISTO PARA USAR EL NOTEBOOK")
print("="*80)
print("\nAhora puedes abrir el notebook:")
print("  jupyter notebook labs/lab05/lab05_azure_openai_basics.ipynb")
