# Generative AI for Banking Sector - BNCR Training Course

![Course Banner](https://img.shields.io/badge/Azure-OpenAI-blue) ![Python](https://img.shields.io/badge/Python-3.11-green) ![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

**Course:** Generative AI Applied to Banking with Azure  
**Institution:** Banco Nacional de Costa Rica (BNCR)  
**Duration:** 20 sessions (60 hours total)  
**Schedule:** Tuesday - Friday, 10:00 AM - 1:00 PM (CR Time)  
**Dates:** October 21 - November 21, 2025  
**Instructor:** Manuela Larrea (manuela.larrea@idataglobal.com)

---

## 📋 Course Overview

This repository contains comprehensive training materials for implementing Generative AI solutions in the banking sector using Microsoft Azure services. The course combines theoretical foundations with extensive hands-on practice, covering everything from basic concepts to production-ready applications.

### **Learning Objectives**

By the end of this course, participants will be able to:

1. ✅ Design and implement intelligent banking chatbots
2. ✅ Integrate Azure OpenAI with existing banking systems
3. ✅ Build RAG (Retrieval-Augmented Generation) systems for knowledge bases
4. ✅ Apply advanced prompt engineering techniques
5. ✅ Deploy GenAI solutions to production on Azure
6. ✅ Implement security, content moderation, and compliance
7. ✅ Optimize costs and performance of GenAI applications
8. ✅ Evaluate and continuously improve AI systems

---

## 🗂️ Repository Structure

```
GenAI-to-BNCR/
├── README.md                          # This file
├── INSTRUCTOR_GUIDE.md                # Complete guide for instructors
├── requirements.txt                   # Python dependencies
├── .env.example                       # Configuration template
├── .gitignore                        # Git ignore rules
│
├── datasets/                          # Banking sample data
│   ├── README.md
│   └── banking/
│       ├── banking_products.csv       # Banking products
│       ├── transactions.csv           # Sample transactions
│       └── banking_faq.csv           # Frequently asked questions
│
├── utils/                             # Shared utilities
│   ├── __init__.py
│   ├── azure_openai_helper.py        # Azure OpenAI client
│   └── infrastructure_diagrams.py     # Diagram generator
│
├── labs/                              # Laboratory notebooks
│   ├── lab05/                         # Azure OpenAI Basics
│   ├── lab06/                         # Prompt Engineering
│   ├── lab07/                         # Conversation Management
│   ├── lab08/                         # Function Calling
│   ├── lab09/                         # Embeddings & Semantic Search
│   ├── lab10/                         # RAG Implementation
│   ├── lab11/                         # Azure AI Search Integration
│   ├── lab12/                         # Content Moderation & Safety
│   ├── lab13/                         # Fine-tuning for Banking
│   ├── lab14/                         # Multimodal AI - Vision
│   ├── lab15/                         # Agent Frameworks & LangChain
│   ├── lab16/                         # Production Deployment
│   ├── lab17/                         # Testing & Evaluation
│   ├── lab18/                         # Ethics, Bias & Responsible AI
│   ├── lab19/                         # Cost Optimization
│   └── lab20/                         # Final Project
│
├── presentations/                     # Presentation materials
│   ├── MASTER_PRESENTATIONS_OUTLINE.md
│   └── class06-20/                   # Slides per class
│
└── scripts/                           # Utility scripts
    └── setup_environment.sh           # Initial setup
```

---

## 📖 Course Schedule

### **Module 1: Introduction to GenAI (Sessions 1-4)**
*Theoretical foundations - materials not included in this repository*

### **Module 2: Azure OpenAI Fundamentals (Sessions 5-9)**

| Session | Topic | Lab | Duration |
|---------|-------|-----|----------|
| **05** | First Steps with Azure OpenAI | Lab 05 | 3h |
| **06** | Prompt Engineering for Banking | Lab 06 | 3h |
| **07** | Advanced Conversation Management | Lab 07 | 3h |
| **08** | Function Calling & Tool Integration | Lab 08 | 3h |
| **09** | Embeddings & Semantic Search | Lab 09 | 3h |

### **Module 3: RAG & Knowledge Systems (Sessions 10-12)**

| Session | Topic | Lab | Duration |
|---------|-------|-----|----------|
| **10** | RAG (Retrieval-Augmented Generation) | Lab 10 | 3h |
| **11** | Azure AI Search Integration | Lab 11 | 3h |
| **12** | Content Moderation & Safety | Lab 12 | 3h |

### **Module 4: Advanced AI Capabilities (Sessions 13-15)**

| Session | Topic | Lab | Duration |
|---------|-------|-----|----------|
| **13** | Fine-tuning for Banking Domain | Lab 13 | 3h |
| **14** | Multimodal AI - Vision & Documents | Lab 14 | 3h |
| **15** | Agent Frameworks & LangChain | Lab 15 | 3h |

### **Module 5: Production & Best Practices (Sessions 16-20)**

| Session | Topic | Lab | Duration |
|---------|-------|-----|----------|
| **16** | Production Deployment on Azure | Lab 16 | 3h |
| **17** | Testing & Evaluation | Lab 17 | 3h |
| **18** | Ethics, Bias & Responsible AI | Lab 18 | 3h |
| **19** | Cost Optimization & Performance | Lab 19 | 3h |
| **20** | Final Project - Banking AI Assistant | Lab 20 | 3h |

---

## 🚀 Quick Start

### **Prerequisites**

- Python 3.11 or higher
- Jupyter Lab or VS Code with Jupyter extension
- Git installed
- Azure account with access to Azure OpenAI

### **Installation**

1. **Clone the repository:**
```bash
git clone https://github.com/manularrea/GenAI-to-BNCR.git
cd GenAI-to-BNCR
```

2. **Create virtual environment:**
```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your Azure OpenAI credentials
```

5. **Launch Jupyter Lab:**
```bash
jupyter lab
```

6. **Open first notebook:**
Navigate to `labs/lab05/lab05_azure_openai_basics.ipynb`

---

## 🔑 Azure OpenAI Configuration

### Get Credentials

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your Azure OpenAI resource
3. In "Keys and Endpoint", copy:
   - API Key
   - Endpoint
   - Deployment names

### Configure `.env`

```env
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Deployment Names
AZURE_OPENAI_GPT4_DEPLOYMENT=gpt-4
AZURE_OPENAI_GPT35_DEPLOYMENT=gpt-35-turbo
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

---

## 🏦 Banking Use Cases Covered

### 1. **Customer Service Chatbot**
- Answer product inquiries
- Handle information requests
- Intelligent escalation to human agents

### 2. **Loan Application Assistant**
- Assess eligibility
- Collect applicant information
- Generate pre-approvals

### 3. **Document Search System**
- Internal policies and procedures
- Product documentation
- Regulations and compliance

### 4. **Document Analysis**
- Check processing
- Form data extraction
- Financial statement analysis

### 5. **Fraud Detection**
- Transaction pattern analysis
- Suspicious activity identification
- Real-time alerts

---

## 💻 Technologies Used

### **Azure Services**
- **Azure OpenAI Service** - GPT-4, GPT-3.5, Embeddings
- **Azure AI Search** - Enterprise search capabilities
- **Azure Content Safety** - Content moderation
- **Azure API Management** - API governance

### **Python Libraries**
- `openai` - Official OpenAI client
- `python-dotenv` - Environment variable management
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `langchain` - Agent framework (Labs 15+)
- `chromadb` - Vector database (Lab 10)
- `azure-ai-search` - Azure Cognitive Search (Lab 11)

---

## 🔒 Security & Best Practices

### **Implemented Best Practices**

✅ **Never** include sensitive data in prompts  
✅ **Always** use environment variables for credentials  
✅ **Implement** content moderation  
✅ **Validate** all user inputs  
✅ **Log** all interactions for auditing  
✅ **Encrypt** data in transit and at rest  
✅ **Limit** access based on roles  
✅ **Monitor** usage and costs continuously

### **Banking Compliance**

- **GDPR** - Personal data protection
- **PCI DSS** - Card data security
- **SOC 2** - Security controls
- **Local regulations** - Costa Rica banking laws

---

## 💰 Cost Estimation

### Azure OpenAI Pricing (Approximate)

| Model | Input (1K tokens) | Output (1K tokens) | Typical Lab Cost |
|-------|-------------------|--------------------| -----------------|
| GPT-4 | $0.03 | $0.06 | ~$2-5 |
| GPT-3.5 Turbo | $0.0005 | $0.0015 | ~$0.50-1 |
| Embeddings | $0.0001 | N/A | ~$0.10-0.50 |

**Estimated cost per student for entire course:** $50-100 USD

### Cost Optimization

- Use GPT-3.5 for development and testing
- Implement caching for repeated queries
- Limit max_tokens in responses
- Use batch processing when possible
- Monitor usage with Azure Cost Management

---

## 📚 Additional Resources

### **Official Documentation**
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [LangChain Documentation](https://python.langchain.com/)

### **Tutorials & Guides**
- [Azure OpenAI Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [RAG Best Practices](https://python.langchain.com/docs/use_cases/question_answering/)

### **Community**
- [Azure OpenAI Samples](https://github.com/Azure-Samples/openai)
- [OpenAI Community Forum](https://community.openai.com/)
- [Stack Overflow - Azure OpenAI](https://stackoverflow.com/questions/tagged/azure-openai)

---

## 🐛 Troubleshooting

### Error: "Authentication failed"
```bash
# Verify .env has correct credentials
cat .env
# Verify variables are loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('AZURE_OPENAI_API_KEY'))"
```

### Error: "Rate limit exceeded"
```bash
# Wait 60 seconds and retry
# Or configure retry logic in code
```

### Error: "Module not found"
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Notebook won't connect
```bash
# Verify kernel
jupyter kernelspec list
# Reinstall kernel if needed
python -m ipykernel install --user --name=venv
```

---

## 📈 Infrastructure Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  Students (Jupyter Lab)                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ├─────────► Azure OpenAI Service
                       │            ├─ GPT-4 (10K TPM)
                       │            ├─ GPT-3.5 (60K TPM)
                       │            └─ Embeddings (60K TPM)
                       │
                       ├─────────► Azure AI Search
                       │            └─ Vector + Semantic Search
                       │
                       ├─────────► Azure Content Safety
                       │            └─ Content Moderation
                       │
                       └─────────► Azure Key Vault
                                    └─ Secrets Management
```

---

## 🤝 Contributing

This repository is specific to the BNCR course. For suggestions or improvements:

1. Create an issue describing the improvement
2. Contact instructor: manuela.larrea@idataglobal.com
3. For major changes, discuss with BNCR team first

---

## 📝 License

This material is property of **iData Global** and is licensed exclusively for use by **Banco Nacional de Costa Rica (BNCR)** for internal training purposes.

**Prohibited:**
- Distribution outside BNCR
- Commercial use without authorization
- Modification without approval

---

## 👥 Contact

**Lead Instructor:**  
Manuela Larrea  
Email: manuela.larrea@idataglobal.com

**Organization:**  
iData Global  
Website: https://idataglobal.com

**Client:**  
Banco Nacional de Costa Rica (BNCR)

---

## 🎉 Acknowledgments

Special thanks to:
- BNCR team for their collaboration
- Microsoft Azure for the platform
- OpenAI for language models
- Open-source community for tools

---

## 📅 Version History

### v1.0.0 (2024-01-27)
- ✅ Complete repository structure
- ✅ 16 laboratory notebooks (Labs 05-20)
- ✅ Shared utilities and helpers
- ✅ Banking sample datasets
- ✅ Complete documentation
- ✅ Instructor guide
- ✅ Presentation templates

---

## 🚀 Next Steps

After completing this course, participants can:

1. **Implement** GenAI solutions in production at BNCR
2. **Explore** additional specific use cases
3. **Optimize** existing systems with AI
4. **Train** other internal teams
5. **Innovate** with new GenAI applications

---

**Welcome to the future of banking with Generative AI!** 🚀🏦

**Last Updated:** January 2025  
**Version:** 1.0.0

