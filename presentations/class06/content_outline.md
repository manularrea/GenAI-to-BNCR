# Clase 6: Prompt Engineering para Aplicaciones Bancarias

## Información del Curso
- **Duración:** 3 horas
- **Formato:** 1.5 horas teoría + 1.5 horas práctica (Lab 06)
- **Audiencia:** Equipo técnico BNCR

## Objetivos de Aprendizaje

Al finalizar esta clase, los participantes podrán:
1. Diseñar prompts efectivos para casos de uso bancarios
2. Aplicar técnicas de zero-shot, few-shot y chain-of-thought
3. Implementar templates de prompts reutilizables
4. Optimizar prompts para precisión y consistencia
5. Evaluar y mejorar la calidad de las respuestas

## Estructura de la Presentación (45 min)

### 1. Introducción al Prompt Engineering (5 min)
- **Concepto clave:** El prompt engineering es el arte y ciencia de diseñar instrucciones efectivas para modelos de lenguaje
- **Por qué importa:** Un prompt bien diseñado puede mejorar la precisión en 40-60% sin cambiar el modelo
- **Aplicación BNCR:** Respuestas consistentes y precisas en atención al cliente

### 2. Anatomía de un Prompt Efectivo (10 min)
- **Componentes esenciales:**
  - Rol/Contexto: Define quién es el asistente
  - Instrucción: Qué debe hacer
  - Contexto: Información relevante
  - Formato: Cómo debe responder
  - Restricciones: Qué NO debe hacer
  
- **Ejemplo bancario:**
  ```
  Rol: Eres un asesor financiero de BNCR especializado en productos de ahorro
  Instrucción: Recomienda el mejor producto de ahorro para el cliente
  Contexto: Cliente de 28 años, ingreso $2000/mes, sin ahorros previos
  Formato: Respuesta en 3 párrafos con justificación
  Restricciones: No mencionar competidores, no dar asesoría de inversión
  ```

### 3. Técnicas de Prompting (15 min)

#### Zero-Shot Prompting
- **Definición:** Solicitar tarea sin ejemplos previos
- **Cuándo usar:** Tareas simples, respuestas generales
- **Ejemplo:** "Explica qué es una cuenta de ahorros"
- **Limitaciones:** Menos preciso para tareas complejas

#### Few-Shot Prompting
- **Definición:** Proporcionar 2-5 ejemplos antes de la tarea real
- **Cuándo usar:** Formato específico, tono consistente
- **Ejemplo:** Clasificación de consultas bancarias
- **Ventaja:** Mejora precisión en 30-50%

#### Chain-of-Thought (CoT)
- **Definición:** Solicitar razonamiento paso a paso
- **Cuándo usar:** Cálculos, decisiones complejas
- **Ejemplo:** Evaluación de elegibilidad para préstamos
- **Frase clave:** "Piensa paso a paso"

#### Self-Consistency
- **Definición:** Generar múltiples respuestas y seleccionar la más común
- **Cuándo usar:** Alta precisión requerida
- **Costo:** 3-5x más tokens

### 4. Patrones de Prompts para Banca (10 min)

#### Patrón 1: Clasificación de Intenciones
```
Clasifica la siguiente consulta en una de estas categorías:
- Consulta de saldo
- Transferencia
- Problema técnico
- Información de productos
- Reclamo

Consulta: {user_input}
Categoría:
```

#### Patrón 2: Extracción de Información
```
Extrae la siguiente información de la consulta del cliente:
- Tipo de producto de interés
- Monto aproximado
- Plazo deseado
- Urgencia (alta/media/baja)

Consulta: {user_input}
Información extraída (JSON):
```

#### Patrón 3: Generación de Respuestas Personalizadas
```
Genera una respuesta personalizada para el cliente considerando:
- Historial: {customer_history}
- Consulta actual: {current_query}
- Productos disponibles: {available_products}

Respuesta (tono profesional, máximo 150 palabras):
```

### 5. Mejores Prácticas (5 min)

1. **Claridad sobre creatividad:** Ser específico reduce ambigüedad
2. **Iteración:** Refinar prompts basado en resultados
3. **Temperatura adecuada:** 
   - 0-0.3: Tareas determinísticas (clasificación, extracción)
   - 0.7-0.9: Tareas creativas (redacción, ideas)
4. **Validación:** Siempre validar outputs críticos
5. **Versionado:** Mantener historial de prompts efectivos

## Demostración en Vivo (30 min)

### Demo 1: Evolución de un Prompt (10 min)
- Mostrar prompt básico con resultado mediocre
- Iterar agregando contexto, ejemplos, formato
- Comparar resultados lado a lado

### Demo 2: Few-Shot para Clasificación (10 min)
- Clasificar consultas bancarias sin ejemplos (baseline)
- Agregar 3 ejemplos y mostrar mejora
- Métricas: precisión antes/después

### Demo 3: Chain-of-Thought para Cálculos (10 min)
- Calcular elegibilidad de préstamo sin CoT
- Mismo cálculo con "piensa paso a paso"
- Mostrar razonamiento transparente

## Transición al Lab (5 min)

En el Lab 06 practicarán:
- Diseñar prompts para casos reales de BNCR
- Implementar templates reutilizables
- Comparar técnicas de prompting
- Medir y optimizar resultados

## Script de Diálogo (Puntos Clave)

**Apertura:**
"Bienvenidos a la Clase 6. Hoy hablaremos de Prompt Engineering, una habilidad fundamental que puede mejorar dramáticamente los resultados de sus aplicaciones de IA sin necesidad de reentrenar modelos o cambiar infraestructura. En BNCR, un prompt bien diseñado puede ser la diferencia entre un chatbot que frustra a los clientes y uno que los deleita."

**Transición a Anatomía:**
"Antes de ver técnicas avanzadas, necesitamos entender qué hace que un prompt sea efectivo. Piensen en un prompt como una receta de cocina: si falta un ingrediente clave, el resultado será impredecible."

**Introducción a Few-Shot:**
"Imaginen que están entrenando a un nuevo empleado. ¿Le dan solo instrucciones abstractas, o le muestran ejemplos concretos? Few-shot prompting es exactamente eso: enseñar con ejemplos."

**Sobre Chain-of-Thought:**
"Cuando un cliente pregunta si califica para un préstamo, no queremos solo un 'sí' o 'no'. Queremos transparencia. Chain-of-thought nos permite ver el razonamiento del modelo, lo cual es crítico para cumplimiento regulatorio."

**Cierre:**
"El prompt engineering no es magia, es ingeniería. Requiere experimentación, medición y refinamiento continuo. En el lab de hoy, pondrán en práctica todo lo que hemos visto con casos reales de BNCR."

## Recursos Adicionales

- OpenAI Prompt Engineering Guide
- Azure OpenAI Best Practices
- BNCR Internal Prompt Library (a crear)

## Notas para el Instructor

- Tener ejemplos de prompts malos y buenos preparados
- Mostrar métricas reales de mejora (si están disponibles)
- Enfatizar seguridad: no incluir datos sensibles en prompts
- Recordar límites de tokens (contexto)
- Mencionar costos: prompts más largos = más tokens

