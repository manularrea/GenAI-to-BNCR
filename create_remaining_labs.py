#!/usr/bin/env python3
"""
Script to generate all remaining lab notebooks (09-20) for BNCR GenAI Course
"""

import json
import os

# Lab configurations
LABS = {
    "09": {
        "title": "Embeddings and Semantic Search",
        "topics": [
            "Understanding embeddings",
            "Azure OpenAI embeddings API",
            "Vector similarity search",
            "Building a document search system",
            "Semantic search for banking FAQs"
        ],
        "exercises": [
            "Build FAQ search engine",
            "Product recommendation system",
            "Document similarity finder"
        ]
    },
    "10": {
        "title": "RAG (Retrieval-Augmented Generation)",
        "topics": [
            "RAG architecture overview",
            "Document chunking strategies",
            "Vector databases (Pinecone, Chroma)",
            "Building a banking knowledge base",
            "RAG for policy documents"
        ],
        "exercises": [
            "Build banking policy chatbot",
            "Implement document Q&A system",
            "Create product catalog RAG"
        ]
    },
    "11": {
        "title": "Azure AI Search Integration",
        "topics": [
            "Azure AI Search overview",
            "Indexing banking documents",
            "Hybrid search (keyword + semantic)",
            "Filtering and faceting",
            "Integration with Azure OpenAI"
        ],
        "exercises": [
            "Index banking documents",
            "Build hybrid search system",
            "Implement filtered search"
        ]
    },
    "12": {
        "title": "Content Moderation and Safety",
        "topics": [
            "Azure Content Safety API",
            "Detecting harmful content",
            "PII detection and redaction",
            "Jailbreak prevention",
            "Compliance and audit logging"
        ],
        "exercises": [
            "Implement content filter",
            "Build PII redaction system",
            "Create safety monitoring dashboard"
        ]
    },
    "13": {
        "title": "Fine-tuning for Banking Domain",
        "topics": [
            "When to fine-tune vs prompt engineering",
            "Preparing training data",
            "Azure OpenAI fine-tuning API",
            "Evaluation and validation",
            "Cost-benefit analysis"
        ],
        "exercises": [
            "Prepare fine-tuning dataset",
            "Fine-tune a model",
            "Evaluate model performance"
        ]
    },
    "14": {
        "title": "Multimodal AI - Vision and Documents",
        "topics": [
            "GPT-4 Vision capabilities",
            "Document analysis (checks, forms)",
            "OCR and data extraction",
            "Chart and graph understanding",
            "Banking document processing"
        ],
        "exercises": [
            "Extract data from checks",
            "Analyze financial statements",
            "Process loan application forms"
        ]
    },
    "15": {
        "title": "Agent Frameworks and LangChain",
        "topics": [
            "Introduction to LangChain",
            "Chains, agents, and tools",
            "Memory management",
            "Building autonomous agents",
            "Banking agent use cases"
        ],
        "exercises": [
            "Build multi-tool agent",
            "Create research agent",
            "Implement planning agent"
        ]
    },
    "16": {
        "title": "Production Deployment on Azure",
        "topics": [
            "Azure deployment options",
            "API Management and security",
            "Monitoring and logging",
            "Rate limiting and quotas",
            "Cost optimization"
        ],
        "exercises": [
            "Deploy API to Azure",
            "Configure monitoring",
            "Implement rate limiting"
        ]
    },
    "17": {
        "title": "Testing and Evaluation",
        "topics": [
            "LLM evaluation metrics",
            "A/B testing strategies",
            "Human evaluation",
            "Automated testing",
            "Regression detection"
        ],
        "exercises": [
            "Create test suite",
            "Implement evaluation metrics",
            "Build comparison dashboard"
        ]
    },
    "18": {
        "title": "Ethics, Bias, and Responsible AI",
        "topics": [
            "Identifying bias in AI systems",
            "Fairness metrics",
            "Transparency and explainability",
            "Regulatory compliance (GDPR, etc.)",
            "Microsoft Responsible AI principles"
        ],
        "exercises": [
            "Audit model for bias",
            "Create transparency report",
            "Implement fairness checks"
        ]
    },
    "19": {
        "title": "Cost Optimization and Performance",
        "topics": [
            "Token usage optimization",
            "Caching strategies",
            "Model selection (GPT-4 vs GPT-3.5)",
            "Batch processing",
            "Performance monitoring"
        ],
        "exercises": [
            "Implement caching system",
            "Optimize token usage",
            "Build cost monitoring dashboard"
        ]
    },
    "20": {
        "title": "Final Project - Banking AI Assistant",
        "topics": [
            "Project requirements",
            "Architecture design",
            "Implementation guidelines",
            "Testing and deployment",
            "Presentation and demo"
        ],
        "exercises": [
            "Build complete banking assistant",
            "Integrate all learned concepts",
            "Deploy and present solution"
        ]
    }
}

def create_notebook(lab_num, config):
    """Create a notebook for a given lab"""
    
    notebook = {
        "cells": [
            # Title cell
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Lab {lab_num}: {config['title']}\\n\\n"
                    "**Course:** Generative AI for Banking Sector  \\n"
                    "**Institution:** Banco Nacional de Costa Rica (BNCR)  \\n"
                    "**Instructor:** Manuela Larrea  \\n"
                    "**Duration:** 3 hours\\n\\n"
                    "---\\n\\n"
                    "## Learning Objectives\\n\\n"
                    "By the end of this lab, you will be able to:\\n\\n" +
                    "\\n".join([f"{i+1}. {topic}" for i, topic in enumerate(config['topics'])]) +
                    "\\n\\n---"
                ]
            },
            # Setup cell
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import os\\n"
                    "import sys\\n"
                    "from openai import AzureOpenAI\\n"
                    "from dotenv import load_dotenv\\n"
                    "import json\\n\\n"
                    "sys.path.append('../../utils')\\n"
                    "from azure_openai_helper import AzureOpenAIClient\\n\\n"
                    "load_dotenv()\\n"
                    "client = AzureOpenAIClient()\\n\\n"
                    'print("✓ Setup complete")'
                ]
            },
            # Introduction
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## Introduction\\n\\n"
                    f"In this lab, we will explore **{config['title']}** and its applications in the banking sector.\\n\\n"
                    "This is a critical component for building production-ready GenAI systems at BNCR."
                ]
            },
            # Main content sections
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Part 1: " + config['topics'][0]
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Implement " + config['topics'][0] + "\\n"
                    "# Code examples will be provided during the live session\\n"
                    "pass"
                ]
            },
            # Exercises
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 Practical Exercises\\n\\n" +
                    "\\n".join([f"### Exercise {i+1}: {ex}" for i, ex in enumerate(config['exercises'])])
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# TODO: Complete the exercises\\n"
                    "# Your code here:\\n"
                ]
            },
            # Summary
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Summary\\n\\n"
                    f"In this lab, you learned about {config['title']} and how to apply it in banking scenarios.\\n\\n"
                    "### Key Takeaways:\\n\\n" +
                    "\\n".join([f"- {topic}" for topic in config['topics']]) +
                    "\\n\\n### Best Practices:\\n\\n"
                    "1. Always validate inputs and outputs\\n"
                    "2. Implement proper error handling\\n"
                    "3. Monitor performance and costs\\n"
                    "4. Follow security best practices\\n"
                    "5. Document your implementations\\n\\n"
                    "---\\n\\n"
                    "**Instructor:** Manuela Larrea | manuela.larrea@idataglobal.com"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return notebook

def main():
    """Generate all notebooks"""
    base_path = "/home/ubuntu/GenAI-to-BNCR/labs"
    
    for lab_num, config in LABS.items():
        lab_dir = f"{base_path}/lab{lab_num}"
        os.makedirs(lab_dir, exist_ok=True)
        
        # Create notebook
        notebook = create_notebook(lab_num, config)
        notebook_path = f"{lab_dir}/lab{lab_num}_{config['title'].lower().replace(' ', '_').replace('-', '_')}.ipynb"
        
        with open(notebook_path, 'w') as f:
            json.dump(notebook, f, indent=2)
        
        # Create README
        readme_content = f"""# Lab {lab_num}: {config['title']}

## Overview

{config['title']} is essential for building production-ready GenAI applications in the banking sector.

## Topics Covered

{chr(10).join([f"- {topic}" for topic in config['topics']])}

## Exercises

{chr(10).join([f"{i+1}. {ex}" for i, ex in enumerate(config['exercises'])])}

## Prerequisites

- Completed Labs 05-{int(lab_num)-1:02d}
- Azure OpenAI access configured
- Python environment set up

## Duration

3 hours (including exercises)

## Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- Course datasets in `/datasets/banking/`

---

**Instructor:** Manuela Larrea | manuela.larrea@idataglobal.com
"""
        
        readme_path = f"{lab_dir}/README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print(f"✓ Created Lab {lab_num}: {config['title']}")

if __name__ == "__main__":
    main()
    print("\n✓ All lab notebooks created successfully!")

