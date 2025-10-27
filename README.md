# GenAI Applied to Banking - Azure OpenAI Labs

**Course:** Generative AI Applied to Banking with Azure  
**Institution:** Banco Nacional de Costa Rica (BNCR)  
**Duration:** 20 sessions (60 hours total)  
**Schedule:** Tuesday - Friday, 10:00 AM - 1:00 PM (CR Time)  
**Dates:** October 21 - November 21, 2025

---

## 📚 Course Overview

This repository contains hands-on laboratory exercises for learning Generative AI technologies applied to the banking sector using Microsoft Azure services. The course covers everything from foundational concepts to production-ready applications.

### **Learning Objectives**

By the end of this course, students will be able to:

- ✅ Understand foundational concepts of Generative AI and Large Language Models
- ✅ Implement Azure OpenAI Service in banking use cases
- ✅ Build RAG (Retrieval Augmented Generation) systems for document analysis
- ✅ Develop AI-powered applications for fraud detection, customer service, and compliance
- ✅ Deploy production-ready AI solutions using Azure services
- ✅ Apply best practices for security, cost optimization, and responsible AI

---

## 🏗️ Repository Structure

\`\`\`
GenAI-to-BNCR/
├── labs/                    # Laboratory exercises (Lab 05-20)
│   ├── lab05/              # First Steps with Azure OpenAI
│   ├── lab06/              # Prompt Engineering Fundamentals
│   ├── lab07/              # Advanced Prompting Techniques
│   ├── lab08/              # Function Calling & Tools
│   ├── lab09/              # Embeddings & Semantic Search
│   ├── lab10/              # RAG: Document Q&A System
│   ├── lab11/              # RAG: Multi-Document Analysis
│   ├── lab12/              # RAG: Production Optimization
│   ├── lab13/              # Computer Vision for Banking
│   ├── lab14/              # Form Processing & OCR
│   ├── lab15/              # Sentiment Analysis & NLP
│   ├── lab16/              # Building AI APIs with Functions
│   ├── lab17/              # Deploying Web Applications
│   ├── lab18/              # Fraud Detection System
│   ├── lab19/              # Compliance & Regulatory Reporting
│   └── lab20/              # Final Project: Integrated Banking AI
├── datasets/               # Sample datasets for exercises
│   └── banking/           # Banking-specific datasets
├── docs/                   # Documentation and diagrams
│   └── diagrams/          # Infrastructure diagrams
├── utils/                  # Utility functions and helpers
├── .github/workflows/      # CI/CD pipelines
├── .gitignore             # Git ignore file
├── requirements.txt        # Python dependencies
└── README.md              # This file
\`\`\`

---

## 🚀 Getting Started

### **Prerequisites**

- Python 3.11+
- Jupyter Lab or Jupyter Notebook
- Azure subscription with access to:
  - Azure OpenAI Service
  - Azure AI Search
  - Azure SQL Database
  - Azure Storage Account
  - Azure AI Services

### **Installation**

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/manularrea/GenAI-to-BNCR.git
   cd GenAI-to-BNCR
   \`\`\`

2. **Create a virtual environment:**
   \`\`\`bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   \`\`\`

3. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Configure Azure credentials:**
   
   Create a \`.env\` file in the root directory:
   \`\`\`env
   # Azure OpenAI
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_API_KEY=your-api-key
   AZURE_OPENAI_DEPLOYMENT_GPT4=gpt-4
   AZURE_OPENAI_DEPLOYMENT_GPT35=gpt-35-turbo
   AZURE_OPENAI_DEPLOYMENT_EMBEDDING=text-embedding-ada-002
   
   # Azure AI Search
   AZURE_SEARCH_ENDPOINT=https://your-search.search.windows.net
   AZURE_SEARCH_API_KEY=your-search-key
   
   # Azure SQL Database
   AZURE_SQL_CONNECTION_STRING=your-connection-string
   
   # Azure Storage
   AZURE_STORAGE_CONNECTION_STRING=your-storage-connection-string
   \`\`\`

5. **Launch Jupyter Lab:**
   \`\`\`bash
   jupyter lab
   \`\`\`

---

## 📖 Course Schedule

### **Module 1: Introduction to GenAI (Sessions 1-4)**
- Session 1-3: Theoretical foundations (no labs)
- Session 4: Introduction to Azure OpenAI (demos only)

### **Module 2: Azure OpenAI Fundamentals (Sessions 5-9)**
- **Lab 05:** First Steps with Azure OpenAI
- **Lab 06:** Prompt Engineering Fundamentals
- **Lab 07:** Advanced Prompting Techniques
- **Lab 08:** Function Calling & Tools
- **Lab 09:** Embeddings & Semantic Search

### **Module 3: RAG Systems (Sessions 10-12)**
- **Lab 10:** RAG: Document Q&A System
- **Lab 11:** RAG: Multi-Document Analysis
- **Lab 12:** RAG: Production Optimization

### **Module 4: Azure AI Services (Sessions 13-15)**
- **Lab 13:** Computer Vision for Banking
- **Lab 14:** Form Processing & OCR
- **Lab 15:** Sentiment Analysis & NLP

### **Module 5: Production Applications (Sessions 16-20)**
- **Lab 16:** Building AI APIs with Azure Functions
- **Lab 17:** Deploying Web Applications
- **Lab 18:** Fraud Detection System
- **Lab 19:** Compliance & Regulatory Reporting
- **Lab 20:** Final Project: Integrated Banking AI

---

## 🏦 Banking Use Cases Covered

1. **Customer Service Automation**
   - Intelligent chatbots with context awareness
   - Multi-language support
   - Sentiment analysis

2. **Fraud Detection**
   - Transaction pattern analysis
   - Anomaly detection
   - Real-time alerts

3. **Document Processing**
   - Loan application analysis
   - KYC (Know Your Customer) automation
   - Contract review

4. **Regulatory Compliance**
   - Automated reporting to SUGEF
   - AML (Anti-Money Laundering) monitoring
   - Risk assessment

5. **Credit Scoring**
   - Alternative data analysis
   - Explainable AI models
   - Risk profiling

---

## 🛠️ Technologies Used

### **Azure Services**
- Azure OpenAI Service (GPT-4, GPT-3.5, Embeddings)
- Azure AI Search (Semantic search, Vector search)
- Azure AI Services (Computer Vision, Form Recognizer, Language)
- Azure SQL Database
- Azure Storage Account
- Azure Functions
- Azure App Service
- Azure Key Vault

### **Python Libraries**
- \`openai\` - Azure OpenAI SDK
- \`langchain\` - LLM application framework
- \`azure-search-documents\` - Azure AI Search SDK
- \`azure-ai-formrecognizer\` - Form processing
- \`pandas\` - Data manipulation
- \`numpy\` - Numerical computing
- \`matplotlib\` / \`seaborn\` - Data visualization
- \`fastapi\` - API development
- \`streamlit\` - Web app development

---

## 📊 Datasets

All datasets used in this course are either:
- Publicly available open-source datasets
- Synthetic data generated for educational purposes
- Anonymized and compliant with data protection regulations

**Available datasets:**
- \`customer_transactions.csv\` - Sample banking transactions
- \`loan_applications.json\` - Loan application documents
- \`customer_support_tickets.csv\` - Support conversation history
- \`regulatory_documents/\` - Sample compliance documents
- \`fraud_patterns.csv\` - Historical fraud cases (synthetic)

---

## 🔒 Security & Best Practices

### **Credential Management**
- ✅ Never commit \`.env\` files or API keys to the repository
- ✅ Use Azure Key Vault for production secrets
- ✅ Rotate API keys regularly
- ✅ Use managed identities when possible

### **Data Privacy**
- ✅ All datasets are anonymized
- ✅ No real customer data is used
- ✅ Comply with GDPR and local regulations

### **Cost Optimization**
- ✅ Use GPT-3.5 for development and testing
- ✅ Implement caching strategies
- ✅ Monitor token usage
- ✅ Set spending limits

### **Responsible AI**
- ✅ Implement content filtering
- ✅ Monitor for bias
- ✅ Provide transparency to end users
- ✅ Human oversight for critical decisions

---

## 📈 Infrastructure Overview

Each lab includes a diagram showing the Azure infrastructure being used. Here's the overall architecture:

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                     Students (Jupyter Lab)                   │
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
                       ├─────────► Azure SQL Database
                       │            └─ Structured Data
                       │
                       ├─────────► Azure Storage Account
                       │            └─ Documents & Files
                       │
                       ├─────────► Azure AI Services
                       │            ├─ Computer Vision
                       │            ├─ Form Recognizer
                       │            └─ Language Service
                       │
                       └─────────► Azure Key Vault
                                    └─ Secrets Management
\`\`\`

---

## 🎓 Learning Path

### **Beginner (Sessions 5-9)**
Start with basic Azure OpenAI interactions, learn prompt engineering, and understand embeddings.

### **Intermediate (Sessions 10-15)**
Build RAG systems, integrate multiple Azure AI services, and process complex documents.

### **Advanced (Sessions 16-20)**
Deploy production applications, implement fraud detection, and create integrated banking solutions.

---

## 🤝 Contributing

This repository is maintained for educational purposes. If you find issues or have suggestions:

1. Open an issue describing the problem or enhancement
2. Submit a pull request with your proposed changes
3. Ensure all code follows PEP 8 style guidelines
4. Add tests for new functionality

---

## 📞 Support

For questions or issues during the course:

- **Instructor:** Manuela Larrea Gomez
- **Institution:** Banco Nacional de Costa Rica (BNCR)
- **GitHub Issues:** Use the Issues tab for technical questions

---

## 📄 License

This educational material is provided for the exclusive use of BNCR course participants. All rights reserved.

---

## 🙏 Acknowledgments

- Microsoft Azure for providing cloud infrastructure
- OpenAI for foundational AI models
- BNCR for supporting AI education and innovation
- All open-source contributors whose libraries make this course possible

---

**Last Updated:** October 2025  
**Version:** 1.0.0
