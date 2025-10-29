# 🔧 Troubleshooting - Lab 05

## Error: "getaddrinfo failed" o "APIConnectionError"

Este error significa que el cliente no puede conectarse al endpoint de Azure OpenAI.

### Solución:

1. **Verifica que tienes el archivo `.env` en la raíz del proyecto**

```bash
# Debe estar en: GenAI-to-BNCR/.env
ls -la .env
```

2. **Verifica el contenido del `.env`**

```bash
cat .env
```

Debe contener:

```env
AZURE_OPENAI_ENDPOINT=https://iki-genai-sandbox-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=[PROPORCIONADA_POR_INSTRUCTOR]
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_GPT4=gpt-4o-mini
AZURE_OPENAI_DEPLOYMENT_GPT35=gpt-4o-mini
```

3. **Ejecuta el script de verificación**

```bash
python verify_config.py
```

Este script te dirá exactamente qué está mal.

4. **Si el script pasa pero el notebook falla:**

Asegúrate de ejecutar las celdas en orden:
- Celda 1: Imports
- Celda 2: Load environment variables
- Celda 3: Initialize client
- Luego las demás

---

## Error: "Invalid API key" o "401 Unauthorized"

### Solución:

1. **Verifica que la API key sea correcta**

Ve a Azure Portal:
- iki-genai-sandbox-resource → Keys and Endpoint → Pestaña "OpenAI" → KEY 1

2. **Copia la key completa** (debe tener ~88 caracteres)

3. **Actualiza el `.env`** con la key correcta

---

## Error: "Deployment not found" o "404"

### Solución:

1. **Verifica el nombre del deployment**

En Azure AI Foundry:
- Models + endpoints → Model deployments

2. **Actualiza el `.env`** con el nombre correcto:

```env
AZURE_OPENAI_DEPLOYMENT_GPT4=gpt-4o-mini
```

---

## Error: "Rate limit exceeded"

### Solución:

1. **Espera unos segundos** y vuelve a intentar

2. **Reduce la frecuencia** de requests en el código

3. **Verifica los límites** en Azure Portal:
   - Model deployments → gpt-4o-mini → Capacity: 100K TPM

---

## El notebook no encuentra el módulo `openai`

### Solución:

```bash
pip install -r requirements.txt
```

O específicamente:

```bash
pip install openai==1.12.0
```

---

## El notebook no carga las variables de entorno

### Solución:

1. **Instala python-dotenv:**

```bash
pip install python-dotenv
```

2. **Verifica que la celda de carga esté correcta:**

```python
from dotenv import load_dotenv
load_dotenv()  # Esto debe estar ANTES de os.getenv()
```

3. **Reinicia el kernel** del notebook:
   - Kernel → Restart & Clear Output

---

## Verificación Rápida

Ejecuta esto en una celda del notebook:

```python
import os
from dotenv import load_dotenv

load_dotenv()

print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))
print("API Key:", os.getenv("AZURE_OPENAI_API_KEY")[:20] + "..." if os.getenv("AZURE_OPENAI_API_KEY") else "NO ENCONTRADA")
print("Deployment:", os.getenv("AZURE_OPENAI_DEPLOYMENT_GPT4"))
```

Deberías ver:
```
Endpoint: https://iki-genai-sandbox-resource.openai.azure.com/
API Key: BnTTgYvTuac9So9xANPB...
Deployment: gpt-4o-mini
```

---

## Contacto

Si ninguna solución funciona, contacta a:
- **Instructor:** Manuela Larrea
- **Email:** manuela.larrea@idataglobal.com

