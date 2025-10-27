# Master Outline - BNCR GenAI Course Presentations (Classes 6-20)

## Overview
This document contains the structured outlines for all presentation materials for the BNCR Generative AI training course.

---

## Class 06: Prompt Engineering para Aplicaciones Bancarias
**Duration:** 45 min presentation + 30 min demo + Lab 06 (1.5 hours)

### Key Messages
1. Prompt engineering can improve accuracy by 40-60% without model changes
2. Structure matters: Role, Instruction, Context, Format, Constraints
3. Few-shot learning dramatically improves consistency
4. Chain-of-thought enables transparent reasoning for compliance

### Slides Structure (10-12 slides)
1. Title: Prompt Engineering para Aplicaciones Bancarias
2. Why Prompt Engineering Matters in Banking
3. Anatomy of an Effective Prompt
4. Zero-Shot vs Few-Shot vs Chain-of-Thought
5. Banking Use Case: Customer Intent Classification
6. Banking Use Case: Loan Eligibility Assessment
7. Prompt Templates for BNCR
8. Best Practices and Common Pitfalls
9. Live Demo Preview
10. Transition to Lab 06

---

## Class 07: Gestión Avanzada de Conversaciones
**Duration:** 45 min presentation + 30 min demo + Lab 07 (1.5 hours)

### Key Messages
1. Stateful conversations require proper context management
2. Sentiment detection enables proactive escalation
3. Conversation summarization improves handoffs
4. Multi-turn dialogues need intent tracking

### Slides Structure (10-12 slides)
1. Title: Gestión Avanzada de Conversaciones
2. The Challenge of Stateful Conversations
3. Conversation State Architecture
4. Intent Detection and Classification
5. Sentiment Analysis for Banking
6. Escalation Logic and Human Handoff
7. Conversation Summarization
8. Quality Metrics and Monitoring
9. Banking Chatbot Demo
10. Transition to Lab 07

---

## Class 08: Function Calling e Integración de Herramientas
**Duration:** 45 min presentation + 30 min demo + Lab 08 (1.5 hours)

### Key Messages
1. Function calling enables AI to interact with banking systems
2. Proper schema design is critical for reliability
3. Security and validation are paramount
4. Multi-step function calls handle complex workflows

### Slides Structure (10-12 slides)
1. Title: Function Calling e Integración de Herramientas
2. What is Function Calling?
3. Function Calling Architecture
4. Defining Function Schemas
5. Banking Functions: Balance, Transfer, History
6. Security Considerations
7. Error Handling and Validation
8. Multi-Step Function Calls
9. Production Patterns
10. Transition to Lab 08

---

## Class 09: Embeddings y Búsqueda Semántica
**Duration:** 45 min presentation + 30 min demo + Lab 09 (1.5 hours)

### Key Messages
1. Embeddings convert text to numerical vectors
2. Semantic search understands meaning, not just keywords
3. Vector similarity enables intelligent document retrieval
4. Critical for building knowledge bases

### Slides Structure (10-12 slides)
1. Title: Embeddings y Búsqueda Semántica
2. The Limitation of Keyword Search
3. What are Embeddings?
4. Azure OpenAI Embeddings API
5. Vector Similarity and Distance Metrics
6. Building a Banking FAQ Search
7. Document Similarity Use Cases
8. Performance and Cost Considerations
9. Demo: Semantic Search in Action
10. Transition to Lab 09

---

## Class 10: RAG (Retrieval-Augmented Generation)
**Duration:** 45 min presentation + 30 min demo + Lab 10 (1.5 hours)

### Key Messages
1. RAG combines retrieval with generation for accurate responses
2. Solves the "hallucination" problem with grounded information
3. Document chunking strategy impacts quality
4. Essential for banking policy and compliance documents

### Slides Structure (10-12 slides)
1. Title: RAG (Retrieval-Augmented Generation)
2. The Problem: LLMs Don't Know Your Data
3. RAG Architecture Overview
4. Document Processing Pipeline
5. Chunking Strategies
6. Vector Databases (Pinecone, Chroma, FAISS)
7. RAG for Banking Policies
8. Evaluation and Quality Metrics
9. Demo: Banking Knowledge Base
10. Transition to Lab 10

---

## Class 11: Azure AI Search Integration
**Duration:** 45 min presentation + 30 min demo + Lab 11 (1.5 hours)

### Key Messages
1. Azure AI Search provides enterprise-grade search capabilities
2. Hybrid search combines keyword and semantic approaches
3. Filtering and faceting enable precise retrieval
4. Native integration with Azure OpenAI

### Slides Structure (10-12 slides)
1. Title: Azure AI Search Integration
2. Enterprise Search Requirements
3. Azure AI Search Architecture
4. Indexing Banking Documents
5. Hybrid Search: Best of Both Worlds
6. Filtering, Faceting, and Ranking
7. Integration with Azure OpenAI
8. Security and Access Control
9. Demo: Banking Document Search
10. Transition to Lab 11

---

## Class 12: Moderación de Contenido y Seguridad
**Duration:** 45 min presentation + 30 min demo + Lab 12 (1.5 hours)

### Key Messages
1. Content moderation is mandatory for customer-facing AI
2. Azure Content Safety detects harmful content
3. PII detection prevents data leaks
4. Jailbreak prevention protects system integrity

### Slides Structure (10-12 slides)
1. Title: Moderación de Contenido y Seguridad
2. Why Content Safety Matters in Banking
3. Azure Content Safety API
4. Detecting Harmful Content
5. PII Detection and Redaction
6. Jailbreak Prevention Techniques
7. Compliance and Audit Logging
8. Building a Safety Layer
9. Demo: Content Moderation Pipeline
10. Transition to Lab 12

---

## Class 13: Fine-tuning para el Dominio Bancario
**Duration:** 45 min presentation + 30 min demo + Lab 13 (1.5 hours)

### Key Messages
1. Fine-tuning customizes models for specific domains
2. When to fine-tune vs prompt engineering
3. Data quality is more important than quantity
4. Cost-benefit analysis is essential

### Slides Structure (10-12 slides)
1. Title: Fine-tuning para el Dominio Bancario
2. Fine-tuning vs Prompt Engineering
3. When to Fine-tune
4. Preparing Training Data
5. Azure OpenAI Fine-tuning Process
6. Evaluation Metrics
7. Cost-Benefit Analysis
8. Banking Domain Examples
9. Demo: Fine-tuned Model Comparison
10. Transition to Lab 13

---

## Class 14: IA Multimodal - Visión y Documentos
**Duration:** 45 min presentation + 30 min demo + Lab 14 (1.5 hours)

### Key Messages
1. GPT-4 Vision processes images and documents
2. OCR and data extraction from banking forms
3. Chart and graph understanding
4. Streamlines document processing workflows

### Slides Structure (10-12 slides)
1. Title: IA Multimodal - Visión y Documentos
2. Beyond Text: Multimodal AI
3. GPT-4 Vision Capabilities
4. Banking Document Processing
5. Check and Form Analysis
6. Chart and Graph Understanding
7. OCR vs Vision Models
8. Production Considerations
9. Demo: Processing Banking Documents
10. Transition to Lab 14

---

## Class 15: Frameworks de Agentes y LangChain
**Duration:** 45 min presentation + 30 min demo + Lab 15 (1.5 hours)

### Key Messages
1. Agent frameworks enable autonomous AI systems
2. LangChain simplifies complex AI workflows
3. Agents can use multiple tools dynamically
4. Memory management enables context retention

### Slides Structure (10-12 slides)
1. Title: Frameworks de Agentes y LangChain
2. What are AI Agents?
3. LangChain Architecture
4. Chains, Agents, and Tools
5. Memory Management
6. Banking Agent Use Cases
7. Building a Research Agent
8. Production Considerations
9. Demo: Multi-Tool Banking Agent
10. Transition to Lab 15

---

## Class 16: Despliegue en Producción en Azure
**Duration:** 45 min presentation + 30 min demo + Lab 16 (1.5 hours)

### Key Messages
1. Production deployment requires proper architecture
2. API Management provides security and governance
3. Monitoring and logging are essential
4. Cost optimization through proper configuration

### Slides Structure (10-12 slides)
1. Title: Despliegue en Producción en Azure
2. Production Architecture Overview
3. Azure Deployment Options
4. API Management and Security
5. Authentication and Authorization
6. Monitoring and Logging
7. Rate Limiting and Quotas
8. Cost Optimization Strategies
9. Demo: Deploying to Azure
10. Transition to Lab 16

---

## Class 17: Testing y Evaluación
**Duration:** 45 min presentation + 30 min demo + Lab 17 (1.5 hours)

### Key Messages
1. LLM evaluation requires specialized metrics
2. Automated testing catches regressions
3. Human evaluation remains critical
4. A/B testing validates improvements

### Slides Structure (10-12 slides)
1. Title: Testing y Evaluación
2. The Challenge of Evaluating LLMs
3. Evaluation Metrics (BLEU, ROUGE, etc.)
4. Automated Testing Strategies
5. Human Evaluation Frameworks
6. A/B Testing for AI Systems
7. Regression Detection
8. Building a Test Suite
9. Demo: Evaluation Dashboard
10. Transition to Lab 17

---

## Class 18: Ética, Sesgo e IA Responsable
**Duration:** 45 min presentation + 30 min demo + Lab 18 (1.5 hours)

### Key Messages
1. AI bias can perpetuate discrimination
2. Fairness metrics quantify bias
3. Transparency builds trust
4. Regulatory compliance is mandatory

### Slides Structure (10-12 slides)
1. Title: Ética, Sesgo e IA Responsable
2. Why Responsible AI Matters in Banking
3. Types of AI Bias
4. Fairness Metrics
5. Transparency and Explainability
6. Microsoft Responsible AI Principles
7. Regulatory Compliance (GDPR, etc.)
8. Building Ethical AI Systems
9. Demo: Bias Audit
10. Transition to Lab 18

---

## Class 19: Optimización de Costos y Rendimiento
**Duration:** 45 min presentation + 30 min demo + Lab 19 (1.5 hours)

### Key Messages
1. Token usage directly impacts costs
2. Caching reduces redundant API calls
3. Model selection affects both cost and quality
4. Monitoring enables optimization

### Slides Structure (10-12 slides)
1. Title: Optimización de Costos y Rendimiento
2. Understanding Azure OpenAI Pricing
3. Token Usage Optimization
4. Caching Strategies
5. Model Selection: GPT-4 vs GPT-3.5
6. Batch Processing
7. Performance Monitoring
8. Cost Allocation and Tracking
9. Demo: Cost Optimization Dashboard
10. Transition to Lab 19

---

## Class 20: Proyecto Final - Asistente Bancario IA
**Duration:** 3 hours (project work session)

### Key Messages
1. Integrate all learned concepts
2. Focus on production-ready implementation
3. Demonstrate business value
4. Present and defend design decisions

### Slides Structure (8-10 slides)
1. Title: Proyecto Final - Asistente Bancario IA
2. Project Requirements
3. Architecture Guidelines
4. Evaluation Criteria
5. Timeline and Milestones
6. Resources and Support
7. Presentation Guidelines
8. Q&A and Project Kickoff

---

## General Presentation Guidelines

### Visual Design
- BNCR branding colors (blue, white, green accents)
- Clean, professional layouts
- Minimal text per slide (max 5 bullet points)
- High-quality diagrams and screenshots
- Consistent fonts and styling

### Content Principles
- Start with business value, then technical details
- Use banking-specific examples throughout
- Include real metrics and data where possible
- Balance theory with practical application
- End each section with key takeaways

### Delivery Notes
- Allocate time for questions
- Prepare backup slides for deep dives
- Have demo environment ready
- Provide handouts/references
- Record sessions for future reference

