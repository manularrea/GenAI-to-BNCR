# Guía del Instructor - Curso GenAI para BNCR

## Información General del Curso

**Nombre del Curso:** Generative AI for Banking Sector  
**Cliente:** Banco Nacional de Costa Rica (BNCR)  
**Duración Total:** 60 horas (20 clases de 3 horas)  
**Formato:** Híbrido (teoría + práctica hands-on)  
**Nivel:** Intermedio-Avanzado  
**Instructor Principal:** Manuela Larrea (manuela.larrea@idataglobal.com)

---

## Estructura del Curso

### Clases 1-5: Fundamentos (No incluidas en este repositorio)
- Clase 1: Introducción a GenAI
- Clase 2: Fundamentos de LLMs
- Clase 3: Azure OpenAI Overview
- Clase 4: APIs y Autenticación
- Clase 5: Primeros Pasos con Python

### Clases 6-20: Implementación Práctica (Incluidas en este repositorio)

Cada clase sigue esta estructura:
- **45 minutos:** Presentación teórica
- **30 minutos:** Demostración en vivo
- **90 minutos:** Lab práctico (hands-on)
- **15 minutos:** Q&A y cierre

---

## Contenido por Clase

### Clase 6: Prompt Engineering para Aplicaciones Bancarias
**Lab:** lab05_azure_openai_basics.ipynb  
**Objetivos:**
- Diseñar prompts efectivos para casos bancarios
- Aplicar técnicas zero-shot, few-shot, chain-of-thought
- Crear templates reutilizables

**Puntos Clave:**
- Prompt engineering puede mejorar precisión en 40-60%
- Estructura: Rol, Instrucción, Contexto, Formato, Restricciones
- Few-shot mejora consistencia dramáticamente

**Demostración:**
1. Mostrar prompt básico con resultado mediocre
2. Iterar agregando contexto y ejemplos
3. Comparar resultados lado a lado

**Ejercicios del Lab:**
- Clasificación de intenciones de clientes
- Extracción de información estructurada
- Generación de respuestas personalizadas

---

### Clase 7: Gestión Avanzada de Conversaciones
**Lab:** lab07_conversation_management.ipynb  
**Objetivos:**
- Implementar gestión de estado conversacional
- Detectar intenciones y sentimientos
- Manejar escalaciones a agentes humanos

**Puntos Clave:**
- Conversaciones stateful requieren context tracking
- Sentiment analysis permite escalación proactiva
- Logging esencial para QA y mejora continua

**Demostración:**
1. Chatbot sin gestión de estado (malo)
2. Chatbot con context management (bueno)
3. Escalación automática por sentimiento negativo

**Ejercicios del Lab:**
- Construir asistente de solicitud de préstamos
- Implementar sistema de routing inteligente
- Crear métricas de calidad conversacional

---

### Clase 8: Function Calling e Integración de Herramientas
**Lab:** lab08_function_calling.ipynb  
**Objetivos:**
- Entender function calling en Azure OpenAI
- Definir schemas de funciones bancarias
- Implementar validación y seguridad

**Puntos Clave:**
- Function calling permite interacción con sistemas reales
- Schemas JSON definen funciones disponibles
- Validación y límites son críticos para seguridad

**Demostración:**
1. Consulta de saldo con function calling
2. Transferencia con validación multi-paso
3. Manejo de errores y límites

**Ejercicios del Lab:**
- Sistema de pago de facturas
- Gestor de portafolio de inversiones
- Integración de detección de fraude

---

### Clase 9: Embeddings y Búsqueda Semántica
**Lab:** lab09_embeddings_and_semantic_search.ipynb  
**Objetivos:**
- Entender qué son los embeddings
- Implementar búsqueda semántica
- Construir sistema de búsqueda de FAQs

**Puntos Clave:**
- Embeddings convierten texto a vectores numéricos
- Búsqueda semántica entiende significado, no solo keywords
- Critical para knowledge bases bancarias

**Demostración:**
1. Búsqueda por keywords (limitada)
2. Búsqueda semántica (superior)
3. Comparación de resultados

**Ejercicios del Lab:**
- Motor de búsqueda de FAQs bancarias
- Sistema de recomendación de productos
- Detector de similitud de documentos

---

### Clase 10: RAG (Retrieval-Augmented Generation)
**Lab:** lab10_rag_(retrieval_augmented_generation).ipynb  
**Objetivos:**
- Entender arquitectura RAG
- Implementar chunking de documentos
- Construir knowledge base bancaria

**Puntos Clave:**
- RAG combina retrieval con generation
- Soluciona problema de "hallucinations"
- Esencial para políticas y compliance

**Demostración:**
1. LLM sin RAG (respuestas genéricas/incorrectas)
2. LLM con RAG (respuestas precisas y fundamentadas)
3. Mostrar fuentes de información

**Ejercicios del Lab:**
- Chatbot de políticas bancarias
- Sistema Q&A de documentos
- Catálogo de productos con RAG

---

### Clase 11: Azure AI Search Integration
**Lab:** lab11_azure_ai_search_integration.ipynb  
**Objetivos:**
- Configurar Azure AI Search
- Implementar hybrid search
- Integrar con Azure OpenAI

**Puntos Clave:**
- Azure AI Search = enterprise-grade search
- Hybrid search combina keyword + semantic
- Filtering y faceting para precisión

**Demostración:**
1. Indexar documentos bancarios
2. Búsqueda híbrida en acción
3. Filtros y facetas

**Ejercicios del Lab:**
- Indexar documentación bancaria
- Construir sistema de búsqueda híbrida
- Implementar búsqueda con filtros

---

### Clase 12: Moderación de Contenido y Seguridad
**Lab:** lab12_content_moderation_and_safety.ipynb  
**Objetivos:**
- Implementar Azure Content Safety
- Detectar y redactar PII
- Prevenir jailbreaks

**Puntos Clave:**
- Content moderation es obligatoria para customer-facing AI
- PII detection previene fugas de datos
- Audit logging para compliance

**Demostración:**
1. Contenido dañino detectado y bloqueado
2. PII automáticamente redactado
3. Intento de jailbreak prevenido

**Ejercicios del Lab:**
- Implementar filtro de contenido
- Sistema de redacción de PII
- Dashboard de monitoreo de seguridad

---

### Clase 13: Fine-tuning para el Dominio Bancario
**Lab:** lab13_fine_tuning_for_banking_domain.ipynb  
**Objetivos:**
- Decidir cuándo fine-tunear
- Preparar datos de entrenamiento
- Evaluar modelos fine-tuneados

**Puntos Clave:**
- Fine-tuning vs prompt engineering
- Calidad de datos > cantidad
- Análisis costo-beneficio esencial

**Demostración:**
1. Modelo base vs fine-tuneado
2. Mejoras en precisión y tono
3. Métricas de evaluación

**Ejercicios del Lab:**
- Preparar dataset de fine-tuning
- Fine-tunear modelo
- Evaluar performance

---

### Clase 14: IA Multimodal - Visión y Documentos
**Lab:** lab14_multimodal_ai___vision_and_documents.ipynb  
**Objetivos:**
- Usar GPT-4 Vision
- Procesar documentos bancarios
- Extraer datos de formularios

**Puntos Clave:**
- GPT-4 Vision procesa imágenes y documentos
- OCR + comprensión semántica
- Automatiza procesamiento de formularios

**Demostración:**
1. Análisis de cheque bancario
2. Extracción de datos de formulario
3. Comprensión de gráficos financieros

**Ejercicios del Lab:**
- Extraer datos de cheques
- Analizar estados financieros
- Procesar formularios de préstamos

---

### Clase 15: Frameworks de Agentes y LangChain
**Lab:** lab15_agent_frameworks_and_langchain.ipynb  
**Objetivos:**
- Entender arquitectura de agentes
- Usar LangChain
- Construir agentes autónomos

**Puntos Clave:**
- Agentes pueden usar múltiples herramientas
- LangChain simplifica workflows complejos
- Memory management para contexto

**Demostración:**
1. Agente simple con una herramienta
2. Agente multi-tool
3. Agente con memoria

**Ejercicios del Lab:**
- Construir agente multi-herramienta
- Crear agente de investigación
- Implementar agente de planificación

---

### Clase 16: Despliegue en Producción en Azure
**Lab:** lab16_production_deployment_on_azure.ipynb  
**Objetivos:**
- Arquitectura de producción
- API Management
- Monitoreo y logging

**Puntos Clave:**
- Deployment requires proper architecture
- API Management para seguridad
- Monitoring esencial para operaciones

**Demostración:**
1. Deploy API a Azure
2. Configurar API Management
3. Dashboard de monitoreo

**Ejercicios del Lab:**
- Desplegar API a Azure
- Configurar monitoreo
- Implementar rate limiting

---

### Clase 17: Testing y Evaluación
**Lab:** lab17_testing_and_evaluation.ipynb  
**Objetivos:**
- Métricas de evaluación de LLMs
- Testing automatizado
- A/B testing

**Puntos Clave:**
- LLM evaluation requiere métricas especializadas
- Automated testing previene regresiones
- Human evaluation sigue siendo crítica

**Demostración:**
1. Suite de tests automatizados
2. Métricas de evaluación
3. A/B test results

**Ejercicios del Lab:**
- Crear suite de tests
- Implementar métricas de evaluación
- Construir dashboard de comparación

---

### Clase 18: Ética, Sesgo e IA Responsable
**Lab:** lab18_ethics,_bias,_and_responsible_ai.ipynb  
**Objetivos:**
- Identificar sesgos en AI
- Métricas de fairness
- Compliance regulatorio

**Puntos Clave:**
- AI bias puede perpetuar discriminación
- Transparency builds trust
- Regulatory compliance es obligatorio

**Demostración:**
1. Detección de sesgo en modelo
2. Métricas de fairness
3. Transparency report

**Ejercicios del Lab:**
- Auditar modelo por sesgo
- Crear reporte de transparencia
- Implementar checks de fairness

---

### Clase 19: Optimización de Costos y Rendimiento
**Lab:** lab19_cost_optimization_and_performance.ipynb  
**Objetivos:**
- Optimizar uso de tokens
- Estrategias de caching
- Selección de modelos

**Puntos Clave:**
- Token usage impacta costos directamente
- Caching reduce llamadas redundantes
- Model selection afecta costo y calidad

**Demostración:**
1. Análisis de costos
2. Implementación de caching
3. Comparación GPT-4 vs GPT-3.5

**Ejercicios del Lab:**
- Implementar sistema de caching
- Optimizar uso de tokens
- Dashboard de monitoreo de costos

---

### Clase 20: Proyecto Final - Asistente Bancario IA
**Lab:** lab20_final_project___banking_ai_assistant.ipynb  
**Formato:** Session de trabajo de proyecto (3 horas)

**Objetivos:**
- Integrar todos los conceptos aprendidos
- Implementación production-ready
- Presentar y defender decisiones

**Requerimientos del Proyecto:**
- Chatbot bancario funcional
- Integración con al menos 3 funciones
- RAG para knowledge base
- Content moderation
- Logging y monitoring
- Documentación completa

**Evaluación:**
- Funcionalidad (30%)
- Calidad del código (20%)
- Arquitectura (20%)
- Seguridad (15%)
- Presentación (15%)

---

## Preparación para Cada Clase

### Antes de la Clase:
1. Revisar notebook del lab correspondiente
2. Probar todos los ejemplos de código
3. Verificar que Azure OpenAI esté funcionando
4. Preparar datos de ejemplo si es necesario
5. Revisar preguntas frecuentes de la clase anterior

### Durante la Clase:
1. **Presentación (45 min):**
   - Usar slides en `/presentations/classXX/`
   - Mantener ritmo dinámico
   - Hacer preguntas al grupo
   - Relacionar con casos bancarios reales

2. **Demostración (30 min):**
   - Usar Jupyter notebook en vivo
   - Explicar cada línea de código
   - Mostrar errores comunes y cómo resolverlos
   - Invitar participación del grupo

3. **Lab Práctico (90 min):**
   - Los estudiantes trabajan en sus notebooks
   - Circular para ayudar individualmente
   - Resolver dudas en tiempo real
   - Compartir soluciones interesantes

4. **Cierre (15 min):**
   - Recap de conceptos clave
   - Preview de próxima clase
   - Asignar lectura/preparación si aplica

### Después de la Clase:
1. Recopilar feedback
2. Actualizar materiales si es necesario
3. Responder preguntas pendientes por email
4. Preparar siguiente clase

---

## Recursos Técnicos Necesarios

### Para el Instructor:
- Laptop con Python 3.11+
- Jupyter Lab o VS Code con extensión de Jupyter
- Acceso a Azure OpenAI (keys configuradas)
- Proyector/pantalla compartida
- Repositorio GitHub clonado localmente

### Para los Estudiantes:
- Laptop con Python 3.11+
- Jupyter Lab o VS Code
- Acceso a Azure OpenAI (proporcionado por BNCR)
- Archivo `.env` con credenciales
- Repositorio GitHub clonado

### Datasets:
Todos los datasets están en `/datasets/banking/`:
- `banking_products.csv` - Productos bancarios
- `transactions.csv` - Transacciones de ejemplo
- `banking_faq.csv` - Preguntas frecuentes

---

## Solución de Problemas Comunes

### Problema: "Authentication failed"
**Solución:** Verificar que `.env` tiene las keys correctas y que no están expiradas.

### Problema: "Rate limit exceeded"
**Solución:** Esperar 60 segundos o usar diferentes deployment si disponible.

### Problema: "Module not found"
**Solución:** Ejecutar `pip install -r requirements.txt`

### Problema: Notebook no se conecta a kernel
**Solución:** Reiniciar Jupyter, verificar que Python 3.11 está seleccionado.

### Problema: Código funciona para instructor pero no para estudiantes
**Solución:** Verificar que todos tienen las mismas versiones de librerías.

---

## Evaluación del Curso

### Evaluación Continua:
- Participación en clase (10%)
- Completar labs (40%)
- Ejercicios prácticos (30%)
- Proyecto final (20%)

### Criterios de Éxito:
- Estudiante puede diseñar prompts efectivos
- Estudiante puede implementar chatbot funcional
- Estudiante entiende consideraciones de seguridad
- Estudiante puede desplegar a producción

---

## Contacto y Soporte

**Instructor Principal:**  
Manuela Larrea  
Email: manuela.larrea@idataglobal.com

**Repositorio del Curso:**  
https://github.com/manularrea/GenAI-to-BNCR

**Soporte Técnico BNCR:**  
[Contacto interno BNCR]

---

## Notas Finales

Este curso está diseñado para ser práctico y aplicable inmediatamente en BNCR. Enfatice siempre:
- **Seguridad primero:** Nunca exponer datos sensibles
- **Compliance:** Seguir regulaciones bancarias
- **Calidad sobre velocidad:** Mejor implementación correcta que rápida
- **Documentación:** Essential para mantenimiento
- **Testing:** Validar todo antes de producción

¡Éxito con el curso!

