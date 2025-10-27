"""
Infrastructure Diagram Templates
Provides ASCII diagrams showing Azure infrastructure for each lab
"""


def get_lab05_diagram():
    """Lab 05: First Steps with Azure OpenAI"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                    LAB 05 - AZURE INFRASTRUCTURE                         ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (Jupyter Notebook)                            │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ HTTPS Request
                                 │ (API Key in Header)
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │                            │
                    │  ┌──────────────────────┐  │
                    │  │  GPT-3.5 Turbo       │  │
                    │  │  (60K TPM)           │  │
                    │  └──────────────────────┘  │
                    │                            │
                    │  ┌──────────────────────┐  │
                    │  │  GPT-4               │  │
                    │  │  (10K TPM)           │  │
                    │  └──────────────────────┘  │
                    └────────────────────────────┘

📊 Resources Used:
  • Azure OpenAI Service (East US 2)
  • GPT-3.5 Turbo deployment
  • GPT-4 deployment (optional)

💰 Estimated Cost: ~$0.50 per lab session
"""


def get_lab06_07_diagram():
    """Lab 06-07: Prompt Engineering"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                  LAB 06-07 - AZURE INFRASTRUCTURE                        ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (Jupyter Notebook)                            │
│                                                                           │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────────────┐ │
│  │ System Prompts  │  │  User Messages   │  │  Temperature Control   │ │
│  └─────────────────┘  └──────────────────┘  └────────────────────────┘ │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ Optimized Prompts
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │                            │
                    │  ┌──────────────────────┐  │
                    │  │  GPT-3.5 Turbo       │  │
                    │  │  • Few-shot learning │  │
                    │  │  • Chain-of-thought  │  │
                    │  └──────────────────────┘  │
                    └────────────────────────────┘

📊 Resources Used:
  • Azure OpenAI Service
  • GPT-3.5 Turbo (primary)
  • GPT-4 (comparison testing)

💰 Estimated Cost: ~$1.00 per lab session
"""


def get_lab08_diagram():
    """Lab 08: Function Calling"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                    LAB 08 - AZURE INFRASTRUCTURE                         ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (Jupyter Notebook)                            │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Python Functions (Tools)                                        │   │
│  │  • get_account_balance()                                         │   │
│  │  • get_transaction_history()                                     │   │
│  │  • transfer_funds()                                              │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ Function Definitions + User Query
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │                            │
                    │  ┌──────────────────────┐  │
                    │  │  GPT-4               │  │
                    │  │  (Function Calling)  │  │
                    │  └──────────────────────┘  │
                    └────────────────────────────┘
                                 │
                                 │ Function Call Instructions
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     Local Function Execution                             │
│                     (Simulated Banking API)                              │
└─────────────────────────────────────────────────────────────────────────┘

📊 Resources Used:
  • Azure OpenAI Service (GPT-4)
  • Local Python functions (no external APIs)

💰 Estimated Cost: ~$2.00 per lab session
"""


def get_lab09_diagram():
    """Lab 09: Embeddings & Semantic Search"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                    LAB 09 - AZURE INFRASTRUCTURE                         ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (Jupyter Notebook)                            │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Banking Documents (Local)                                       │   │
│  │  • Product descriptions                                          │   │
│  │  • FAQ documents                                                 │   │
│  │  • Policy texts                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ Text chunks
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │                            │
                    │  ┌──────────────────────┐  │
                    │  │  text-embedding-ada  │  │
                    │  │  (1536 dimensions)   │  │
                    │  └──────────────────────┘  │
                    └────────────────────────────┘
                                 │
                                 │ Embedding vectors
                                 ▼
                    ┌────────────────────────────┐
                    │   Local Vector Store       │
                    │   (NumPy / In-Memory)      │
                    │                            │
                    │  • Cosine similarity       │
                    │  • Semantic search         │
                    └────────────────────────────┘

📊 Resources Used:
  • Azure OpenAI Embeddings
  • Local vector storage (no Azure AI Search yet)

💰 Estimated Cost: ~$0.30 per lab session
"""


def get_lab10_11_12_diagram():
    """Lab 10-12: RAG Systems"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                  LAB 10-12 - AZURE INFRASTRUCTURE                        ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (Jupyter Notebook)                            │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ User Query
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │   (Generate Query          │
                    │    Embedding)              │
                    └────────────┬───────────────┘
                                 │
                                 │ Query Vector
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure AI Search          │
                    │                            │
                    │  • Vector Search           │
                    │  • Semantic Ranking        │
                    │  • 2GB Storage (Basic)     │
                    └────────────┬───────────────┘
                                 │
                                 │ Retrieved Documents
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │   (Generate Answer with    │
                    │    Context)                │
                    └────────────┬───────────────┘
                                 │
                                 │ Final Answer
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure Storage Account    │
                    │   (Document Storage)       │
                    │   • Blob Storage           │
                    │   • 500GB capacity         │
                    └────────────────────────────┘

📊 Resources Used:
  • Azure OpenAI (Embeddings + GPT-3.5/4)
  • Azure AI Search (Basic tier)
  • Azure Storage Account

💰 Estimated Cost: ~$3.00 per lab session
"""


def get_lab13_14_15_diagram():
    """Lab 13-15: Azure AI Services"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                  LAB 13-15 - AZURE INFRASTRUCTURE                        ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (Jupyter Notebook)                            │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Input Data                                                      │   │
│  │  • Images (ID cards, checks)                                     │   │
│  │  • Documents (forms, contracts)                                  │   │
│  │  • Text (customer reviews, support tickets)                      │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ├─────────► Computer Vision API
                                 │           • Object detection
                                 │           • OCR
                                 │           • Face verification
                                 │
                                 ├─────────► Form Recognizer API
                                 │           • Document extraction
                                 │           • Table recognition
                                 │           • Key-value pairs
                                 │
                                 └─────────► Language Service API
                                             • Sentiment analysis
                                             • Entity recognition
                                             • Key phrase extraction

                    ┌────────────────────────────┐
                    │   Azure AI Services        │
                    │   (Multi-Service Resource) │
                    │                            │
                    │  • Computer Vision         │
                    │  • Form Recognizer         │
                    │  • Language Service        │
                    └────────────────────────────┘
                                 │
                                 │ Processed Results
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure OpenAI Service     │
                    │   (Synthesis & Analysis)   │
                    └────────────────────────────┘

📊 Resources Used:
  • Azure AI Services (Multi-service)
  • Azure OpenAI Service
  • Azure Storage Account

💰 Estimated Cost: ~$2.50 per lab session
"""


def get_lab16_17_diagram():
    """Lab 16-17: Production Applications"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                  LAB 16-17 - AZURE INFRASTRUCTURE                        ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                         End Users (Web Browser)                          │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ HTTPS Requests
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure App Service        │
                    │   (Web Application)        │
                    │   • Streamlit/FastAPI      │
                    │   • 1.75GB RAM             │
                    └────────────┬───────────────┘
                                 │
                                 ├─────────► Azure Functions
                                 │           • Serverless APIs
                                 │           • Event-driven
                                 │
                                 ├─────────► Azure OpenAI Service
                                 │           • GPT-4 / GPT-3.5
                                 │
                                 ├─────────► Azure AI Search
                                 │           • Document retrieval
                                 │
                                 ├─────────► Azure SQL Database
                                 │           • User data
                                 │           • Transaction logs
                                 │
                                 └─────────► Azure Key Vault
                                             • API Keys
                                             • Connection strings

📊 Resources Used:
  • Azure App Service (B1 tier)
  • Azure Functions (Consumption plan)
  • Full Azure AI stack

💰 Estimated Cost: ~$4.00 per lab session
"""


def get_lab18_19_20_diagram():
    """Lab 18-20: Advanced Banking Applications"""
    return """
╔══════════════════════════════════════════════════════════════════════════╗
║                  LAB 18-20 - AZURE INFRASTRUCTURE                        ║
╚══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                    Banking System Integration                            │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 │ Real-time Data
                                 ▼
                    ┌────────────────────────────┐
                    │   Azure SQL Database       │
                    │   • Transaction data       │
                    │   • Customer profiles      │
                    │   • Historical patterns    │
                    └────────────┬───────────────┘
                                 │
                                 ├─────────► Azure OpenAI Service
                                 │           • Pattern analysis
                                 │           • Anomaly detection
                                 │           • Report generation
                                 │
                                 ├─────────► Azure AI Search
                                 │           • Regulatory docs
                                 │           • Compliance search
                                 │
                                 ├─────────► Azure AI Services
                                 │           • Document processing
                                 │           • Identity verification
                                 │
                                 └─────────► Azure Functions
                                             • Real-time alerts
                                             • Automated workflows

                    ┌────────────────────────────┐
                    │   Azure App Service        │
                    │   (Dashboard & Reports)    │
                    └────────────────────────────┘

📊 Resources Used:
  • Complete Azure AI stack
  • Azure SQL Database (Gen5, 2 vCores)
  • Production-grade configuration

💰 Estimated Cost: ~$5.00 per lab session
"""


def display_diagram(lab_number: int):
    """
    Display infrastructure diagram for a specific lab
    
    Args:
        lab_number: Lab number (5-20)
    """
    diagrams = {
        5: get_lab05_diagram(),
        6: get_lab06_07_diagram(),
        7: get_lab06_07_diagram(),
        8: get_lab08_diagram(),
        9: get_lab09_diagram(),
        10: get_lab10_11_12_diagram(),
        11: get_lab10_11_12_diagram(),
        12: get_lab10_11_12_diagram(),
        13: get_lab13_14_15_diagram(),
        14: get_lab13_14_15_diagram(),
        15: get_lab13_14_15_diagram(),
        16: get_lab16_17_diagram(),
        17: get_lab16_17_diagram(),
        18: get_lab18_19_20_diagram(),
        19: get_lab18_19_20_diagram(),
        20: get_lab18_19_20_diagram(),
    }
    
    if lab_number in diagrams:
        print(diagrams[lab_number])
    else:
        print(f"No diagram available for Lab {lab_number}")


# Example usage
if __name__ == "__main__":
    display_diagram(5)

